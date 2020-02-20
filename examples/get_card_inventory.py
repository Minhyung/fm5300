from fm_rest_api_binding import FmClient
from node_utils import NodeUtils
from chassis_utils import ChassisUtils
import sys
import csv
import os

#
# Script that generates a "card inventory" report for all the devices managed by FM
#

def gen_card_inventory_report(fmIp, model, lines):

    cwd = os.getcwd()
    fname = cwd + "/" + fmIp + ".CardInventoryReport." + model + ".csv"

    print("Creating card inventory report file {}".format(fname))

    fp = open(fname, 'w')

    fp.write("sep=:" + '\n')
    csvwriter = csv.writer(fp, delimiter=':')

    h_eader = ['HOSTNAME', 'DEVICE IP', 'CLUSTER ID', 'MODEL', 'CARDS INSTALLED', 'CARD SLOTS AVAILABLE']
    csvwriter.writerow(h_eader)

    count = 0
    for line in lines:
        csvwriter.writerow(line)

    return

def get_card_slots_available(cards, model):
 
    card_slots_available = 0

    if "HD" in model:
        n_cc = len([card for card in cards if "cc" in card])
        if model == "HD8":
            card_slots_available = 8 - (len(cards) - n_cc)
        elif model == "HD4":
            card_slots_available = 4 - (len(cards) - n_cc)

    elif "HC" in model:
        card_slots_available = 4 - (len(cards) - 1)

    return card_slots_available

if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("\nUsage: " + sys.argv[0] + " <FM IP> <FM USER> <FM PASSWORD> <DEVICE MODEL>")
        print("\n   <DEVICE MODEL> : ALL (or) HD8 (or) HC3 (or) HC2\n")
        sys.exit(1)
    else:
        fmIp = sys.argv[1]
        fmUser = sys.argv[2]
        fmPasswd = sys.argv[3]
        model = sys.argv[4]

    fm = FmClient(fmIp, fmUser, fmPasswd)

    ns = NodeUtils(fm)

    cs = ChassisUtils(fm)

    #
    # Identify all HD8 devices
    #

    if model == "ALL":
        nodeList = ns.get_device_inventory()
    else:
        nodeList = ns.get_device_inventory( devicefilter={'model': model} )
   
    print("Number of nodes: {}".format(len(nodeList)))

    if len(nodeList):
        print("FM IP: {}".format(fmIp))
        print("Model: {}".format(model))
        print("Number of devices: {}".format(len(nodeList)))
        lines=[]
        for node in nodeList:
            buf=[]
            nodeId = node['deviceIp']
            clusterMode = node['clusterMode']
            print("nodeId: {}".format(nodeId))
            cardList = []
            if clusterMode == "Standalone":
                cardList = cs.get_chassis_card_inventory(nodeId=nodeId)
                if len(cardList):
                    slots = [card['slotId'].encode('ascii') for card in cardList]
                    slots_free = get_card_slots_available(slots, node.get('model').encode('ascii'))
                    buf += [node.get('hostname').encode('ascii'), node.get('deviceIp').encode('ascii'), node.get('clusterId').encode('ascii'), node.get('model').encode('ascii'), str(slots), slots_free]
                    lines.append(buf)
                else:
                    print("cardList empty!") 

            else:
                chassisList = cs.get_chassis_inventory(nodeId=nodeId)
                for chassis in chassisList:
                    if node.get('hostname') == chassis.get('deviceName'):
                        cardList = chassis.get('cards')
                        break

                if len(cardList):
                    slots = [card['slotId'].encode('ascii') for card in cardList]
                    slots_free = get_card_slots_available(slots, node.get('model').encode('ascii'))
                    buf += [node.get('hostname').encode('ascii'), node.get('deviceIp').encode('ascii'), node.get('clusterId').encode('ascii'), node.get('model').encode('ascii'), str(slots), slots_free]
                    lines.append(buf)
                else:
                    print("cardList empty!") 

        gen_card_inventory_report(fmIp, model, lines)

    else:
        print("nodeList empty!") 

    sys.exit(0)
