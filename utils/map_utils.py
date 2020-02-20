from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
from node_utils import NodeUtils
import re
import json

class MapUtils(object):

    '''
       MapUtils class provides custom methods to perform various map related operations
    '''

    def __init__( self, fm, ns ):
        self.fm = fm
        self.ns = ns
        self.cluster_maps = self._create_cluster_maps_dict()

    def _create_cluster_maps_dict( self ):
        
        '''

        Method that creates the dict for all devices and the list of maps associated with it

        Return:
            cluster_maps: Dict of all clusters and its maps

        '''
    
        cluster_maps = {}

        if len(self.fm.device_list):
            for node in self.fm.device_list:
                clusterId = ""
                m = node.split(":")
                clusterId = m[2]

                if clusterId == 'None':
                    self.fm.logger.error("Error getting clusterId for {}".format(node))
                    return

                try:
                    params = { 'clusterId' : clusterId }
                    obj = self.fm.maps().get(params=params)
                    if re.search(r"20(\d)", str(obj.status_code)):
                        js = obj.content
                        if len(js['maps']):
                            cluster_maps[clusterId] = js['maps']
                        else:
                            cluster_maps[clusterId] = []

                except Exception as e:
                    self.fm.logger.error("Exception while getting map inventory")
                    raise e

        else:
            self.fm.logger.error("device_list empty!")

        return cluster_maps

    def get_maps_from_all_devices( self ):

        '''

        Method to get maps associated with all the devices

        Return:
            cluster_maps: Dict of all clusters and its maps

        '''

        return self.cluster_maps


    def get_maps( self, device_str ):

        '''

        Method to get all maps associated with the one or more devices

        Parameters:
            device_str: device ip (or) hostname (or) cluster id

        Return:
            mapList: List of maps associated with a specific cluster

        '''

        mapList = []

        clusterId = self.ns.get_cluster_id ( device_str.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(device_str))
            return 1

        mapList = self.cluster_maps[clusterId]

        return mapList

    def get_maps_by_port( self, clusterId, portId ):

        '''

        Method to get all maps associated with the given port

        Parameters:
            clusterId: cluster id
            portId: port id

        Return:
            mapList: On a given cluster, list of maps associated with a specific port 

        '''

        mapList = []

        try:
            params = { 'clusterId' : clusterId, 'portId' : portId }

            obj = self.fm.maps().get(params=params)
            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                mapList = js['maps']
            else:
                self.fm.logger.error("Error getting maps for port {}".format(portId))

            return mapList

        except Exception as e:
            self.fm.logger.error("Exception while getting map inventory")
            raise e


    def create_map( self, device_str, payload={} ):

        '''

        Create map on the given cluster using the payload provided.

        Parameters:
            device_str: device ip (or) hostname (or) cluster id
            payload: map specific input in dictionary format (like below)

                     data = {
                         'alias': 'test-map-1',
                         'subType': 'byRule',
                         'srcPorts': ['1/1/x1'],
                         'type': 'regular',
                         'dstPorts': ['1/1/x2'],
                         'rules': {
                             'dropRules': [],
                             'passRules': [
                              {
                                  'comment': '',
                                   'bidi': False,
                                   'matches': [{
                                        'type': 'ipVer',
                                        'value': 'v4'
                                   }],
                                   'ruleId': 1
                              },
                              {
                                   'comment': '',
                                   'bidi': False,
                                   'matches': [{
                                       'type': 'ipVer',
                                       'value': 'v6'
                                   }],
                                   'ruleId': 2
                              }
                              ]
                         }
                    }

            Return:
                1: Fail
                0: Success

        '''

        clusterId = self.ns.get_cluster_id ( device_str.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(device_str))
            return 1

        params = { 'clusterId' : clusterId }

        try:
            obj = self.fm.maps().post(params=params, data=payload)
            if re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.info("map created successfully")
                return 0
            else:
                self.fm.logger.error("Error while creating map")
                return 1

        except Exception as e:
            self.fm.logger.error("Exception while creating map")
            raise e

    def update_map( self, device_str, map_alias, payload={} ):

        '''

        Incremental update to an existing map

        Parameters:
            deviceStr: device ip (or) hostname (or) cluster id
            map_alias: map alias
            payload: map specific input in dictionary format (like below)

                     data = {
                         'alias': 'test-map-1',
                         'subType': 'byRule',
                         'srcPorts': ['1/1/x1'],
                         'type': 'regular',
                         'dstPorts': ['1/1/x2'],
                         'rules': {
                             'dropRules': [],
                             'passRules': [
                             {
                                 'comment': '',
                                 'bidi': False,
                                 'matches': [{
                                     'type': 'ipVer',
                                     'value': 'v4'
                                 }],
                                 'ruleId': 1
                             },
                             {
                                 'comment': '',
                                 'bidi': False,
                                 'matches': [{
                                   'type': 'ipVer',
                                   'value': 'v6'
                                 }],
                                 'ruleId': 2
                             }
                             ]
                         }
                    }

           Return:
               1: Fail
               0: Success

        '''

        clusterId = self.ns.get_cluster_id ( device_str.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(device_str))
            return 1

        params = { 'clusterId' : clusterId }

        try:
            obj = self.fm.mapsalias(alias=map_alias).patch(params=params, data=payload)
            if re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.info("map updated successfully")
                return 0
            else:
                self.fm.logger.error("Error while updating map")
                return 1

        except Exception as e:
            self.fm.logger.error("Exception while updating map")
            raise e

    def add_map_rule( self, device_str, map_alias, rule_type, payload={} ):

        '''

        Add map rule to an existing map

        Parameters:
            deviceStr: device ip (or) hostname (or) cluster id
            map_alias: map alias
            rule_type: 'pass' or 'drop'
            payload: map rule in dictionary format (like below)

                    data = {
                        'ruleId': 3,
                        'comment': '',
                        'bidi': False,
                        'matches': [
                            {
                                'type': 'macSrc',
                                'value': '00:11:22:33:44:55'
                            }
                        ]
                    }

            Return:
                1: Fail
                0: Success

        '''

        clusterId = self.ns.get_cluster_id ( device_str.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(device_str))
            return 1

        params = { 'clusterId' : clusterId }

        try:
            obj = self.fm.mapsaliasrulesruleType(alias=map_alias, ruleType=rule_type).post(params=params, data=payload)
            if re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.info("Rule add to successfully to map {}".format(map_alias))
                return 0
            else:
                self.fm.logger.error("Error while adding rule to map {}".format(map_alias))
                return 1

        except Exception as e:
            self.fm.logger.error("Exception while adding rule to map {}".format(map_alias))
            raise e

    def delete_map_by_alias( self, device_str, alias ):

        '''

        Method to delete a map by alias

        Parameters:
            device_str: device ip (or) hostname (or) cluster id
            alias: map alias

        Return:
            1: Fail
            0: Success

        '''
 
        clusterId = self.ns.get_cluster_id ( device_str.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(node))
            return 1

        try:
            params = { 'clusterId' : clusterId }

            obj = self.fm.mapsalias(alias=alias).delete(params=params)
            if re.search(r"20(\d)", str(obj.status_code)):
                return 0
            else:
                return 1

        except Exception as e:
            self.fm.logger.error("Exception while deleting map by alias")
            raise e
