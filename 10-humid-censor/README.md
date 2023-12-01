Lille	128	2001:660:4403:0480::/64	2001:660:4403:04ff::/64
iotlab-auth -u riotp13

choose ip :	2001:660:4403:048b::/64

37 - BR
38 - SRV

make TARGET=iotlab-m3

________________________________________________________________________________________________________________
Choose the border router node
BORDER_ROUTER = 
SERVER = 
TUN_IP=
sudo tunslip6.py -v2 -L -a m3-BORDER_ROUTER -p 20000 TUN_IP::1/64
iotlab-node --update ./border-router.iotlab-m3 -l lille,m3,BORDER_ROUTER
iotlab-node --update ./server.iotlab-m3 -l lille,m3,SRV
wait BR_IP=
lynx -dump http://[BR_IP]
wait SVR_IP=
aiocoap-client coap://[SVR_IP]:5683/sensors/light
aiocoap-client coap://[SVR_IP]:5683/test/hello

