import mysql.connector
import time
import datetime
from mposextractor import mposextractor as Poolmaster
from operator import itemgetter
rowdict = {}
gcloud = mysql.connector.connect(user='root', password='mindfreak', host='35.202.15.174',database='Pools')
dbcurser=gcloud.cursor()
request = Poolmaster('https://etn.suprnova.cc','ae36b05aae2e4447c7cd1c320fe42f6c8b48df2832a11f0627584fda157e9c49')
query = ("SELECT * FROM Users ")
dbcurser.execute(query)
row = dbcurser.fetchall()
now = time.strftime('%Y-%m-%d %H:%M' )
print now
#queires db for pool and api keys by user#
for x in row:
    query = ("SELECT poolid, poolurl, poolapi FROM pools WHERE UserID =" + str(x[0]))
    dbcurser.execute(query)
    pools = dbcurser.fetchall()
    for y in pools: #for each pool get in users#
        request = Poolmaster(y[1],y[2])
        workers = request.getuserworkers()
        worker = workers['getuserworkers']
        machine = worker['data']
        print""
        print x[0]
        uid = x[0]
        print y[0]
        poolid = y[0]
        for rig in machine:#for each seperate machine in pool for the user#
            print rig["username"]
            username = rig["username"]
            monitor = rig["monitor"]
            shares = rig["shares"]
            hashrate = rig["hashrate"]
            difficulty = rig["difficulty"]
            query = ("""UPDATE IGNORE workers SET
             username = '%s',monitor = %s,shares = %s,hashrate = %s,difficulty = %s,uid =%s,poolid =%s, DT = '%s'
             """) \
                    % (username, monitor, shares, hashrate, difficulty, uid, poolid, now)
            print query
            dbcurser.execute(query)

            gcloud.commit()
