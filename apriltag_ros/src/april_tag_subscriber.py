import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage
from enum import Enum, auto
import pygame
from typing import Tuple
from pathlib import Path
from time import sleep
from geometry_msgs.msg import TransformStamped
import time
import math



class CameraDroneNavigationNode(Node):
    def __init__(self):
        super().__init__("camera_drone_navigation_node")
        self.create_subscription(TFMessage, "tf", self.process_tf, 10)
        pygame.init()
        pygame.mixer.init()

        self.A = [0.05, 0]
        self.B = [0.015, 0.05]
        self.C = [-0.05,0]
        self.D = [0.015, -0.05]

        self.letter = self.D
        self.timer = self.create_timer(1.5, self.run_loop)

        self.current_tf: TransformStamped = None
  
        
    def process_tf(self, msg: TFMessage):
        # Only use data from the first tag
        if msg.transforms:
            for item in msg.transforms:
                if (item.child_frame_id == "ID4"):
                    self.current_tf = item
                    break
                else:
                    self.current_tf = None
    
    def print_stuff(self):
        if self.current_tf:
            print("X: " + f"{self.current_tf.transform.translation.x}")
            print("Y: " + f"{self.current_tf.transform.translation.y}")



    
    def run_loop(self):
        # lets do x 
        if self.current_tf:
            self.print_stuff()

            error_x = abs(self.letter[0]-self.current_tf.transform.translation.x)
            error_y = abs(self.letter[1] - self.current_tf.transform.translation.y)

            if((error_x > error_y) and (error_x > .0075)):
                
                if(self.current_tf.transform.translation.x > self.letter[0]):
                    print("RIGHT")
                    pygame.mixer.music.load("sounds/right.mp3")
                    pygame.mixer.music.play()

                if(self.current_tf.transform.translation.x < self.letter[0]):
                    print("LEFT")
                    pygame.mixer.music.load("sounds/left.mp3")
                    pygame.mixer.music.play()
                    
            elif((error_y > error_x) and (error_y > .0075)):
                
                if(self.current_tf.transform.translation.y > self.letter[1]):
                    print("BACK")
                    pygame.mixer.music.load("sounds/back.mp3")
                    pygame.mixer.music.play()

                if(self.current_tf.transform.translation.y < self.letter[1]):
                    print("FORWARD")
                    pygame.mixer.music.load("sounds/forward.mp3")
                    pygame.mixer.music.play()
            elif(error_x < 0.0075 and error_y < 0.0075):
            # elif((self.current_tf.transform.translation.x < 0.015 or self.current_tf.transform.translation.x > 0) and (self.current_tf.transform.translation.y > 0.045 or self.current_tf.transform.translation.y < 0.055)):
                    pygame.mixer.music.load("sounds/descend.mp3")
                    pygame.mixer.music.play()

            else:
                pass



            

        # pygame.mixer.music.load("sounds/descend.mp3")
        # pygame.mixer.music.play()

def main(args=None):
    rclpy.init(args=args)
    node = CameraDroneNavigationNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()