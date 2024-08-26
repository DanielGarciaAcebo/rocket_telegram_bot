from random import SystemRandom
from bernard.platforms.telegram.layers import (
    TextLayer as lyText
)

from bernard.i18n import  translate

from pathlib import Path

from ..baseStates import *
from ..services import (
cs,
translate_txt
)

random = SystemRandom()

MEDIA = Path(__file__).parent.parent.joinpath('media')

class MiddleXGuessRocketLaunch(TelegramBotState):

    @page_view("/bot/guess-rocket")
    @cs.inject()
    async def handle(self, context) -> None:

        context["rocket_number"] = 11
        text = translate.ROCKET

        rocket = translate_txt(str(MEDIA / "rockets/R1.txt"))

        self.send(
            lyrText(text),
            lyrText(rocket)
        )




class MiddleXGuessRocketLaunchAgain(TelegramBotState):
    """
    If the user gave a number that is wrong, we give an indication whether that
    guess is too low or too high.
    """
    @page_view('/bot/guess-rocket-again')
    @cs.inject()
    async def handle(self, context) -> None:
        user_frame = self.trigger.rocket_number
        url = str(MEDIA / "rockets/R" )
        url = url + str(user_frame) + ".txt"

        text = translate_txt(url)
        if text is None:
            url = str(MEDIA / "rockets/R22.txt")
            text = translate_txt(url)

        self.send(lyText(text))
        if user_frame < context["rocket_number"]:
            self.send(lyText(translate.UP))
        else:
            self.send(lyText(translate.DOWN))


