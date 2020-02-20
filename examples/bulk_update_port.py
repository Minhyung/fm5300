from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
from node_utils import NodeUtils
from port_utils import PortUtils
import sys
import os

#
# Script for performing bulk port updates
#
# - Identifying all TA10s and enable neighborDiscovery across all network ports
#

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD>\n")
        sys.exit(1)
    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]

    fm = FmClient(fmIp, fmUser, fmPasswd)

    ns = NodeUtils(fm)

    #
    # Identify devices of specific type
    #
    nodeList = ns.get_device_inventory( devicefilter={'model': 'TA10'} )

    flag = 0
    if len(nodeList):
        print("Number of device identified = {}".format(len(nodeList)))
        for node in nodeList:
            clusterId = node['clusterId']
            portList = []
            ps = PortUtils(fm, ns)

            #
            # For each TA device, identify all network ports and enable neighbor discovery
            #
            portList = ps.get_ports_by_type(clusterId, port_filter=["network"])
            if len(portList):
                print("Number of ports identified = {}".format(len(portList)))
                print("Configuring neightborDiscovery to all")
                for port in portList:
                    ret = ps.configure_port_config(clusterId, port['portId'], neighborDiscovery="all")
                    if ret:
                        flag = 1

            else:
                print("Unable to find any matching ports for device: {}".format(clusterId))
                flag = 1

    else:
        print("Unable to find any matching device")
        flag = 1

    if flag:
        print("Bulk config update failed")
        sys.exit(1)
    else:
        print("Bulk config update successful")
        sys.exit(0)
