from fm_rest_api_binding import FmClient
from node_utils import NodeUtils
from port_utils import PortUtils
from map_utils import MapUtils
import sys
import os

#
# Script that identifies number of ports that are not part of map across all devices managed by FM
#

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD>\n")
        sys.exit(1)

    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]

    fm = FmClient(fmIp, fmUser, fmPasswd, screen_out=True)

    ns = NodeUtils(fm)

    ps = PortUtils(fm, ns)

    ms = MapUtils(fm, ns)

    nodeList = ns.get_device_inventory()
   
    flag = 0
    if len(nodeList):
        print("Number of devices: {}".format(len(nodeList)))
        lines=[]
        cluster_free_ports = {}
        for node in nodeList:
            portList=[]
            freePortList=[]
            clusterId = node['clusterId']
            print("clusterId {}".format(clusterId))
            portList = ps.get_ports_by_type(clusterId)
            if len(portList):
                print("Number of ports identified = {}".format(len(portList)))
                for port in portList:
                    mapList = []
                    portId = port['portId'].encode('ascii')
                    mapList = ms.get_maps_by_port(clusterId, portId)
                    if not len(mapList):
                        freePortList.append(port)

                cluster_free_ports[clusterId] = freePortList

            else:
                print("portList empty!")
                flag = 1

    else:
        print("nodeList empty!")
        flag = 1

    for k, v in cluster_free_ports.iteritems():
        print("Cluster: {}, Number of ports not part of map: {}".format(k, len(v)))

    if flag == 0:
        sys.exit(0)
    else:
        sys.exit(1)
