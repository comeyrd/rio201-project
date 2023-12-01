# Ceyraud RIO201 Project

## How to deploy main project

To deploy it, clone the repo and copy the file inside of it into the iot-lab/parts/contiki/examples/iotlab/. (For exemple put 10-humid-censor into iot-lab/parts/contiki/examples/iotlab/10-humid-censor)

You need to compile the 10 and 11 using make TARGET=iotlab-m3

Then login on the shell : iotlab-auth -u yourlogin

then create a project with 3 nodes close to each other with the M3 architecture.

Then launch auto.py and follow the instructions,
/!\ Carefull /!\ when typing the ip addresses, use the double quotes before and after (for exemple "2001:660:4403:0480")

## How to deploy the http vs coap project

Go into 10-humid-censor, 
You need to compile using make TARGET=iotlab-m3

Then login on the shell : iotlab-auth -u yourlogin

then create a project with 3 nodes close to each other with the M3 architecture.

Then launch the coapvshttp.py script and follow the instruction.

## Appendix

To find an ip address for the tunslip, here is the Lille Ip address range : 

Lille	128	2001:660:4403:0480::/64	to 2001:660:4403:04ff::/64
