from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
from node_utils import NodeUtils
from port_utils import PortUtils
from map_utils import MapUtils
import sys
import os

#
# Script for creating a map
#

if __name__ == '__main__':

    if len(sys.argv) != 7:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD> <DEVICE STR> <NETWORK PORT> <TOOL PORT>\n")
        sys.exit(1)
    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]
        deviceStr = sys.argv[4]
        networkPort = sys.argv[5]
        toolPort = sys.argv[6]

    fm = FmClient(fmIp, fmUser, fmPasswd)

    ns = NodeUtils(fm)

    ps = PortUtils(fm, ns)

    ms = MapUtils(fm, ns)

    #
    # Configure network and tool ports
    #

    ret = ps.configure_ports(deviceStr, networkPort, portType="network")

    if ret: 
       print("configuring port as network: FAIL")
    else:
       print("configuring port as network: PASS")

    ret = ps.configure_ports(deviceStr, toolPort, portType="tool")

    if ret: 
       print("configuring port as tool: FAIL")
    else:
       print("configuring port as tool: PASS")

    #
    # Create map
    #

    print("Creating map with alias: testMap")

    payload = {
        'alias': 'testMap',
        'subType': 'byRule',
        'srcPorts': [networkPort],
        'type': 'regular',
        'dstPorts': [toolPort],
        'rules': {
            'dropRules': [],
            'passRules': [{
                'comment': '',
                'bidi': False,
                'matches': [{ 
                    'type': 'ipVer',
                    'value': 'v4'
                }],
                'ruleId': 1
            }]
         } 
    }

    ret = ms.create_map(deviceStr, payload)

    if ret:
        print("Create map: FAIL")
    else:
        print("Create map: PASS")

    sys.exit(0)
