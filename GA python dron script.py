#!/usr/bin/env python
# coding: utf-8

# In[3]:


from dronekit import connect, vehiclemode, locationGlobalRelative
import time
import exceptions
import argparse

#function to connect script to drone
def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()
    
    connection_string = args.connect
    vehicle = connect(connection_string, wait_ready=True)
    
    return vehicle
#anather fuction to call for takeoff
def arm_and_takeoff(aTargetAltitude):
    while not vehicle.is_armable:
        print("waiting for vehicle to become armble")
        time.sleep(1)
        
    vehicle.mode = vehicleMode("GUIDED")
    while vehicle.mode!="GUIDED":
        print("waiting for vehicle to enter GUIDED mode")
        time.sleep(1)
        
    vehicle.armed=True
    while vehicle.armed==False:
        print("waiting for vehicle to become armed.")
        time.sleep(1)
        
    vehicle.simple_takeoff(aTargetAltitude)
    
    while True:
        print("current Altitude: %d"%vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*.95:
            break
        time.sleep(1)
        
    print("Target altitude reached")
    return None

vehicle=connectMyCopter()
print("About to take off..")
vehicle.mode=vehicleMode("Guided")
arm_and_takeoff(2)
vehicle.mode=vehiclemode("LAND")

Time.sleep(2)
print("End of the fuction")
print("Ardupilot version:"%vehicle.version)

while True:
    time.sleep(2)
    vehicle.close()
        
        

