from fm_rest_api_binding import FmClient
from node_utils import NodeUtils
from port_utils import PortUtils
import sys
import os
import time

#
# Script that gets ports inventory (from one or more devices) matching one or more types
#

if __name__ == '__main__':
    
    if len(sys.argv) != 5:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD> <DEVICE STR>")
        print("\n<DEVICE STR> : Device ip or hostname\n")
        sys.exit(1)

    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]
        deviceStr = sys.argv[4]

    fm = FmClient(fmIp, fmUser, fmPasswd)

    ns = NodeUtils(fm)

    ps = PortUtils(fm, ns)
        
    #
    # To get port inventory for all devices managed by FM
    #

    cluster_ports = {}

    cluster_ports = ps.get_ports_from_all_devices()

    for k, v in cluster_ports.items():
        print("ClusterID={} Total number of ports={}".format(k, len(v)))

    #
    # To get all ports from a single device
    # 

    ret = ps.get_ports_by_type(deviceStr)
    print("Total number of ports {} on device {}".format(len(ret), deviceStr))

    #
    # To get all tool ports from a single device
    # 
    # deviceStr = device ip or hostname
    #

    ret = ps.get_ports_by_type(deviceStr, port_filter=["tool"])
    print("Number of tool ports {} on device {}".format(len(ret), deviceStr))
    
    #
    # To get all network and tool ports from a single device
    #
    # deviceStr = device ip or hostname
    #

    ret = ps.get_ports_by_type(deviceStr, port_filter=["network", "tool"])
    print("Number of network and tool ports {} on device {}".format(len(ret), deviceStr))
