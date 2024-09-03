from bernard.engine import (
    Tr,
    triggers as trg,
)
from bernard.platforms.telegram.layers import BotCommand

from ..states import *

transitions_start = [
    Tr(
        dest=StartXWelcome,
        factory=trg.Equal.builder(BotCommand('/start')),
    ),
    Tr(
        dest=StartXWelcome,
        factory=trg.Equal.builder(BotCommand('/lets_play')),
    ),
    Tr(
        dest=StartXWelcomeTest,
        factory=trg.Equal.builder(BotCommand('/start_text')),
    ),
    Tr(
        dest=StartXHelp,
        factory=trg.Equal.builder(BotCommand('/help')),
    ),
    Tr(
        dest=MiddleXSendImage,
        origin=StartXWelcome,
        factory=trg.Action.builder('play'),
    ),
    Tr(
        dest=MiddleXSendImage,
        origin=StartXWelcomeTest,
        factory=trg.Action.builder('play'),
    ),
    Tr(
        dest=StartXWelcomeTest,
        factory=trg.Action.builder('start_text'),
    ),
    Tr(
        dest=StartXHelp,
        origin=StartXWelcome,
        factory=trg.Action.builder('help'),
    ),
    Tr(
        dest=StartXWelcome,
        origin=StartXHelp,
        factory=trg.Action.builder('back_welcome'),
    ),
]
