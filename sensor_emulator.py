import argparse
import random
import time
from opcua import ua, Server

class SensorEmulator:
    def __init__(self, id, type, value, unitcode):
        self.id = id
        self.type = type
        self.value = value
        self.unitcode = unitcode
        self.server = None

    def update_value(self):
        self.value = random.randint(15, 25)

    def start_server(self):
        self.server = Server()
        self.server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

        # Setup namespace
        uri = "http://examples.freeopcua.github.io"
        idx = self.server.register_namespace(uri)

        # Get Objects node, this is where we should put our nodes
        objects = self.server.get_objects_node()

        # Add a node for our sensor
        sensor_obj = objects.add_object(idx, self.id)

        # Add a variable to the sensor object
        temp_var = sensor_obj.add_variable(idx, self.type, self.value)
        temp_var.set_data_type(ua.DataType.Float)
        temp_var.set_writable()

        # Start the server
        self.server.start()

        while True:
            # Update the value of the variable
            self.update_value()
            temp_var.set_value(self.value)

            time.sleep(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sensor Emulator with OPC UA Server')
    parser.add_argument('id', type=str, help='Sensor ID')
    parser.add_argument('type', type=str, help='Sensor Type')
    parser.add_argument('unitcode', type=str, help='Unit Code')
    args = parser.parse_args()

    sensor = SensorEmulator(args.id, args.type, 0, args.unitcode)
    sensor.start_server()
