from urllib import urlencode as _urlencode
str = unicode
import logging
# 3rd party
from requests import get as _get

logger = logging.getLogger(__name__)
#Commands public
PUBLIC_COMMANDS = [
    'public',]

PRIVATE_COMMANDS = [
    'getblockcount',
    'getblocksfound',
    'getblockstats',
    'getcurrentworkers',
    'getdashboarddata',
    'getdifficulty',
    'getestimatedtime',
    'gethourlyhashrates',
    'getnavbardata',
    'getpoolhashrate',
    'getpoolinfo',
    'getpoolsharerate',
    'getpoolstatus',
    'gettimesincelastblock',
    'gettopcontributers',
    'getuserbalance',
    'getusersharerate',
    'getuserhashrate',
    'getuserstatus',
    'getuserworker']

class mposextractorError(Exception):
    pass

class mposextractor(object):
    def __init__(self, url=False, key=False, timeout= 1):
        self.url = url
        self.key = key
        self.timeout = timeout


    def __call__(self, command, args={},api={}):
        global PUBLIC_COMMANDS, PRIVATE_COMMANDS
        args['action'] = command
        '/index.php?page=api'
        api['api_key'] = self.key
        if command in PRIVATE_COMMANDS:
            if not self.url or not self.key:
                    raise mposextractorError("url and an api key is required for this command!")

            ret = _get(self.url + '/index.php?page=api&' +_urlencode(args)+"&"+_urlencode(api))
            return ret.text

        elif command in PUBLIC_COMMANDS:
            ret = _get('https://etn.suprnova.cc/index.php?page=api&' + _urlencode(args))
            return ret.text
        else:
            raise mposextractorError("Invalid Command!")

#-----------------------------------------|public commands|------------------------------------#
    def public(self):
        """ Fetch public pool statistics, no authentication required	"""
        return self.__call__('public')
#-----------------------------------------|private commands|------------------------------------#
    def getpoolinfo(self):
        """Get the information on pool settings	"""
        return self.__call__('getpoolinfo')
    def getuserworkers(self):
        """Fetch a users worker status, both id and username work for id. If not admin, will fetch current users workers.	"""
        return self.__call__('getuserworkers')
    def getpoolhashrate(self):
        """Get current pool hashrate	"""
        return self.__call__('getpoolhashrate')
    def getpoolsharerate(self):
        """Get current pool share rate (shares/s)	"""
        return self.__call__('getpoolsharerate')
    def getpoolstatus(self):
        """Fetch overall pool status, only user token is required	"""
        return self.__call__('getpoolstatus')
    def gettimesincelastblock(self):
        """Get time since last block found (seconds)	"""
        return self.__call__('gettimesincelastblock')
    def gettopcontributors(self):
        """Fetch top contributors data	"""
        return self.__call__('gettopcontributors')
    def getuserbalance(self):
        """Fetch a users balance	"""
        return self.__call__('getuserbalance')
    def getuserhashrate(self):
        """Fetch a users hash rate	"""
        return self.__call__('getuserhashrate')
    def getusersharerate(self):
        """Fetch a users share rate	"""
        return self.__call__('getusersharerate')
    def getuserstatus(self):
        """Fetch a users overall status, both id and username work for id. If not admin, will fetch current users status.	"""
        return self.__call__('getuserstatus')
    def getusertransactions(self):
        """Get a users transactions	"""
        return self.__call__('getusertransactions')
    def getnavbardata(self):
        """Get the data displayed on the navbar	"""
        return self.__call__('getnavbardata')
    def gethourlyhashrates(self):
        """Currently broken	"""
        return self.__call__('gethourlyhashrates')
    def getestimatedtime(self):
        """Get estimated time to next block based on pool hashrate (seconds)	"""
        return self.__call__('getestimatedtime')
    def getdifficulty(self):
        """Get current difficulty in blockchain	"""
        return self.__call__('getdifficulty')
    def getdashboarddata(self):
        """Fetch all dashboard related information	"""
        return self.__call__('getdashboarddata')
    def getcurrentworkers(self):
        """Get amount of current active workers	"""
        return self.__call__('getcurrentworkers')
    def getblockstats(self):
        """Get pool block stats	"""
        return self.__call__('getblockstats')
    def getblocksfound(self):
        """Get last N blocks found as configured in admin panel	"""
        return self.__call__('getblocksfound')
    def getblockcount(self):
        """Get current block height in blockchain"""
        return self.__call__('getblockcount')