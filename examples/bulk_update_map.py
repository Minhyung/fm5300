from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
from node_utils import NodeUtils
from map_utils import MapUtils
import sys
import os
import csv

#
# Script to bulk update map (passed using a CSV file) using FM
#
# - Can be used to add pass/drop rules to an existing map
#
# - Refer to "MAP_UPDATE.csv.template" for the CSV file format
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
        de_limiter = sys.argv[5]

    fm = FmClient(fmIp, fmUser, fmPasswd)

    ns = NodeUtils(fm)

    ms = MapUtils(fm, ns)

    flag = 0

    # Open the csv file
    with open(csvFile) as fp:

        count = 0
        # read one line at a time
        for line in fp:

            if count == 0:
                count += 1
                continue

            buf = line.rstrip('\n')

            deviceStr = ""
            mapAlias = ""
            ruleId = 0
            ruleElementType = ""
            ruleElementValue = ""

            # assign the line item to variables
            [deviceStr, mapAlias, ruleType, ruleId, ruleElementType, ruleElementValue] = buf.strip(de_limiter).split(de_limiter)

            # get cluster id
            clusterId = ns.get_cluster_id (deviceStr.strip())

            payload = {
                'ruleId': ruleId,
                'bidi': False,
                'matches': [
                     {     
                         'type': ruleElementType,
                         'value': ruleElementValue
                     }   
                ]    
            }

            print("Adding rule {} to map {}".format(payload, mapAlias))

            # add rule to the map
            fm.logger.info("Adding rule to map {}".format(mapAlias))
            if ms.add_map_rule(clusterId, mapAlias, ruleType, payload):
                print("Adding rule to map {}: FAIL".format(mapAlias))
                flag = 1
            else:
                print("Adding rule to map {}: PASS".format(mapAlias))
        
    if flag:
        sys.exit(1)
    else:
        sys.exit(0)
