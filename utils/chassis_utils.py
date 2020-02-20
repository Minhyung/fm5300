from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
from node_utils import NodeUtils
import json
import re
import time

class ChassisUtils(object):

    """

    ChassisUtils class provides custom methods to perform various chassis related operations (for both standalone and clusters)       

    """

    def __init__(self, fm):
        self.fm = fm

    def get_chassis_inventory( self, clusterId=None, nodeId=None ):

        """

        Get chassis inventory for a given cluster or device

        Parameters:
            clusterId: cluster id
            nodeId: node id

        Return:
            chassisList: Chassis inventory for the matching cluster or node

        """

        if not clusterId and not nodeId:
            self.fm.logger.error("Require clusterId or nodeId as a parameter")
            return 1
        elif clusterId and not nodeId:
            params = { 'clusterId' : clusterId }
        elif nodeId and not clusterId:
            params = { 'nodeId' : nodeId }

        try:
            obj = self.fm.inventorychassis().get(params=params)

            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                return js.get('chassisList')
            else:
                self.fm.logger.error("get inventory chassis failed")
                return []

        except Exception as e:
            self.fm.logger.error("exception while get chassis inventory")
            raise e

    def get_chassis_card_inventory( self, clusterId=None, nodeId=None ):

        """

        Get chassis inventory for a given cluster or device

        Parameters:
            clusterId: cluster id
            nodeId: node id

        Return:
            cardList: Chassis card inventory for the matching cluster or node

        """

        if not clusterId and not nodeId:
            self.fm.logger.error("Require clusterId or nodeId as a parameter")
            return 1
        elif clusterId and not nodeId:
            params = { 'clusterId' : clusterId }
        elif nodeId and not clusterId:
            params = { 'nodeId' : nodeId }

        try:
            obj = self.fm.inventorychassiscards().get(params=params)

            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                return js.get('cards')
            else:
                self.fm.logger.error("get inventory chassis cards failed")
                return []

        except Exception as e:
            self.fm.logger.error("exception while get chassis inventory cards")
            raise e

    def configure_chassis( self, deviceIp, **kwargs ):

        '''

        Configure chassis parameters for a given given device

        Parameters:
            deviceStr: device ip
            **kwargs: configure parameters such as boxId, mode, serialNumber, chassisType or gdp

        Return:
            0 : For success
            1 : For failure

        Example:

           ret = configure_chassis(deviceStr="10.115.32.5", gdp=true)

        '''

        c = self.get_chassis_inventory(nodeId=deviceIp)

        payload = {}

        if len(c):
            payload['boxId'] = c[0].get('boxId')
        else:
            return 1
    
        for k, v in kwargs.items():
            payload[k] = v

        try:
            params = { 'nodeId' : deviceIp }

            obj = self.fm.inventorychassisconfigure().patch(params=params, data=payload)

            if not re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.error("Configure chassis failed")
                return 1

        except Exception as e:
            self.fm.logger.error("Exception while configuring chassis: {}".format(str(e)))
            return 1

        return 0

    def get_card_info( self, nodeId, cardSlot ):

        '''

        Get card info a given device / cluster

        Parameters:
            nodeId: device ip
            cardSlot: card slot ID

        Return:
            card info (dict): For success
            {} : For failure

        Example:

           ret = get_card_info("10.115.32.5", "1/5")

        '''

        try:
            params = { "nodeId" : nodeId }

            s_lot = re.sub("/", "_", cardSlot)

            obj = self.fm.inventorychassiscardsslotId(slotId=s_lot).get(params=params)

            if not re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.error("Get card info failed ..")
                return {}

            else:
                js = obj.content
                if js:
                    return js.get('card')
                else:
                    return {}

        except Exception as e:
            self.fm.logger.error("Exception while getting card info {}".format(str(e)))
            return {}

    def unconfigure_card( self, nodeId, cardSlot ):

        '''

        Unconfigure card for a given device / cluster

        Parameters:
            nodeId: device ip
            cardSlot: card slot ID

        Return:
            0 : For success
            1 : For failure

        Example:

           ret = unconfigure_card("10.115.32.5", "1/5")

        '''
    
        try:
            params = { "nodeId" : nodeId }

            s_lot = re.sub("/", "_", cardSlot)

            obj = self.fm.inventorychassiscardsslotIdconfigure(slotId=s_lot).delete(params=params)

            if not re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.error("Unconfigure card failed ..")
                return 1
            else:
                time.sleep(10)

        except Exception as e:
            self.fm.logger.error("Exception while Unconfiguring card: {}".format(str(e)))
            return 1

    def configure_card( self, nodeId, cardSlot ):

        '''

        Configure card for a given device / cluster

        Parameters:
            nodeId: device ip
            cardSlot: card slot ID

        Return:
            0 : For success
            1 : For failure

        Example:

           ret = configure_card("10.115.32.5", "1/5")

        '''
    
        try:
            params = { "nodeId" : nodeId }

            s_lot = re.sub("/", "_", cardSlot)

            obj = self.fm.inventorychassiscardsslotIdconfigure(slotId=s_lot).post(params=params)

            if not re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.error("configure card failed ..")
                return 1
            else:
                time.sleep(10)

        except Exception as e:
            self.fm.logger.error("Exception while configuring card: {}".format(str(e)))
            return 1

        return 0

    def shutdown_card( self, nodeId, cardSlot ):

        '''

        Shutdown card for a given device / cluster

        Parameters:
            nodeId: device ip
            cardSlot: card slot ID

        Return:
            0 : For success
            1 : For failure

        Example:

           ret = shutdown_card("10.115.32.5", "1/5")

        '''
 
        self.fm.logger.info("Shutdown card {} on node {}".format(cardSlot, nodeId))
        print("Shutdown card {} on node {}".format(cardSlot, nodeId))

        try:
            params = { "nodeId" : nodeId }

            s_lot = re.sub("/", "_", cardSlot)

            payload = { "slotId": cardSlot, "adminStatus": "down" }

            obj = self.fm.inventorychassiscardsslotId(slotId=s_lot).patch(params=params, data=payload)

            if not re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.error("Shutdown card failed ..")
                return 1
            else:
                self.fm.rediscover_nodes(nodeId)

        except Exception as e:
            self.fm.logger.error("Exception while shutting down card: {}".format(str(e)))
            return 1

        #
        # Check if card is in 'shutdown' state before starting it
        #

        time.sleep(60)

        c_flag = 0
        for x in xrange(3):
            c = self.get_card_info(nodeId, cardSlot)
            self.fm.logger.info("Verifying if card is shutdown, operStatus={}".format(c.get('operStatus')))
            print("Verifying if card is shutdown, operStatus={}".format(c.get('operStatus')))
            if c.get('operStatus') == 'shutdown':
                c_flag = 1
                break
            else:
                time.sleep(60)

        if c_flag == 0:
            self.fm.logger.error("Card {} not in shutdown state".format(cardSlot))
            print("Card {} not in shutdown state".format(cardSlot))
            return 1

        return 0

    def restart_card( self, nodeId, cardSlot ):

        '''

        Restart card for a given device / cluster

        Parameters:
            nodeId: device ip
            cardSlot: card slot ID

        Return:
            0 : For success
            1 : For failure

        Example:

           ret = no_shutdown_card("10.115.32.5", "1/5")

        '''
 
        self.fm.logger.info("Restart card {} on node {}".format(cardSlot, nodeId))
        print("Restart card {} on node {}".format(cardSlot, nodeId))

        try:
            params = { "nodeId" : nodeId }

            s_lot = re.sub("/", "_", cardSlot)

            payload = { "slotId": cardSlot, "adminStatus": "up" }

            time.sleep(10)
            obj = self.fm.inventorychassiscardsslotId(slotId=s_lot).patch(params=params, data=payload)

            if not re.search(r"20(\d)", str(obj.status_code)):
                self.fm.logger.error("Start card failed ..")
                return 1
            else:
                self.fm.rediscover_nodes(nodeId)

        except Exception as e:
            self.fm.logger.error("Exception while no shutdown card: {}".format(str(e)))
            return 1

        #
        # Check if card is in 'up' state after starting it
        #

        self.fm.logger.info("Waiting for card to come up ...")
        print("Waiting for card to come up ...")
        time.sleep(120)

        c_flag = 0
        for x in xrange(2):
            c = self.get_card_info(nodeId, cardSlot)
            self.fm.logger.info("Verifying if card is up, operStatus={}".format(c.get('operStatus')))
            print("Verifying if card is up, operStatus={}".format(c.get('operStatus')))
            if c.get('operStatus') == 'up':
                c_flag = 1
                break
            else:
                time.sleep(120)

        if c_flag == 0:
            self.fm.logger.error("Card {} not in up state".format(cardSlot))
            print("Card {} not in up state".format(cardSlot))
            return 1

        return 0

    def reload_card( self, nodeId, cardSlot ):

        '''

        Reload card for a given device / cluster

        Parameters:
            nodeId: device ip
            cardSlot: card slot ID

        Return:
            0 : For success
            1 : For failure

        Example:

           ret = reload_card("10.115.32.5", "1/5")

        '''
    
        if self.shutdown_card(nodeId, cardSlot):
            return 1

        if self.restart_card(nodeId, cardSlot):
            return 1

        return 0
