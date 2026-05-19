#!/usr/bin/env python3

from flexbe_core import Behavior, Autonomy, OperatableStateMachine

from .move_forward_state import MoveForwardState
from .turn_left_state import TurnLeftState
from .stop_robot_state import StopRobotState
from .log_message_state import LogMessageState


class SquarePatrolBehaviorSM(Behavior):

    def __init__(self):
        super(SquarePatrolBehaviorSM, self).__init__()

        self.name = 'SquarePatrol'

    def create(self):

        _state_machine = OperatableStateMachine(
            outcomes=['finished']
        )

        with _state_machine:

            OperatableStateMachine.add(
                'LogStart',
                LogMessageState(message='Square Patrol Start'),
                transitions={'done': 'Forward1'},
                autonomy={'done': Autonomy.Full}
            )

            OperatableStateMachine.add(
                'Forward1',
                MoveForwardState(speed=0.2, duration=3.0),
                transitions={'done': 'Turn1'},
                autonomy={'done': Autonomy.Low}
            )

            OperatableStateMachine.add(
                'Turn1',
                TurnLeftState(duration=2.0),
                transitions={'done': 'Forward2'},
                autonomy={'done': Autonomy.Full}
            )

            OperatableStateMachine.add(
                'Forward2',
                MoveForwardState(speed=0.2, duration=3.0),
                transitions={'done': 'Turn2'},
                autonomy={'done': Autonomy.Low}
            )

            OperatableStateMachine.add(
                'Turn2',
                TurnLeftState(duration=2.0),
                transitions={'done': 'Forward3'},
                autonomy={'done': Autonomy.Full}
            )

            OperatableStateMachine.add(
                'Forward3',
                MoveForwardState(speed=0.2, duration=3.0),
                transitions={'done': 'Turn3'},
                autonomy={'done': Autonomy.Low}
            )

            OperatableStateMachine.add(
                'Turn3',
                TurnLeftState(duration=2.0),
                transitions={'done': 'Forward4'},
                autonomy={'done': Autonomy.Full}
            )

            OperatableStateMachine.add(
                'Forward4',
                MoveForwardState(speed=0.2, duration=3.0),
                transitions={'done': 'StopRobot'},
                autonomy={'done': Autonomy.Low}
            )

            OperatableStateMachine.add(
                'StopRobot',
                StopRobotState(),
                transitions={'done': 'finished'},
                autonomy={'done': Autonomy.Full}
            )

        return _state_machine
