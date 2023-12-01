import subprocess
import time

# Example commands
humid_command = "aiocoap-client coap://[2001:660:4403:4bd::3158]:5683/sensors/gethumid"

noise_command = "aiocoap-client coap://[2001:660:4403:4bd::3355]:5683/sensors/getnoise"
# Function to execute command and capture output
def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        return float(output)  # Assuming the output is a number
    else:
        print("Error executing command '{}': {}".format(command, error))
        return None

# Lists to store data
timestamps = []
humid_values = []
noise_values = []

# Run the loop for 30 seconds
tm = 0
while tm < 30:
    # Execute commands and capture output
    humid_value = execute_command(humid_command)
    noise_value = execute_command(noise_command)

    # Append data to lists
    timestamps.append(tm)
    humid_values.append(humid_value)
    noise_values.append(noise_value)
    tm = tm+1
    # Wait for 1 second
    time.sleep(1)

# Print the arrays
print(timestamps)
print(humid_values)
print(noise_values)
