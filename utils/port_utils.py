from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
from node_utils import NodeUtils
from map_utils import MapUtils
import re
import json
from collections import defaultdict

class PortUtils(object):

    '''
       PortUtils class provides custom methods to perform various port related operations
    '''

    def __init__( self, fm, ns ):
        self.fm = fm
        self.ns = ns
        self.cluster_ports = self._create_cluster_ports_dict()

    def _create_cluster_ports_dict( self ):

        '''

        Method that creates the dict for all devices and the list of ports associated with it

        Return:
            cluster_ports: Dict of all clusters and the associated ports

        '''

        cluster_ports = {}

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
                    obj = self.fm.inventoryports().get(params=params)
                    if re.search(r"20(\d)", str(obj.status_code)):
                        js = obj.content
                        if len(js['ports']):
                            cluster_ports[clusterId] = js['ports']
                        else:
                            cluster_ports[clusterId] = []
                            self.fm.logger.error("Port list empty for cluster {}".format(clusterId))

                except Exception as e:
                    self.fm.logger.error("Exception while getting port inventory")
                    raise e

        else:
            self.fm.logger.error("device_list empty!")

        return cluster_ports

    def get_port_count( self, clusterId ):

        try:
            params = { 'clusterId' : clusterId }
            obj = self.fm.inventoryports().get(params=params)
            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                return len(js['ports'])

        except Exception as e:
            self.fm.logger.error("Exception while getting port inventory")
            raise e

    def get_port_config_count( self, clusterId ):

        try:
            params = { 'clusterId' : clusterId }
            obj = self.fm.portConfigportConfigs().get(params=params)
            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                return len(js['portConfigs'])

        except Exception as e:
            self.fm.logger.error("Exception while getting portConfigs inventory")
            raise e

    def get_ports_from_all_devices( self ):

        '''

        Return the list of all ports for all devices

        Return:
            cluster_ports: Dict of cluster and associated ports
           
        '''

        return self.cluster_ports


    def get_ports_by_type( self, device_str, port_filter=[] ):

        '''

        Return the list of ports (of one or more types) for a given cluster

        Parameters:
            device_str: device ip (or) hostname (or) cluster id
            port_filter: one or more of port type ("network" or "tool" or "stack" or "gateway" or "inline-net" or
                         "inline-tool" or "hybrid" or "gigasmart")

        Return:
            return_list: List of ports matching the filter
     
        '''

        return_list = []

        clusterId = self.ns.get_cluster_id ( device_str.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(device_str))
            return return_list

        portList = self.cluster_ports[clusterId]

        ports_by_type = defaultdict(list)

        for port in portList:
            if port['portType'] == "gigasmart":
                ports_by_type[port['portType']].append(port)
            else:
                port_config_dict = {}
                p_ort = port['portId'].replace('/', '_')
                ports_by_type[port['portType']].append(port)

        if not port_filter:
            return self.cluster_ports[clusterId]

        else:
            for f in port_filter:
                return_list = return_list + ports_by_type[f]

        return return_list

    def get_ports_by_status( self, device_str, adminStatus=None, operStatus=None ):

        '''

        Return the list of ports (matching the status) for a given device or for all devices managed by FM

        Parameters:
            device_str: device ip (or) hostname (or) cluster id
            adminStatus: 'up' or 'down'
            operStatus: 'up' or 'down'

        Return:
            return_list: List of ports matching the adminStatus and operStatus

        '''

        return_list = []

        clusterId = self.ns.get_cluster_id ( device_str.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(device_str))
            return return_list

        if not adminStatus and not operStatus:
            return self.cluster_ports[clusterId]

        for port in self.cluster_ports[clusterId]:
            if not adminStatus and port['operStatus'] == operStatus.lower():
                return_list.append(port)
            elif not operStatus and port['adminStatus'] == adminStatus.lower():
                return_list.append(port)
            elif adminStatus and operStatus and port['adminStatus'] == adminStatus.lower() and port['operStatus'] == operStatus.lower():
                return_list.append(port)

        return return_list

    def _expand( self, ports ):

        '''

        Expand the dotted or comma separated port ranges to list of ports

        Parameters:
            ports: range of ports (separated by "," or "..")

        Return:
            result: List of ports

        '''

        result = []
        pattern = re.compile(r"^(.*?)(\d+)$")
        if ".." in ports:
            # get the borders and the common reusable part
            borders = [pattern.match(border).groups() for border in ports.split('..')]
            (common_part, start), (_, end) = borders

            for x in range(int(start), int(end) + 1):
                result.append("%s%d" % (common_part, x))

        elif "," in ports.strip():
            result = ports.split(",")

        return result

    def configure_ports( self, deviceStr, portId, **kwargs ):

        '''

        Configure single or multiple ports on a given device

        Parameters:
            deviceStr: device ip (or) cluster id (or) hostname
            portId: port id (can be 1/1/x1 or 1/1/x1..1/1/x3 or 1/1/x1,1/1/x2,1/1/x3)
            adminStatus: "up" or "down"

        Return:
            0 : For success
            1 : For failure

        Example:

           ret = configure_ports(deviceStr="10.115.32.5", portId="1/1/x1", portType="network", adminStatus="up")
           ret = configure_ports(deviceStr="10.115.32.5", portId="1/1/x2", portType="tool", adminStatus="up")
           ret = configure_ports(deviceStr="10.115.32.5", portId="1/1/x1..1/1/x3", portType="network", adminStatus="up")
           ret = configure_ports(deviceStr="10.115.32.5", portId="1/1/x1,1/1/x2,1/1/x3", portType="tool", adminStatus="up")

        '''

        clusterId = ""
        portList = []
        payload = {}

        if "," in portId or ".." in portId:
            portList = self._expand(portId)
        else:
            portList.append(portId) 

        clusterId = self.ns.get_cluster_id ( deviceStr.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(deviceStr))
            return 1
    
        for portId in portList:

            payload["portId"] = portId

            for k, v in kwargs.items():
                if k:
                    payload[k] = v 

            p_ortId = re.sub("/", "_", portId)

            try:
                params = { 'clusterId' : clusterId }
 
                obj = self.fm.inventoryportsportId(portId=p_ortId).patch(params=params, data=payload)

                if not re.search(r"20(\d)", str(obj.status_code)):
                    self.fm.logger.error("Configure ports failed")
                    return 1

            except Exception as e:
                self.fm.logger.error("Configure ports failed")
                raise e

        return 0

    def configure_port_config( self, deviceStr, portId, **kwargs ):

        '''

        Configure single or multiple ports on a given device

        Parameters:
            deviceStr: device ip (or) cluster id (or) hostname
            portId: port id (can be 1/1/x1 or 1/1/x1..1/1/x3 or 1/1/x1,1/1/x2,1/1/x3)
            adminStatus: "up" or "down"

        Return:
            0 : For success
            1 : For failure

        Example:

           ret = configure_port_config(deviceStr="10.115.32.5", portId="1/1/x1", neighborDiscovery="all", alarmThreshold=95, alarmThresholdLow=60)
           ret = configure_port_config(deviceStr="10.115.32.5", portId="1/1/x2", ingressVlanTag=900)
           ret = configure_port_config(deviceStr="10.115.32.5", portId="1/1/x1..1/1/x3", neighborDiscovery="all")
           ret = configure_port_config(deviceStr="10.115.32.5", portId="1/1/x1,1/1/x2,1/1/x3", ingressVlanTag=900)

        '''

        clusterId = ""
        portList = []
        payload = {}

        if "," in portId or ".." in portId:
            portList = self._expand(portId)
        else:
            portList.append(portId) 

        clusterId = self.ns.get_cluster_id ( deviceStr.strip() )

        if clusterId == 'None':
            self.fm.logger.error("Error getting clusterId for {}".format(deviceStr))
            return 1
    
        for portId in portList:

            payload["portId"] = portId

            for k, v in kwargs.items():
                if k:
                    if "alarm" in k:
                        if "alarmThresholds" not in payload.keys():
                            payload["alarmThresholds"] = {}
                        payload["alarmThresholds"][k] = v
                    elif "level" in k:
                        if "accessRoles" not in payload.keys():
                            payload["accessRoles"] = {}
                        payload["accessRoles"][k] = v
                    else:
                        payload[k] = v 

            p_ortId = re.sub("/", "_", portId)

            try:
                params = { 'clusterId' : clusterId }
 
                obj = self.fm.portConfigportConfigsportId(portId=p_ortId).patch(params=params, data=payload)

                if not re.search(r"20(\d)", str(obj.status_code)):
                    self.fm.logger.error("Configure portConfig failed")
                    return 1

            except Exception as e:
                self.fm.logger.error("Configure portConfig failed")
                raise e

        return 0

    def get_unhealthy_ports( self ):

        '''

        Return the list of all ports (with adminStatus as up and operStatus as down) across all managed devices

        Return:
            return_list: List of ports

        '''

        return_list = []

        ms = MapUtils(self.fm, self.ns)

        try:
            params = { 'adminStatus' : 'up', 'operStatus' : 'down' }
 
            obj = self.fm.inventoryportsall().get(params=params)

            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                ports = js['ports'] 
                if len(ports):
                    for port in ports:
                        buf = []
                        clusterId = port['clusterId'].encode('ascii')
                        hostname = port['hostname'].encode('ascii')
                        portId = port['portId'].encode('ascii')
                        portAlias = port.get('alias')
                        portType = port['portType'].encode('ascii')
                        adminStatus = port['adminStatus'].encode('ascii')
                        operStatus = port['operStatus'].encode('ascii')
                        mapList = ms.get_maps_by_port(clusterId, portId)
                        if len(mapList):
                            maps = [m['alias'].encode('ascii') for m in mapList]
                            buf += [hostname, clusterId, portId, portAlias, portType, adminStatus, operStatus, "yes", maps]
                        else:
                            buf += [hostname, clusterId, portId, portAlias, portType, adminStatus, operStatus, "no", "na"]

                        return_list.append(buf)

                    return return_list
                else:
                    return return_list
            else:
                self.fm.logger.error("Unable to perform get inventory ports all API")
                return return_list

        except Exception as e:
            self.fm.logger.error("Exception while calling get inventory ports all API")
            raise e

        return return_list
