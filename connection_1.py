import time
from dronekit import connect,VehicleMode,LocationGlobalRelative

import argparse

parser=argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
args=parser.parse_args()

connection_string=args.connect

print("connecting to the vehicle on %s"%connection_string)
vehicle=connect(connection_string,wait_ready=True)

def arm_and_takeoff(tgt_altitude):
    print("Armining motor")

    while not vehicle.is_armable:
        time.sleep(1)

    vehicle.mode=VehicleMode("GUIDED")
    vehicle.armed =True

    print("TakeOff")
    vehicle.simple_takeoff(tgt_altitude)

    while True:
        altitude =vehicle.location.global_relative_frame.alt

        if altitude>=tgt_altitude -1:
            print("altitude reached")
            break

arm_and_takeoff(10)

vehicle.airspeed=7

print("go to waypoint1")
wpl=LocationGlobalRelative(35.9872609,-95.8753037,10)

vehicle.simple_goto(wpl)

time.sleep(30)

print("comingback")

vehicle.mode=VehicleMode("RTL")

time.sleep(20)
vehicle.close()