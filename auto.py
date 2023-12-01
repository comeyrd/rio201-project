import subprocess

# Prompt user for values
BORDER_ROUTER = input("Enter BORDER_ROUTER value: ")
HC_SRV = input("Enter HC_SRV value: ")
TUN_IP = input("Enter TUN_IP value: ")

# Construct commands
tunslip_command = "sudo tunslip6.py -v2 -L -a m3-{} -p 20000 {}::1/64".format(BORDER_ROUTER, TUN_IP)
border_router_command = "iotlab-node --update ./10-humid-censor/border-router.iotlab-m3 -l lille,m3,{}".format(BORDER_ROUTER)
server_command = "iotlab-node --update ./10-humid-censor/er-example-server.iotlab-m3 -l lille,m3,{}".format(HC_SRV)

# Display commands
print("\ncall the following commands:")
print("{}".format(tunslip_command))
print("{}".format(border_router_command))
print("{}".format(server_command))

# Wait for BR_IP input
BR_IP = input("\nEnter BR_IP value: ")

lynx_command = "lynx -dump http://[{}]".format(BR_IP)
print("\n4. {}".format(lynx_command))


NC_SRV = input("Enter NC_SRV value: ")
HC_IP = input("\nEnter HC_IP value: ")


ip_parts = HC_IP.split(':')
print(ip_parts)
ip_parts[4] = ip_parts[5]

formatted_hc_ip = "uip_ip6addr(ipaddr, 0x{}, 0x{}, 0x{}, 0x{}, 0, 0, 0, 0x{})".format(ip_parts[0].upper(),ip_parts[1].upper(),ip_parts[2].upper(),ip_parts[3].upper(),ip_parts[4].upper())

# Display the formatted HC_IP
print("\n {}\n".format(formatted_hc_ip))

print("make TARGET=iotlab-m3")

server_command = "iotlab-node --update ./11-noise-censor/er-example-client.iotlab-m3 -l lille,m3,{}".format(NC_SRV)
print("\ {}".format(server_command))

print("\n4. {}".format(lynx_command))



coap_humid_command = "aiocoap-client coap://[{}]:5683/sensors/gethumid".format(HC_IP)
coap_humid_hello_command = "aiocoap-client coap://[{}]:5683/test/hello".format(HC_IP)

# Display CoAP commands
print("\n5. {}".format(coap_humid_command))
print("6. {}".format(coap_humid_hello_command))


NC_IP = input("\nEnter NC_IP value: ")

coap_noise_command = "aiocoap-client coap://[{}]:5683/sensors/getnoise".format(NC_IP)
coap_noise_hello_command = "aiocoap-client coap://[{}]:5683/test/hello".format(NC_IP)


print("\n7. {}".format(coap_noise_command))
print("8. {}".format(coap_noise_hello_command))



print('humid_command = "{}"\n'.format(coap_humid_command))
print('noise_command = "{}"\n'.format(coap_noise_command))
