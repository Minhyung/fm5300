from fm_rest_api_binding import FmClient
from node_utils import NodeUtils
from port_utils import PortUtils
import sys
import os
import time

#
# Script that demonstrates bulk update of port properties for a given device
#

if __name__ == '__main__':
    
    if len(sys.argv) != 5:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD> <DEVICE STR>")
        print("\n<DEVICE STR> : Device IP or hostname\n")
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
    # To configure a set of ports to 'tool'
    # 
    # deviceStr = device ip or hostname
    #

    print("Configuring ports 1/1/x1, 1/1/x3, 1/1/x5, 1/1/x7 as tool ports on device {}".format(deviceStr))

    ret = ps.configure_ports(deviceStr, "1/1/x1,1/1/x3,1/1/x5,1/1/x7", portType="tool")

    if ret:
       print("configuring port as tool: FAIL")
    else:
       print("configuring port as tool: PASS")

    #
    # To admin enable a range of ports
    # 
    # deviceStr = device ip or hostname
    #

    print("Admin enabling ports 1/1/x8..1/1/x12 on device {}".format(deviceStr))

    ret = ps.configure_ports(deviceStr, "1/1/x8..1/1/x12", adminStatus="up")

    if ret:
       print("admin enable ports: FAIL")
    else:
       print("admin enable ports: PASS")

    #
    # To enable neighbor discovery and alarm thresholds for a range of ports
    # 
    # deviceStr = device ip or hostname
    #

    print("Configuring neighborDiscovery, alarmThreshold for ports 1/1/x8..1/1/x12 on device {}".format(deviceStr))

    ret = ps.configure_port_config(deviceStr, "1/1/x8..1/1/x12", neighborDiscovery="all", alarmThreshold=95, alarmThresholdLow=30)

    if ret:
       print("configuring neighbor discovery and alarm threshold: FAIL")
    else:
       print("configuring neighbor discovery and alarm threshold: PASS")
