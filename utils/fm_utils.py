from fm_rest_api_binding import FmClient
from tapioca.exceptions import TapiocaException
import json
import re

class FMUtils(object):

    """

    FMUtils class provides custom methods to perform various FM functionalities

    """

    def __init__(self, fm):
        self.fm = fm

    def get_fm_version( self ):

        """

        Get FM Version

        Return:

            fmVersion: FM Version

        """

        try:
            obj = self.fm.sysinfo().get()

            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                fmVersion = js['version'].encode('ascii')
                return fmVersion

            else:
                self.fm.logger.error("get fm version failed")
                return []

        except Exception as e:
            self.fm.logger.error("exception while get fm version")
            raise e

    def get_fm_sys_info( self ):

        """

        Get FM system information like hostname, mac, version, build, uptime ..etc

        Return:

            fmSysInfo: Dictionary with all FM system info

        """

        try:
            obj = self.fm.sysinfo().get()

            if re.search(r"20(\d)", str(obj.status_code)):
                js = obj.content
                return js
            else:
                self.fm.logger.error("get sys info failed")
                return []

        except Exception as e:
            self.fm.logger.error("exception while get sys info")
            raise e
