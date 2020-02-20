"""
This class provides method to create a binding to a specific FM rest api interface.
"""

import sys
import requests
import functools
import tapioca
import os
import logging
import time
import re

from datetime import datetime
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from resource_mapping import RESOURCE_MAPPING_v09
from resource_mapping import RESOURCE_MAPPING_v13

logger = None

class FmClientAdapterVersion09(tapioca.JSONAdapterMixin, tapioca.TapiocaAdapter):
    """
    Description: adaptor class to bind to FM rest api version 0.9 for authentication
    """

    resource_mapping = RESOURCE_MAPPING_v09
    requests.packages.urllib3.disable_warnings()

    def get_request_kwargs(self, api_params, *args, **kwargs):
        """
        Description: internal method to return calling params
        :api_params: list - key/value pair passed by caller
        :args: list
        :kwargs: dict
        :return: dict
        """

        params = super(FmClientAdapterVersion09, self).get_request_kwargs(
            api_params, *args, **kwargs)

        return params

    def get_api_root(self, api_params):
        """
        Description: internal method to get server endpoint 
        :api_params: list
        :return: string
        """

        self.fm_url = 'https://{}/api/0.9'.format(api_params['fm_url'])
        return self.fm_url

    def get_iterator_list(self, response_data):
            return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                             response_data, response):
        pass

class FmClientAdapterVersion(tapioca.JSONAdapterMixin, tapioca.TapiocaAdapter):
    """
    Description: adaptor class to bind to FM rest api version 1.3
    """
    resource_mapping = RESOURCE_MAPPING_v13
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def get_request_kwargs(self, api_params, *args, **kwargs):
        """
        Description: internal method to return calling params
        :api_params: list
        :args: list
        :kwargs: dict
        :return: dict
        """
        params = super(FmClientAdapterVersion, self).get_request_kwargs(
            api_params, *args, **kwargs)

        return params

    def get_api_root(self, api_params):
        """
        Description: internal method to get server endpoint 
        :api_params: list
        :return: string
        """
        self.fm_url = 'https://{}/api/{}'.format(api_params['fm_url'], api_params['version'])
        return self.fm_url

    def get_iterator_list(self, response_data):
            return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                             response_data, response):
        pass

def format_result(raw_result, result):
    """
    Description: method to de-serialize the return response from tapioca
    :raw_result: object - object returned by the rest call
    :result: dict - content retgurned by the rest call
    :return: dict
    """

    data = { 
        'status_code': raw_result.status_code,
        'content': result,
        'raw_content': raw_result}

    return data

