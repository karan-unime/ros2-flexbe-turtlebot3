#!/usr/bin/env python3

from flexbe_core import Behavior, Autonomy, OperatableStateMachine

from .move_forward_state import MoveForwardState
from .turn_left_state import TurnLeftState
from .turn_right_state import TurnRightState
from .stop_robot_state import StopRobotState
from .log_message_state import LogMessageState


class TB3DirectBehaviorSM(Behavior):

    def __init__(self):
        super(TB3DirectBehaviorSM, self).__init__()

        self.name = 'TB3Direct'

    def create(self):

        _state_machine = OperatableStateMachine(
            outcomes=['finished']
        )

        with _state_machine:

            OperatableStateMachine.add(
                'LogStart',
                LogMessageState(message='TB3 Direct Start'),
                transitions={'done': 'MoveForward'},
                autonomy={'done': Autonomy.Full}
            )

            OperatableStateMachine.add(
                'MoveForward',
                MoveForwardState(speed=0.2, duration=3.0),
                transitions={'done': 'TurnLeft'},
                autonomy={'done': Autonomy.Low}
            )

            OperatableStateMachine.add(
                'TurnLeft',
                TurnLeftState(duration=2.0),
                transitions={'done': 'TurnRight'},
                autonomy={'done': Autonomy.Full}
            )

            OperatableStateMachine.add(
                'TurnRight',
                TurnRightState(duration=2.0),
                transitions={'done': 'StopRobot'},
                autonomy={'done': Autonomy.Full}
            )

            OperatableStateMachine.add(
                'StopRobot',
                StopRobotState(),
                transitions={'done': 'finished'},
                autonomy={'done': Autonomy.Full}
            )

        return _state_machine
