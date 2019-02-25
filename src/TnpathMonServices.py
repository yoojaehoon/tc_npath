import sys, glob, os
sys.path.append('/opt/tc_npath_client/gen-py')

from tcnpathmonitor import ServerSvc
from tcnpathmonitor.ttypes import *

from tc_npath_client.src.lib.TCRpcWrapper import TCRpcWrapper
from tc_npath_client.src.lib.restclient import *
from tc_npath_client.src.lib import config
from tc_npath_client.src.lib import utils

from pinger import Pinger

from influxdb import InfluxDBClient

DB_URL="http://103.218.158.169:8086/write?db=tc_watcher"

INFLUXDB_URL="103.218.158.169"
INFLUXDB_PORT=8086
INFLUXDB_ID='root'
INFLUXDB_PW='root'
INFLUXDB_DB='tc_watcher'

class TnPathMonServices():
    def __init__(self,url,port):
	self.influxdb_client = InfluxDBClient(INFLUXDB_URL,INFLUXDB_PORT,INFLUXDB_ID,INFLUXDB_PW,INFLUXDB_DB)
        self.tcrpc = TCRpcWrapper(url,port)
        self.api_conf = config.getApiConf()
        url = self.api_conf['meta_url']
        self.data = getData(url)

    def connect(self):
        self.tcrpc.connect()

    def close(self):
        self.tcrpc.close()

    def ping(self):
        self.tcrpc.ping()

    def reportAlive(self):
        aliveinfo = AliveInfo()

        ping = Pinger()
        hosts = []
        hosts.append(self.api_conf['public_router'])
        hosts.append(self.api_conf['public_gateway'])
        ex_hosts=[]
        ex_hosts.append(self.api_conf['aws'])
        ex_hosts.append(self.api_conf['kt'])
        ex_hosts.append(self.api_conf['legacy'])
        ping.hosts = hosts
        status = ping.start()
        status2 = ping.start()

        if self.api_conf['public_router'] in status['alive'] or self.api_conf['public_router'] in status2['alive']:
            aliveinfo.normal_public_fx = True
            aliveinfo.normal_public_fx_latency = status['alive'][self.api_conf['public_router']]
        else:
            aliveinfo.normal_public_fx = False
            aliveinfo.normal_public_fx_latency = status['dead'][self.api_conf['public_router']]


        if self.api_conf['public_gateway'] in status['alive'] or self.api_conf['public_gateway'] in status2['alive']:
            aliveinfo.normal_public_fl = True
            aliveinfo.normal_public_fl_latency = status['alive'][self.api_conf['public_gateway']]
        else:
            ping.hosts = ex_hosts
            ex_status = ping.start()
            if len(ex_status['alive']) > 0:
                aliveinfo.normal_public_fl = True
                if ex_status['alive'].has_key(self.api_conf['aws']):
                    aliveinfo.normal_public_fl_latency = ex_status['alive'][self.api_conf['aws']]
                elif ex_status['alive'].has_key(self.api_conf['kt']):
                    aliveinfo.normal_public_fl_latency = ex_status['alive'][self.api_conf['kt']]
                elif ex_status['alive'].has_key(self.api_conf['legacy']):
                    aliveinfo.normal_public_fl_latency = ex_status['alive'][self.api_conf['legacy']]
                else:
                    aliveinfo.normal_public_fl_latency = -1
            else:
                aliveinfo.normal_public_fl = False
                aliveinfo.normal_public_fl_latency = ex_status['dead'][self.api_conf['aws']]


        aliveinfo.wmi_private_fx = None
        aliveinfo.wmi_private_fl = None
        aliveinfo.wmi_public_fx = None
        aliveinfo.wmi_public_fl = None

        #influx_container = "tc_npath_monitor,host=%s normal_public_fx=%d,normal_public_fl=%d,normal_public_fx_latency=%.4f,normal_public_fl_latency=%.4f" %(self.data['name'], aliveinfo.normal_public_fx,
																						#aliveinfo.normal_public_fl,
																						#aliveinfo.normal_public_fx_latency,
																						#aliveinfo.normal_public_fl_latency)

        metric = "normal_npath"
        json_body = [
          {
            "measurement": metric,
            "tags": {
              "host": self.data['name'],
            },
            "fields": {
              "normal_public_fx": aliveinfo.normal_public_fx,
              "normal_public_fl": aliveinfo.normal_public_fl,
              "normal_public_fx_latency": round(aliveinfo.normal_public_fx_latency,3),
              "normal_public_fl_latency": round(aliveinfo.normal_public_fl_latency,3)
            }
          }
        ]
        self.influxdb_client.write_points(json_body)
        #print influx_container
        #headers = { "Content-Type" : "text/plain"}
        #headers = {}
        #postData(DB_URL,influx_container,headers)

        ret = self.tcrpc.reportAlive(self.data['uuid'], aliveinfo)

        return ret


    def registVm(self):
        vminfo = VmInfo()
        vminfo.hostname = self.data['name']
        vminfo.uuid = self.data['uuid']
        vminfo.availability_zone = self.data['availability_zone']
        vminfo.project_type = self.data['meta']['project_domain']
        nics = utils.listInterfaces()
        for nic in nics:
            if nic[0] == 'eth0':
                vminfo.nic1 = nic[1]
            elif nic[0] == 'eth1':
                vminfo.nic2 = nic[1]

        ret = self.tcrpc.registVm(vminfo)
        return ret

        

        
            
if __name__ == '__main__':
    #cl = TnPathMonServices('10.161.211.223',9090)
    cl = TnPathMonServices('13.124.122.2',9090)
    ret = cl.reportAlive()
