from bernard.engine import (
    Tr,
    triggers as trg,
)


from ..states import *


transitions_end = [
 Tr(
        dest=StartXWelcome,
        origin=EndXCongrats,
        factory=trg.Action.builder('again'),
    )
]
