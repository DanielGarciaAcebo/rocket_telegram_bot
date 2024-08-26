from bernard.platforms.telegram import layers as tll
from pathlib import Path
from bernard.i18n import translate

from ..services import (
translate_txt,
get_current_datetime
)
MEDIA = Path(__file__).parent.parent.joinpath('media')

from ..baseStates import *


class EndXCongrats(TelegramBotState):
    """
    Congratulate the user for finding the number and propose to find another
    one.
    """

    @page_view('/bot/congrats')
    async def handle(self) -> None:
        keyboard = tll.InlineKeyboard([[
            tll.InlineKeyboardCallbackButton(
                text=translate.PLAY_AGAIN,
                payload={'action': 'again'},
            ),
        ]])
        url = str(MEDIA / "rockets/R11.txt")
        text = translate_txt(url)

        current_datetime_str = get_current_datetime()

        self.send(
            lyrText(text),
            lyrText(translate.CONGRATS),
            lyrText(current_datetime_str),
            keyboard
        )
