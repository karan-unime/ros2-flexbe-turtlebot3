#!/usr/bin/env python3

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher

from geometry_msgs.msg import Twist


class MoveForwardState(EventState):
    """
    Moves TurtleBot3 forward for fixed duration.

    -- speed      float  Linear speed in m/s
    -- duration   float  Duration in seconds

    <= done
    """

    def __init__(self, speed=0.2, duration=3.0):
        super(MoveForwardState, self).__init__(
            outcomes=['done']
        )

        self._speed = speed
        self._duration = duration

        self._topic = '/cmd_vel'

        self._pub = ProxyPublisher({
            self._topic: Twist
        })

        self._elapsed = 0.0

    def on_enter(self, userdata):
        Logger.loginfo(
            f'MoveForward: speed={self._speed} duration={self._duration}'
        )

        self._elapsed = 0.0

    def execute(self, userdata):

        self._elapsed += 0.1

        if self._elapsed >= self._duration:
            return 'done'

        msg = Twist()

        msg.linear.x = self._speed

        self._pub.publish(self._topic, msg)

        return None

    def on_exit(self, userdata):

        self._pub.publish(self._topic, Twist())

        Logger.loginfo('MoveForward: stopped')

    def on_stop(self):

        self._pub.publish(self._topic, Twist())
