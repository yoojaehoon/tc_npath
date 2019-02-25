from tc_npath_client.src.lib import config
from tc_npath_client.src.lib.daemon import *
from tc_npath_client.src.TnpathMonServices import TnPathMonServices
import time

from tcnpathmonitor import ServerSvc
from tcnpathmonitor.ttypes import *
from tc_npath_client.src.lib.log import *

log = prepare_log('/opt/tc_npath_client/log/TCRpcWrapper.log')
daemon_cfg = config.getDaemonConf()

#daemonize()

try:
    while 1:
        tncl = TnPathMonServices(daemon_cfg['server_url'],daemon_cfg['server_port'])
        while 1:
            try:
                tncl.connect()
                tncl.ping()
                ret = tncl.reportAlive()
                if ret.rcode == RETURN_CODE.RC_SERVER_NOT_FOUND:
                    tncl.registVm()
                    tncl.reportAlive()
                tncl.close()
                time.sleep(daemon_cfg['interval'])
            except Exception as e:
                #log.error('Error reason [ %s ]' %(e.message))
		print str(e)
                tncl.close()
                break

        time.sleep(daemon_cfg['interval'])

except Exception as e:
    log.error('Daemon Error reason [ %s ]' %(e.message))
    print "Daemon Halted"
