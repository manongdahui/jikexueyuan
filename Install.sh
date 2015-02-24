#!/bin/bash
cd `dirname $0`
source /etc/profile
sudo apt-get install nginx
sudo apt-get install python-flup
sudo apt-get install spawn-fcgi
sudo apt-get install curl
##for thrift ##
sudo apt-get install libboost-dev libboost-test-dev libboost-program-options-dev libboost-system-dev libboost-filesystem-dev libevent-dev automake libtool flex bison pkg-config g++ libssl-dev python-dev
wget http://mirror.bit.edu.cn/apache/thrift/0.9.2/thrift-0.9.2.tar.gz
tar -xvf thrift-0.9.2.tar.gz
cd thrift-0.9.2
sudo ./configure
sudo make
cd lib/py
sudo python setup.py install
cd ../../

sudo apt-get install thrift-compiler
rm -rf thrift-0.9.2.tar.gz
thrift --gen py demo.thrift

service nginx start
cp nginx_example /etc/nginx/site-available/example
ln -s /etc/nginx/site-enable/example /etc/nginx/site-available/example
sevice nginx restart

#./fcgi.py
spawn-fcgi fcgi.py -a 127.0.0.1 -p 8081 
curl "localhost:8080/?pageid=1&areaid=1&userid=liyongbao&history=v1-v2-v3&num=10"


