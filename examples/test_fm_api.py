from fm_rest_api_binding import FmClient
import sys
import time
import os

#
# Script to test if FM API SDK is setup correctly
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

        time.sleep(1)

        print("Test Success!")

    except Exception as e:
        print("Unable to access FM")
        raise e

    sys.exit(0)
