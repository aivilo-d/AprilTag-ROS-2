import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage
from enum import Enum, auto
import pygame
from typing import Tuple
from pathlib import Path
from time import sleep
from geometry_msgs.msg import TransformStamped


class CameraDroneNavigationNode(Node):
    def __init__(self):
        super().__init__("camera_drone_navigation_node")
        self.create_subscription(TFMessage, "tf", self.process_tf, 10)


        self.current_tf: TransformStamped = None
  
        
    def process_tf(self, msg: TFMessage):
        # Only use data from the first tag
        if msg.transforms:
            self.current_tf = msg.transforms[0]
        else:
            self.current_tf = None

        print(self.current_tf)
    


def main(args=None):
    rclpy.init(args=args)
    node = CameraDroneNavigationNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()