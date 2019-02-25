import sys, glob

sys.path.append('/opt/tc_npath_client/gen-py')
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

from tc_npath_client.src.lib.log import *
from tcnpathmonitor import ServerSvc

import time
log = prepare_log('/opt/tc_npath_client/log/TCRpcWrapper.log')

class TCRpcWrapper():
    def __init__(self,url,port):
        self.transport = TSocket.TSocket(url, port)
        self.transport = TTransport.TFramedTransport(self.transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = ServerSvc.Client(self.protocol)

    def _reconnectOrThrowException(self,maxRetries, retry_interval):
        errors = 0
        self.transport.close()

        while(errors < maxRetries):
            try:
                log.info('Attempting to reconnect')
                self.transport.open()
                log.info('Reconnection success')
                break
            except TTransport.TTransportException as e:
                log.error('Error - Reconnect fail')
                errors += 1

                if errors < maxRetries:
                    try:
                        log.info('Waiting for milliseconds for retrying connect')
                        time.sleep(retry_interval)

                    except Exception as e:
                        print e

        if errors >= maxRetries:
            raise TTransport.TTransportException("Connect failed")


    def connect(self):
        try:
            self.transport.open()
            if not self.transport.isOpen():
                self._reconnectOrThrowException(10,1)
        except:
            self._reconnectOrThrowException(10,1)

    def close(self):
        try:
            if self.transport.isOpen():
                self.transport.close()

        except Exception as e:
            print e

    def ping(self):
        self.client.ping()

    def reportAlive(self, uuid, aliveinfo):
        ret = self.client.reportAlive(uuid,aliveinfo)
        return ret

    def registVm(self,vminfo):
        ret = self.client.registVm(vminfo)
        return ret

if __name__ == '__main__':
    cl = TCRpcWrapper('13.124.122.2',9090)
    cl.connect()
    cl.ping()
    cl.close()