class apiResult(object):
    """
    Description: class to provide verification methods
    """

    def __init__(self, raw_response, processed_response):
        self.status_code = raw_response.status_code
        self.content = processed_response
        self.raw_content = raw_response

    def __nonzero__( self):
        """Success if status_code in the 2xx range
        """
        return self.status_code >= 200 and self.status_code < 300

    def __iter__ (self):
        return iter(self.content.keys())

    def __getitem__ (self, key):
        return self.content [key] if key in self.content else None

    def __contains__ (self, key):
        return key in self.content

    def __str__ (self):
        if self.content and type (self.content) == dict:
            return "status_code: {}, ".format (self.status_code) + ", ".join (["{}:{}".format (k, v) for k, v in self.content.iteritems()])
        else:
            return "status_code: {}, {}".format (self.status_code, self.content)

    def equals (self, *args, **kwargs):
        """Verify responsed content to contain the same attribute and value set as specified.

        Parametters:
            args: List of attributes in combination to check for existence (not checking for values of):
                equals ('attr1', 'attr2', ...)
            args: Dictionary of attribute=value pairs to check (for both attributes and values):
                equals ({'attr1': 'value1', 'attr2': 'value2',...}, ...)
            kwargs: List of attribute=value pairs to check (for both attributes and values):
                equals (attr1='value1', attr2='value2', ...)

        Return:
            True -- if responsed content has the same attributes and values as specified.
            False -- otherwise
        """
        # Combine all attributes
        attr_set = set ([k for k in kwargs] + [k for k in args if type (k) != dict])
        for arg in args:
            if type (arg) == dict:
                attr_set.update ([k for k in arg])
        # Make sure the number of attributes specified is the same as the responsed content's
        if len (attr_set) != len (self.content): return False

        # Now verify all the specified attributes in the responsed content set
        return self.contains (*args, **kwargs)

    def contains (self, *args, **kwargs):
        """Verify specified attributes and values are subset of the responsed content.

        Parametters:
            args: List of attributes in combination to check for existent (not checking for values of):
                equals ('attr1', 'attr2', ...)
            args: Dictionary of attribute=value pairs to check (for both attributes and values):
                equals ({'attr1': 'value1', 'attr2': 'value2', ...}, ...)
            kwargs: List of attribute=value pairs to check (for both attributes and values):
                equals (attr1='value1', attr2='value2', ...)

        Return:
            True -- if the responsed content contains attributes and values specified.
            False -- otherwise
        """
        for arg in args:
            if type (arg) == dict:
                # If specified dictionary is a subset of the content set
                # contains ( {...} )
                for attr in arg:
                    if attr not in self.content: return False
                    if arg [attr] != self.content [attr]: return False
            else:
                # If specified attributes is in the content set
                # contains ( 'attr1', 'attr2', ... )
                if arg not in self.content: return False

        for attr in kwargs:
            # If specified attrword argument set is a subset of the content set
            # contains ( attr1='value1', attr2='value2', ... )
            if attr not in self.content: return False
            if kwargs [attr] != self.content [attr]: return False

        return True

    def assertEqual (self, message, *args, **kwargs):
        """Verify the responsed content to contain the same attribute and value set specified.

        Parametters:
            message: Message text to be asserted. The message text may contain the following parameters:
                attr -- To be substituted with attribute name, for examples:
                    assertEqual ("Attribute '{attr}' is expected, but not found.", 'attr1', 'attr2', 'attr3', ...)
                    If 'attr2' does not exist in the result set, the message would be:
                        Attribute 'attr2' is expected, but not found.
                expected -- To be substituted with expected value (values specified by the method arguments)
                actual -- To be substituted with actual value (values from self.content)
                    assertEqual ("Value mismatched: attribute: '{attr}', expected: '{}', actual: '{}'.",
                                    attr='expeced value1', attr2='expected value2', ...)
                    If attr2 value would not match, for example, with the actual value 'actual value2',
                    the asserting message would be:
                        Value mismatched: attribute: 'attr2', expected: 'expected value2', actual: 'actual value2'.
            args: List of attributes in combination to check for existent (not checking for values of):

            args: List of attributes in combination to check for existent (not checking for values of):
                assertEqual ('attr1', 'attr2', ...)
            args: Dictionary of attribute=value pairs to check (for both attributes and values):
                assertEqual ({'attr1': 'value1', 'attr2': 'value2', ...}, ...)
            kwargs: List of attribute=value pairs to check (for both attributes and values):
                assertEqual (attr1='value1', attr2='value2', ...)

        Assertions:
            1. Expected attribute set not being the same as of self.content.
            2. Otherwise as assertContain.
        """
        # Combine all attributes
        attr_set = set ([k for k in kwargs] + [k for k in args if type (k) != dict])
        for arg in args:
            if type (arg) == dict:
                attr_set.update ([k for k in arg])
        # Make sure the number of attributes specified is the same as the responsed content's
        assert len (attr_set) == len (self.content), message.format (attr='__attr__',
                    expected=[a for a in attr_set], actual=[k for k in self.content])

        # Now verify all the specified attributes in the responsed content set
        return self.assertContain (message, *args, **kwargs)

    def assertContain (self, message, *args, **kwargs):
        """Verify specified attributes and values are subset of the responsed content.

        Parametters:
            message: Message text to be asserted. The message text may contain the following parameters:
                attr -- To be substituted with attribute name, for examples:
                    assertContain ("Attribute '{attr}' is expected, but not found.", 'attr1', 'attr2', 'attr3', ...)
                    If 'attr2' does not exist in the result set, the message would be:
                        Attribute 'attr2' is expected, but not found.
                expected -- To be substituted with expected value (values specified by the method arguments)
                actual -- To be substituted with actual value (values from self.content)
                    assertContain ("Value mismatched: attribute: '{attr}', expected: '{}', actual: '{}'.",
                                    attr='expeced value1', attr2='expected value2', ...)
                    If attr2 value would not match, for example, with the actual value 'actual value2',
                    the asserting message would be:
                        Value mismatched: attribute: 'attr2', expected: 'expected value2', actual: 'actual value2'.
            args: List of attributes in combination to check for existent (not checking for values of):
                assertContain ('attr1', 'attr2', ...)
                assertContain ({'attr1': 'value1', 'attr2': 'value2', ...)
            kwargs: List of attribute=value pairs to check (for both attributes and values):
                assertContain (attr1='value1', attr2='value2', ...)

        Assertions:
            1. If any specified attribute does not exist.
            2. If any specified attribute value does not match.
        """
        for arg in args:
            if type (arg) == dict:
                # If specified dictionary is a subset of the content set
                # contains ( {...} )
                for attr in arg:
                    assert  attr in self.content, message.format (attr=attr, expected=attr, actual=None)
                    assert arg [attr] == self.content [attr], message.format (attr=attr,
                                         expected=arg [attr], actual=self.content [attr])
            else:
                # If specified attributes is in the content set
                # contains ( 'attr1', 'attr2', ... )
                assert arg in self.content, message.format (attr=arg, expected=arg, actual=None)

        for attr in kwargs:
            # If specified attrword argument set is a subset of the content set
            # contains ( attr1='value1', attr2='value2', ... )
            assert attr in self.content, message.format (attr=attr, expected=attr, actual=None)
            assert kwargs [attr] == self.content [attr], message.format (attr=attr,
                                    expected=kwargs [attr], actual=self.content [attr])

