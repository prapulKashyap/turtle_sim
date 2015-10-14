#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys
import numpy as np
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

def manipulate(T):
	print("programstarted")	
	T = int(T)
	rospy.init_node('turtlesim_node', anonymous=True)
	rate = rospy.Rate(70.0) # 70hz
	twist = Twist()
	t0 = rospy.get_time()
		
    	while not rospy.is_shutdown():
		t = rospy.get_time() - t0
		
		if(t>10):#reset the time when t reaches T
			t0 = rospy.get_time()

		vx = 12*np.pi*np.cos(4*np.pi*t/T)/T#dx/dt
		vy = 6*np.pi*np.cos(2*np.pi*t/T)/T#dy/dt
		us = np.sqrt(np.power(vx,2) + np.power(vy,2))
		ax = (-48 * np.pi * np.pi * np.sin(4 * np.pi * t / T)) / (T * T)#d2x/dt2
		ay = (-12 * np.pi * np.pi * np.sin(2 * np.pi * t / T)) / (T * T)#d2y/dt2	
		omega = (vx * ay - vy * ax) / (vx * vx + vy * vy)#angular velocity
		twist.linear.x = us
		twist.linear.y = 0.0
		twist.linear.z = 0.0
		twist.angular.x = 0.0
		twist.angular.y = 0.0
		twist.angular.z = omega
        	rospy.loginfo(str(twist))
        	pub.publish(twist)
        	rate.sleep()

if __name__ == '__main__':
    try:
	if len(sys.argv)<2:
		print("usage manipulate.py <value of T>")
	else:
		rospy.wait_for_service('turtle1/teleport_absolute')			# wait for the turtle simulator start running
		#turtle_sp = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute) 
		#turtle_sp = (20,5,0)		#set turtle initial position
		#rospy.init_node('steering_turtle', anonymous=True) # init node
		manipulate(sys.argv[1])
    except rospy.ROSInterruptException:
	pass

