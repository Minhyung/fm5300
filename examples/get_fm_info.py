from fm_rest_api_binding import FmClient
from fm_utils import FMUtils
import sys
import time
import os

#
# Script to show the FM version info
#

if __name__ == '__main__':

   if len(sys.argv) != 4:
     print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD>\n")
     sys.exit(1)
   else:
    fmIp = sys.argv[1]
    fmUser = sys.argv[2]
    fmPasswd = sys.argv[3]

    try:
        fm = FmClient(fmIp, fmUser, fmPasswd)

        m = FMUtils(fm)

        fmInfo = m.get_fm_sys_info()

        print("Version={}, Build={}, Uptime={}".format(fmInfo['version'], fmInfo['buildId'], fmInfo['fmUptime']))

    except Exception as e:
        print("Unable to access FM")
        raise e

    sys.exit(0)
