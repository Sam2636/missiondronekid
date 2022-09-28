import time
from dronekit import connect,VehicleMode,LocationGlobalRelative

import argparse

parser=argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
args=parser.parse_args()

connection_string=args.connect
sitl = None


#Start SITL if no connection string specified
if not connection_string:
    import dronekit_sitl
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()

print("connecting to the vehicle on %s"%connection_string)
vehicle=connect(connection_string,wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

        
    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:      
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude


    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command 
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)      
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: #Trigger just below target alt.
            print("Reached target altitude")
            break
        time.sleep(1)


#Arm and take of to altitude of 5 meters
arm_and_takeoff(10)

vehicle.airspeed=7

print("go to waypoint1")
wp1=LocationGlobalRelative(12.976900, 80.264600, 10)

vehicle.simple_goto(wp1)

time.sleep(30)

print("comingback")

vehicle.mode=VehicleMode("RTL")

time.sleep(20)
vehicle.close()