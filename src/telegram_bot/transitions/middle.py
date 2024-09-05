from bernard.engine import (
    Tr,
    triggers as trg,
)

from ..states import *

transitions_middle = [
    Tr(
        dest=MiddleXSelectUp,
        origin=MiddleXSendImage,
        factory=trg.Action.builder('select_image'),
    ),
    Tr(
        dest=MiddleXSelectDown,
        origin=MiddleXSendImage,
        factory=trg.Action.builder('reject_image'),
    ),
    Tr(
        dest=MiddleXSendImage,
        origin=MiddleXSelectUp,
        factory=trg.Action.builder('next'),
    ),
    Tr(
        dest=MiddleXSendImage,
        origin=MiddleXSelectDown,
        factory=trg.Action.builder('next'),
    ),
    Tr(
        dest=EndXCongrats,
        origin=MiddleXSendImage,
        factory=trg.Action.builder('finish_congrats'),
    ),
]
