from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
import re
import json
import time
import datetime

class EventUtils(object):

    '''

    EventUtils class provides custom methods to perform various "Alarm/Events" related operations

    '''

    def __init__( self, fm ):
        self.fm = fm

    def get_events( self, since=None ):

        '''

        Collect and return device traps for a given time range

        Parameters:
            since: N-hour (or) N-day

        Return:
            List of faults : For success
            Empty List : For failure

        '''

        event_list = []

        try:
            if not since:
                obj = self.fm.events().get()
            else:
                s1 = int(since.split('-')[0])
                s2 = since.split('-')[1]
 
                start_time = ""
                if "hour" in s2.lower():
                    t = datetime.datetime.now() - datetime.timedelta(hours=s1)
                    start_time = t.strftime("%Y-%m-%dT%H:%M:%S")
                elif "day" in s2.lower():
                    t = datetime.datetime.now() - datetime.timedelta(days=s1)
                    start_time = t.strftime("%Y-%m-%dT%H:%M:%S")

                params = { 'startTime' : start_time }

                obj = self.fm.events().get(params=params)

            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                event_list = js['events']
                return event_list
            else:
                self.fm.logger.error("Unable to get events")
                return []

        except Exception as e:
            self.fm.logger.error("Get events failed")
            raise e

        return []
