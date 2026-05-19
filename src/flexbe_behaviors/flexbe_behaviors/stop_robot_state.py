#!/usr/bin/env python3

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher

from geometry_msgs.msg import Twist


class StopRobotState(EventState):
    """
    Stops TurtleBot3.

    <= done
    """

    def __init__(self):
        super(StopRobotState, self).__init__(
            outcomes=['done']
        )

        self._pub = ProxyPublisher({
            '/cmd_vel': Twist
        })

    def on_enter(self, userdata):

        Logger.loginfo('Stopping robot')

        self._pub.publish('/cmd_vel', Twist())

    def execute(self, userdata):

        return 'done'

    def on_stop(self):

        self._pub.publish('/cmd_vel', Twist())
