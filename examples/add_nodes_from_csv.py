from fm_rest_api_binding import FmClient
from node_utils import NodeUtils
import sys
import os

#
# Script to bulk add devices (passed using a CSV file) to FM
#
# - Refer to "Nodes.csv.template" for the CSV file format
#

if __name__ == '__main__':

    if len(sys.argv) != 6:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD> <CSV FILE> <DELIMITER>\n")
        sys.exit(1)
    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]
        csvFile = sys.argv[4]
        delimiter = sys.argv[5]

    fm = FmClient(fmIp, fmUser, fmPasswd)

    ns = NodeUtils(fm)

    if ns.add_nodes_from_file(csvFile, delimiter):
        print("Adding nodes to FM: FAIL")
    else:
        print("Adding nodes to FM: PASS")

    sys.exit(0)
