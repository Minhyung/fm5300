from fm_rest_api_binding import FmClient
from event_utils import EventUtils
import sys
import csv
import os
import datetime

#
# Script that generates a report based on the device traps received by FM (for any given time period)
#

def gen_trap_report(fm, eventList, since):

    cwd = os.getcwd()
    fname = cwd + "/DeviceTrapReport." + since + "." + datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S") + ".csv"

    h_eader = ['DEVICE IP','HOSTNAME','EVENT ID','EVENT TYPE','RESOURCE TYPE', 'RESOURCE ID', 'EVENT DESCRIPTION', 'SEVERITY', 'TIME']

    fp = open(fname, 'w')
   
    fp.write("sep=:" + '\n')
    csvwriter = csv.writer(fp, delimiter=';')
    count = 0
    n_traps = 0

    for event in eventList:
        buf = []
        if count == 0:
          csvwriter.writerow(h_eader)
          count += 1

        if event.get('type').startswith('Trap'):
          n_traps += 1
          buf.append(event.get('deviceIp'))
          buf.append(event.get('hostname'))
          buf.append(event.get('id'))
          buf.append(event.get('type'))
          buf.append(event.get('resourceType'))
          buf.append(event.get('resourceId'))
          buf.append(event.get('description'))
          buf.append(event.get('severity'))
          buf.append(event.get('ts'))
          csvwriter.writerow(buf)

    return n_traps

if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD> <SINCE>")
        print("\n<SINCE> = N-hour (or) N-day (or) all\n")
        sys.exit(1)
    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]
        since = sys.argv[4]

    fm = FmClient(fmIp, fmUser, fmPasswd)

    es = EventUtils(fm)

    if since == "all":
        eventList = es.get_events()
    else:
        eventList = es.get_events(since)

    print("Total number of events found: {}".format(len(eventList)))

    if len(eventList):
        gen_trap_report(fm, eventList, since)

    sys.exit(0)
