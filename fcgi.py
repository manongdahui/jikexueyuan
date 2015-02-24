#!/usr/bin/python
#coding=utf-8
import flup.server.fcgi as flups  
import urlparse,sys,json
from thrift import Thrift  
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol
from gconstants import *
sys.path.append(CON_GEN_PY)
from jikexueyuan import RecomService
from jikexueyuan.ttypes import *

#client=None
#transport=None
def init():
  try:
    transport = TSocket.TSocket('localhost', 9090)  
    transport = TTransport.TBufferedTransport(transport)  
    protocol = TBinaryProtocol.TBinaryProtocol(transport)  
    client = RecomService.Client(protocol)  
    transport.open()
  except Exception, e:  
    print '%r' % e 
  print client 
  
def application(environ, start_response):
  ret = "TEST\n" 
  ret+=environ['REQUEST_METHOD']+"\n"
  status = '200 OK'
  response_headers = [('Content-type','text/plain')]  
  start_response(status, response_headers)  
  arg_dict=urlparse.parse_qs(environ['QUERY_STRING'])
  rreq = RecomRequest()
  rreq.userid = arg_dict.get('userid',['unknow'])[0]
  rreq.his_list = arg_dict.get('history',[''])[0].split('-')
  rreq.num = int(arg_dict.get('num',[10])[0])
  rres = client.getRecomResponse(rreq)
  print rres
  return [ret]
      
if __name__ == "__main__":
  init()
  #直接用python运行  
  flups.WSGIServer(application, multithreaded=False, multiprocess=False, bindAddress=('127.0.0.1', 8081)).run()  
  #fastcgi方式运行  
  #flups.WSGIServer(application).run()  
