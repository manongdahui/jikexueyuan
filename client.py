#!/usr/bin/python
#coding=utf-8
import sys
from thrift import Thrift  
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol
from gconstants import *
sys.path.append(CON_GEN_PY)
from jikexueyuan import RecomService
from jikexueyuan.ttypes import *
try:
  transport = TSocket.TSocket('localhost', 9090)  
  transport = TTransport.TBufferedTransport(transport)  
  protocol = TBinaryProtocol.TBinaryProtocol(transport)  
  client = RecomService.Client(protocol)  
  transport.open()
  rreq = RecomRequest()
  rreq.userid = 'liyongbao'
  rreq.his_list = ['v1','v2']
  rreq.num=10
  print rreq
  try:
    rres = client.getRecomResponse(rreq)  
    print rres
  except Exception, e:  
    print '%r' % e  
  transport.close()  
except Thrift.TException, tx:  
    print '%s' % (tx.message)
