from bernard.engine import (
    Tr,
)


from ..states import *
from ..services import *

transitions_middle = [
    Tr(
        dest=MiddleXGuessRocketLaunchAgain,
        origin=MiddleXGuessRocketLaunch,
        factory=Rocket.builder(is_right=False),
    ),
    Tr(
        dest=MiddleXGuessRocketLaunchAgain,
        origin=MiddleXGuessRocketLaunchAgain,
        factory=Rocket.builder(is_right=False),
    ),
    Tr(
        dest=EndXCongrats,
        origin=MiddleXGuessRocketLaunchAgain,
        factory=Rocket.builder(is_right=True),
    ),
    Tr(
        dest=EndXCongrats,
        origin=MiddleXGuessRocketLaunch,
        factory=Rocket.builder(is_right=True),
    ),
]
