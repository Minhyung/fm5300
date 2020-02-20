from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
import re

class NodeUtils(object):

    '''
       NodeUtils class provides custom methods to perform various operations on nodes (for both standalone and clusters)       

    '''

    def __init__(self, fm):
        self.fm = fm
        if len(self.fm.device_list) == 0:
            self._create_device_list()

    def _create_device_list(self):

        '''

        Creates device list for all the devices managed by FM

        Return:
            d_list: List of devices managed by FM

        '''

        try:
            obj = self.fm.nodesflat().get()
            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                for node in js.get('nodes'):
                    if node.get('discOutcome') == 'ok':
                        buf = []
                        if 'boxId' in node:
                            boxId = node.get('boxId')
                        else:
                            boxId = 'None'

                        if 'hostname' in node:
                            hostname = node.get('hostname')
                        else:
                            hostname = 'None'

                        buf = node.get('deviceIp') + ":" + hostname + ":" + node.get('clusterId') + ":" + boxId + ":" + node.get('model') + ":" + node.get('swVersion') + ":" + node.get('clusterMode') + ":" + node.get('discOutcome') + ":" + node.get('topoNodeId') + ":"
                        self.fm.device_list.append(buf)

            else:
                self.fm.logger.error("get node failed")

        except Exception as e:
            self.fm.logger.error("failed to get all nodes")
            raise e

    def get_cluster_id( self, device_str="" ):

        '''

        Returns the cluster id for device hostname or ip address

        Parameters:
            device_str: device ip (or) hostname (or) cluster id

        Return:
            cluster_id: For success
            None: For failure

        '''

        cluster_id = "None"

        for l in self.fm.device_list:
            if device_str in l:
                m1 = l.split(":")
                cluster_id = m1[2]
                return cluster_id

        return cluster_id

    def _find_match( self, devicefilter={}, nodes=[]):

        '''

        Returns matching device list (from nodes) that matches all the filter criteria

        Parameters:
            devicefilter: dictionary with one or more of the keys ( 'deviceIp', 'operStatus',
                          'swVersion', 'hostname', 'clusterMode', 'deviceId', 'healthState', 'model' )
            nodes: List of devices

        Return:
            match: List of devices that match the devicefilter 

        '''

        match = []
        for node in nodes:
            try:
                for key, value in devicefilter.items():
                    if value and value.strip() in node.get(key):
                        if node not in match:
                            match.append(node)
                    else:
                        if node in match:
                            match.remove(node)
                        break

            except KeyError as err:
                pass

        return match


    def get_device_inventory( self, devicefilter={} ):

        '''

        Get device inventory from FM based on the device filter

        Parameters:
            devicefilter: dictionary with one or more of the keys ( 'deviceIp', 'operStatus',
                          'swVersion', 'hostname', 'clusterMode', 'deviceId', 'healthState', 'model' )

        Return:
            node_list: List of matched devices

        Example:

            out = client.get_device_inventory(devicefilter={'hostname' : 'TA40'})
            out = client.get_device_inventory(devicefilter={'hostname' : 'TA40'})
            out = client.get_device_inventory(devicefilter={'deviceIp': '10.115.32', 'model': 'HD8'})
            out = client.get_device_inventory(devicefilter={'deviceIp': '10.115.32', 'hostname': 'HD8', 'model': 'HD8'})

        '''

        node_list = []

        try:
            obj = self.fm.nodesflat().get()

            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                if not devicefilter:
                  return js.get('nodes')
                node_list = self._find_match( devicefilter, js.get('nodes') )
            else:
                self.fm.logger.error("get node failed")

            return node_list

        except Exception as e:
            self.fm.logger.error("failed to get all nodes")
            raise e

    def add_nodes_from_file( self, csvfile, de_limiter=';' ):

        '''

        Method to add one or more nodes from CSV file

        Parameters:
            csvfile: csvfile with all device details
                     (First line of CSV file is the header (contains 'name', 'username', 'password'))
            de_limiter: Delimiter used in the csvfile

        Return:
            0: For success
            1: For failure


        '''

        with open(csvfile) as fp:

            nodeAddSpecs = []

            count = 0
            for line in fp:

                if count == 0:
                    count += 1
                    continue

                buf = line.rstrip('\n')

                [nodeIp, nodeUser, nodePasswd] = buf.strip(de_limiter).split(de_limiter)

                p = {
                    "nodeAddress": nodeIp,
                    "username": nodeUser,
                    "password": nodePasswd
                }

                nodeAddSpecs.append(p)
                count += 1

            payload = {"nodeAddSpecs" : nodeAddSpecs}

            try: 
                obj = self.fm.nodes().post(data=payload)
                if re.search(r"20(\d)", str(obj.status_code)):
                    self.fm.logger.info("Node added successfully")
                    return 0
                elif obj.status_code == 409:
                    self.fm.logger.info("Node already managed by FM")
                    return 0
                else:
                    self.fm.logger.error("Error while adding the node to FM, {}".format(obj.content))
                    return 1

            except Exception as e:
                self.fm.logger.error("failed to add nodes to FM, payload: {}".format(payload))
                raise e

    def add_node_to_fm( self, nodeIp, nodeUser, nodePasswd ):

        '''

        Method to add a node to FM

        Parameters:
            nodeIp: device ip
            nodeUser: device user
            nodePasswd: device password

        Return:
            0: For success
            1: For failure

        '''

        payload = {
            "nodeAddSpecs": [
                {
                    "nodeAddress": nodeIp,
                    "username": nodeUser,
                    "password": nodePasswd
                }]
        }   

        try: 
            obj = self.fm.nodes().post(data=payload)

            if re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.info("Node added successfully")
                return 0
            elif obj.status_code == 409:
                self.fm.logger.info("Node already managed by FM")
                return 0
            else:
                self.fm.logger.error("Error while adding the node to FM, {}".format(obj.content))
                return 1

        except Exception as e:
            self.fm.logger.error("failed to add nodes to FM, payload: {}".format(payload))
            raise e

    def delete_node( self, device_str ):

        '''

        Method to delete a node to FM

        Parameters:
            device_str: device ipaddress or hostname to be deleted from FM

        Return:
            0: For success
            1: For failure

        '''

        clusterId = self.get_cluster_id ( device_str.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(device_str))
            return 1

        try: 
            payload = { 'clusterId': clusterId }

            obj = self.fm.nodes().delete(params=payload)

            if re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.info("Node deleted successfully")
                return 0
            else:
                self.fm.logger.error("Error while deleting the node from FM, {}".format(obj.content))
                return 1

        except Exception as e:
            self.fm.logger.error("failed to delete node from FM, payload: {}".format(payload))
            raise e
