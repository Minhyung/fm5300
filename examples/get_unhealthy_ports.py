from fm_rest_api_binding import FmClient
from port_utils import PortUtils
from node_utils import NodeUtils
import sys
import os
import csv

#
# Script that generates a report for all the unhealthy ports across all devices managed by FM
#
# - Unhealthy ports referred here ports that are "admin enabled" but "link down" and part of map(s)
#

def gen_report(fm, lines):

    cwd = os.getcwd()
    fname = cwd + "/" + fmIp + ".UnhealthyPortsReport.csv"

    print("Creating unhealthy ports report file {}".format(fname))

    fp = open(fname, 'w')
    
    fp.write("sep=:" + '\n')
    csvwriter = csv.writer(fp, delimiter=':')
    
    h_eader = ['HOSTNAME', 'CLUSTER ID', 'PORT ID', 'PORT ALIAS', 'PORT TYPE', 'ADMIN STATUS', 'OPER STATUS', 'PART OF MAP', 'MAP ALIAS(s)']
    csvwriter.writerow(h_eader)
    
    count = 0 
    for line in lines:
        csvwriter.writerow(line)
          
    return

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

    ps = PortUtils(fm, ns)

    portList = []

    portList = ps.get_unhealthy_ports()

    print("Number of unhealthy ports: {}".format(len(portList)))

    if len(portList):
        gen_report(fmIp, portList)

    sys.exit(0)
