#!/usr/bin/env python3

import rospy
import time
import sys
import math
import angles
from geometry_msgs.msg import Pose2D, Twist
from turtlesim.msg import Pose


def callback_robot_pose(msg):
    global robot_odom

    robot_odom.x = msg.x
    robot_odom.y = msg.y
    robot_odom.theta = msg.theta


def callback_robot_goal(msg):
    global goal

    goal.x = msg.x
    goal.y = msg.y
    goal.theta = msg.theta


def robot_comand(robot_odom, goal, gain):
    global k_i
    # robot coords
    x = robot_odom.x
    y = robot_odom.y
    theta = robot_odom.theta

    # goal coords
    x_d = goal.x
    y_d = goal.y
    theta_d = goal.theta

    # gains
    K_v = gain[0]
    K_omega = gain[1]

    # Errors
    delta_x = x_d - x
    delta_y = y_d - y

    distance = 1.5

    error_p_exact = math.sqrt((delta_x)**2 + (delta_y)**2)

    erro_p = round(error_p_exact - distance, 3)
    erro_int = 0

    print('erro_p')
    print(erro_p)

    heading = round(math.atan2(delta_y, delta_x), 3)

    erro_theta = angles.shortest_angular_distance(theta, heading)

    erro_int += erro_p*0.066

    omega = K_omega*erro_theta
    v = K_v*erro_p + k_i*erro_int

    robot_vel = Twist()
    robot_vel.linear.x = v
    robot_vel.angular.z = omega

    return robot_vel


def main_control():
    global robot_odom
    global gain

    rospy.init_node('turtle_control', anonymous=True)
    robot_pose = rospy.Subscriber('/turtle2/pose', Pose, callback_robot_pose)
    robot_goal = rospy.Subscriber('/turtle1/pose', Pose, callback_robot_goal)
    pub_cmd_vel = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(15)

    cmd_vel = Twist()

    while not rospy.is_shutdown():

        cmd_vel = robot_comand(robot_odom, goal, gain)

        print(cmd_vel)

        pub_cmd_vel.publish(cmd_vel)

        rate.sleep()


### Main ###
robot_odom = Pose2D()
goal = Pose2D()
k_v = 1.5
k_i = 0.5
k_w = 1.5
gain = [k_v, k_w]

if __name__ == '__main__':
    main_control()
