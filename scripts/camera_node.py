#!/usr/bin/env python3

import rospy
import time
import sys
import cv2
import numpy as np
from geometry_msgs.msg import Pose2D
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def get_img(cap):

    _, cv_image = cap.read()

    bridge = CvBridge()
    img_msg = bridge.cv2_to_imgmsg(cv_image, "bgr8")

    cv2.namedWindow('Boring')
    cv2.imshow('Boring', cv_image)
    cv2.waitKey(5)

    return img_msg


def camera_main(video):

    rospy.init_node('camera_node', anonymous=True)

    pub_image = rospy.Publisher('camera_raw', Image, queue_size=10)

    rate = rospy.Rate(30)
    pub_img = Image()

    cap = cv2.VideoCapture(video)

    while not rospy.is_shutdown():
        print('camera node runing ook')

        pub_img = get_img(cap)

        pub_image.publish(pub_img)

        rate.sleep()


if __name__ == '__main__':
    camera_main(video=0)
