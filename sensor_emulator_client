from opcua import Client
import time

url = "opc.tcp://localhost:4840/freeopcua/server/"
client = Client(url)
client.connect()

# Assuming the sensor emulator node ID is "sensor"
node = client.get_node("ns=1;s=sensor")

while True:
    temperature = node.get_value()
    print(f"Temperature: {temperature} CEL")
    time.sleep(1)

client.disconnect()
