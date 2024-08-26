from bernard.engine import (
    Tr,
    triggers as trg,
)


from ..states import *
from ..services import *


transitions_end = [
 Tr(
        dest=MiddleXGuessRocketLaunch,
        origin=EndXCongrats,
        factory=trg.Action.builder('again'),
    )
]
