import json
import urllib2
from mposextractor import mposextractor as Poolmaster
str = unicode
from requests import get as _get
request = Poolmaster('https://etn.suprnova.cc','ae36b05aae2e4447c7cd1c320fe42f6c8b48df2832a11f0627584fda157e9c49')


john = request.getpoolinfo()
print john
print type(john)