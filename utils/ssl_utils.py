from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
from node_utils import NodeUtils
import re
import json
from urlparse import urlparse

class SSLUtils(object):
    '''
       SSLUtils class provides custom methods to perform various SSL related operations
    '''

    def __init__( self, fm ):
        self.fm = fm
        self.ns = NodeUtils(fm)

    def add_key_to_ssl_keystore( self, device_str, key_alias, key_type, file_source ):

        '''

        Add key to SSL keystore

        Parameters:
            device_str: device ip (or) hostname (or) cluster id
            key_alias: key alias
            key_type: key type ('private' or 'certificate' or 'pkcs12')
            comment: comment
            file_source: URL to download the file

        Return:
            1: Fail
            0: Success

        '''

        clusterId = self.ns.get_cluster_id ( device_str.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(device_str))
            return 1

        payload = {}

        url = urlparse(file_source)
        
        payload['alias'] = key_alias
        payload['type'] = key_type
        payload['fileSource'] = {}
        payload['fileSource']['protocol'] = url.scheme
        payload['fileSource']['hostname'] = url.netloc
        payload['fileSource']['path'] = url.path

        params = { 'clusterId' : clusterId }

        try:
            obj = self.fm.appskeystorekeys().post(params=params, data=payload)
            if re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.info("key added successfully")
                return 0
            else:
                self.fm.logger.error("Error while adding key to keystore")
                return 1

        except Exception as e:
            self.fm.logger.error("Exception while adding key")
            raise e

    def add_key_map_to_inline_ssl_profile( self, device_str, profile_alias, hostname, ssl_key_alias):

        '''

        Add key map entry to Inline SSL Profile

        Parameters:
            deviceStr: device ip (or) hostname (or) cluster id
            profile_alias: Inline SSL profile alias
            hostname: Server hostname or ip address
            ssl_key_alias: SSL key alias

        Return:
            1: Fail
            0: Success

        '''

        clusterId = self.ns.get_cluster_id ( device_str.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(device_str))
            return 1

        params = { 'clusterId' : clusterId }

        payload = {
            'hostname' : hostname,
            'key' : ssl_key_alias
        }

        try:
            obj = self.fm.appsinlineSslprofilesaliaskeyMap(alias=profile_alias).post(params=params, data=payload)
            if re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.info("Added keyMap entry to Inline SSL Profile successfully")
                return 0
            else:
                self.fm.logger.error("Error while adding keyMap entry to Inline SSL profile")
                return 1

        except Exception as e:
            self.fm.logger.error("Exception while adding keyMap entry to profile")
            raise e