class modify_TapiocaClientExecutor(tapioca.tapioca.TapiocaClientExecutor):
    """
    Description: method that overrided TapiocaClientExecutor _make_request method to return custom response data
    """

    @staticmethod 
    def _make_request(self, request_method, refresh_token=None, *args, **kwargs):
        # default ssl verification to false
        if 'verify' not in  kwargs:
            kwargs['verify'] = False

        # set auth login for the request
        kwargs['auth'] = self._api_params['auth']

        if 'url' not in kwargs:
            kwargs['url'] = self._data

        request_kwargs = self._api.get_request_kwargs(
            self._api_params, request_method, *args, **kwargs)
        logger.info("api request method: {}".format(request_method))
        logger.info("api request endpoint: {}".format(request_kwargs['url']))
        logger.info("api request payload: {}".format(request_kwargs['data']))

        # make the the request
        response = self._session.request(request_method, **request_kwargs)

        try:
            if response.status_code < 200 or response.status_code > 205:
                logger.error("status code: {}".format(response.status_code))
                logger.error("content: {}".format(response.content))
            else:
                logger.info("status code: {}".format(response.status_code))
                logger.info("content: {}".format(response.content))
        except Exception as e:
            logger.error("failed to get response: {}".format(e.message))

        try:
            data = apiResult(response, self._api.process_response(response))
        except tapioca.tapioca.ResponseProcessException as e:
            data = apiResult(response, response.content)

        return data

class FmClientVersion(FmClientAdapterVersion):
    def __init__(self, url, version, username, password):
        """
        Description: constructor for FM client

        :url: string - fm url
        :version: string - api version
        :username: string - authorization username
        :password: string - authorization password
        """
        fmApiBinding = tapioca.generate_wrapper_from_adapter(FmClientAdapterVersion)
        self.make_call = fmApiBinding(fm_url=url, version=version, auth=(username, password))

