import subprocess

# Prompt user for values
BORDER_ROUTER = input("Enter BORDER_ROUTER value: ")
COAP_srv = input("Enter COAP nodenbr value: ")
HTTP_srv = input("Enter HTTP nodenbr value: ")

TUN_IP = input("Enter TUN_IP value: ")


# Construct commands
tunslip_command = "sudo tunslip6.py -v2 -L -a m3-{} -p 20000 {}::1/64".format(BORDER_ROUTER, TUN_IP)
border_router_command = "iotlab-node --update ./10-humid-censor/border-router.iotlab-m3 -l lille,m3,{}".format(BORDER_ROUTER)
coap_command = "iotlab-node --update ./10-humid-censor/er-example-server.iotlab-m3 -l lille,m3,{}".format(COAP_srv)
http_command = "iotlab-node --update ./10-humid-censor/http-server.iotlab-m3 -l lille,m3,{}".format(HTTP_srv)

# Display commands
print("\ncall the following commands:")
print("{}".format(tunslip_command))
print("{}".format(border_router_command))
print("{}".format(coap_command))
print("{}".format(http_command))

# Wait for BR_IP input
BR_IP = input("\nEnter BR_IP value: ")

lynx_command = "lynx -dump http://[{}]".format(BR_IP)
print("\n4. {}".format(lynx_command))


COAP_ip = input("Enter COAP_IP value: ")
http_ip = input("\nEnter HTTP_IP value: ")


http_command = "time lynx -dump http://[{}]".format(http_ip)
coap_noise_hello_command = "time aiocoap-client coap://[{}]:5683/test/hello".format(COAP_ip)


print("\n7. {}".format(http_command))
print("8. {}".format(coap_noise_hello_command))
