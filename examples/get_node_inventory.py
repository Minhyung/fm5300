from fm_rest_api_binding import FmClient
from node_utils import NodeUtils
import os
import sys

#
# Script to fetch device inventory from FM based on one or more filters
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
        
    nodes = []

    #
    # To get all devices managed by FM
    #

    nodes = ns.get_device_inventory()

    #
    # Print all the node details
    #

    print("\nAll devices managed by FM")
    for node in nodes:
        print("IP={}, HOSTNAME={}, CLUSTER_ID={}, MODEL={}, VERSION={}\n".format(node.get("deviceIp"), node.get("hostname"), node.get("clusterId"), node.get("model"), node.get("swVersion")))

    #
    # To get all devices matching a specific model
    #

    print("Get all devices matching a specific model ..")
    nodes = ns.get_device_inventory( devicefilter={'model': 'TA10'} )
    print("Number of devices matching the filter : {}\n".format(len(nodes)))

    #
    # To get all devices matching a specific model and version
    #

    print("Get all devices matching a specific model and version")
    nodes = ns.get_device_inventory( devicefilter={'model': 'TA10', 'swVersion': '5.1.00'} )
    print("Number of devices matching the filter : {}\n".format(len(nodes)))
