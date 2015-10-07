#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def manipulate():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtlesim_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	# testing with value'[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
        rospy.loginfo('[2.0, 0.0, 0.0][0.0, 0.0, 1.8]')
        pub.publish('[2.0, 0.0, 0.0]','[0.0, 0.0, 1.8]')
        rate.sleep()

if __name__ == '__main__':
    try:
        manipulate()
    except rospy.ROSInterruptException:
        pass