class FmClient(object):
    """
    Description: FM api client class to create binding to a specific FM server 
    """
    def __init__(self, fm_ip, username=None, password=None, log_dir=None, log_name=None, screen_out=False):
        """
        Construtor

        :fm_ip: string - fm server ip
        :username: string - admin user name
        :password: string - admin password
        :log_dir: string - directory where the access log will be generated
        "log_name: string - log file name that will be generated in the log_dir
        :return: none
        """

        import tapioca
        self.resources = []
        self.username = username
        self.password = password
        self.api_version = self._get_api_version(url=fm_ip, username=username, password=password)
        self.init_log(log_dir, log_name, screen_out)
        # initialize 0.9 version for private apis
        fmApiBinding = tapioca.generate_wrapper_from_adapter(FmClientAdapterVersion09)
        self.make_call = fmApiBinding(fm_url=fm_ip, auth=(username, password))
        self.fmApiVersion = FmClientVersion(url=fm_ip, version=self.api_version, username=username, password=password)
        self.device_list = []
        sys.modules['tapioca'].tapioca.TapiocaClientExecutor._make_request = modify_TapiocaClientExecutor._make_request
        self._fetch_methods()

    def _get_api_version(self, url, username, password):
        """
        Description: private method to get FM api version

        :username: string - login username
        :password: string - login password
        :return: version string
        """

        login = (username, password)
        content = requests.get("https://{}/api/version".format(url), verify=False, auth=login)
        if content.status_code != 200:
            # if fail to get version string, default to "v1.3"
            api_version = "v1.3"
        else:
            # in case content changes, default to "v1.3"
            try:
                api_version = content.json()['apiVersion']
            except Exception:
                api_version = "v1.3"

        return api_version

    def _fetch_methods(self):
        """
        Description: internal method to associate methods to the client object
        """

        # 0.9 api
        for item in dir(self.make_call):
            setattr(FmClient, item, classmethod(getattr(self.make_call, item)))
        # 1.3 api
        for item in dir(self.fmApiVersion.make_call):
            self.resources.append(item)
            func = getattr(self.fmApiVersion.make_call, item)
            setattr(FmClient, item, classmethod(func))

    def init_log(self, path=None, log_name=None, screen_out=False):
        """
        Description: method to create log file

        :path:string - path of the log
        :return: none
        """

        global logger
        script_name = "{}.log".format(sys.argv[0].split("/")[-1].split(".")[0])

        try:
            # set log file path
            self.logger = logging.getLogger()
            if path == None and log_name == None:
                path = "{}/{}".format(os.getcwd(), script_name)
            elif path == None and log_name != None:
                path = "{}/{}".format(os.getcwd(), log_name)
            elif path != None and log_name == None:
                path = "{}/{}".format(path, script_name)
            elif path != None and log_name != None:
                path = "{}/{}".format(path, log_name)
            log_base_dir = os.path.dirname(path)
            log_filename = os.path.basename(path)

            if not os.path.isdir(log_base_dir):
                os.makedirs(log_base_dir)

            # file handler
            try:
                handler = logging.FileHandler(path, mode='w')
            except Exception as e:
                handler = logging.FileHandler(os.path.join("/tmp/", log_filename), mode='w')

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # stdout handler
            if screen_out: 
                stdout_handler = logging.StreamHandler(sys.stdout)
                stdout_handler.setFormatter(formatter)
                self.logger.addHandler(stdout_handler)
 
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.DEBUG)
            self.logger.info("log initialized")
            logger = self.logger
        except Exception as e:
            raise e


    def rediscover_nodes(self, clusterId):

        '''

        Re-discover a standalone node or cluster

        Parameters:
            clusterId: device ip (or) cluster id

        Return:
            0 : For success
            1 : For failure

        Example:

           ret = rediscover_nodes("10.115.32.5")
           ret = rediscover_nodes("Cluster-201")

        '''

        try:
            time.sleep(10)
            params = { "clusterId" : clusterId }
            obj = self.nodes().put(params=params)

            if re.search(r"20(\d)", str(obj.status_code)):
                return 0
            else:
                self.logger.error("Device re-discovery failed ..")
                return 1

        except Exception as e:
            self.logger.error("Exception while triggering device re-discovery")
            raise e

        return 0
