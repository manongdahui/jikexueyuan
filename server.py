#!/usr/bin/python
#coding=utf-8
import sys
from thrift import Thrift
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer
from gconstants import *
sys.path.append(CON_GEN_PY)
from jikexueyuan import RecomService
from jikexueyuan.ttypes import *

class RecomServiceHandler:  
  def getRecomResponse(self,rreq):  
    rres=RecomResponse()
    rres.recom_list=[]
    for i in xrange(rreq.num):
      rres.recom_list.append('test_'+str(i))
    return rres
   
handler = RecomServiceHandler()  
processor = RecomService.Processor(handler)  
transport = TSocket.TServerSocket("localhost", 9090)  
tfactory = TTransport.TBufferedTransportFactory()  
pfactory = TBinaryProtocol.TBinaryProtocolFactory()  
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)  
#server = TServer.TNonblockingServer(processor, transport, tfactory, pfactory)  
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)  
print "Starting thrift server in python..."  
server.serve()  
print "done!"  
