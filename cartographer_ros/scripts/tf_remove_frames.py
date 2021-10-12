#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2016 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage

class TFRemoveFrames(Node):
    def __init__(self):
        super().__init__('tf_remove_frames')

        self._subscriber = self.create_subscription('/tf_in', TFMessage, self.cb, 10)
        self._publisher = self.create_publisher('/tf_out', TFMessage, 1)

        self.declare_parameter('remove_frames')
        self._remove_frames = self.get_parameter('remove_frames')

    def cb(self, msg):
        transforms_ = []
        for t in msg.transforms:
            if t.header.frame_id.lstrip('/') not in self._remove_frames and t.child_frame_id.lstrip('/') not in self._remove_frames:
              transforms_.append(t)

        self._publisher.publish(TFMessage(transforms=transforms_))


def main(args=None):
    rclpy.init(args=args)
    tf_rf_ = TFRemoveFrames()
    rclpy.spin(tf_rf_)
    tf_rf_.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()