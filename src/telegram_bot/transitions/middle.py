from bernard.engine import (
    Tr,
    triggers as trg,
)

from ..states import *

transitions_middle = [
    Tr(
        dest=MiddleXCheckTrue,
        origin=MiddleXSendImage,
        factory=trg.Action.builder('select_image'),
    ),
    Tr(
        dest=MiddleXCheckFalse,
        origin=MiddleXSendImage,
        factory=trg.Action.builder('reject_image'),
    ),
    Tr(
        dest=MiddleXSendImage,
        origin=MiddleXCheckFalse,
        factory=trg.Action.builder('Next'),
    ),
    Tr(
        dest=MiddleXSendImage,
        origin=MiddleXCheckTrue,
        factory=trg.Action.builder('Next'),
    ),
    Tr(
        dest=EndXCongrats,
        origin=MiddleXCheckTrue,
        factory=trg.Action.builder('finish_congrats'),
    ),
]
