from bernard.platforms.telegram import layers as tll
from pathlib import Path

from ..services import (
get_current_datetime,
send_photo
)
MEDIA = Path(__file__).parent.parent.joinpath('media')

from ..baseStates import *
from ..services import cs


class EndXCongrats(TelegramBotState):
    """
    Congratulate the user for finding the number and propose to find another
    one.
    """

    @page_view('/bot/congrats')
    @cs.inject()
    async def handle(self, context) -> None:
        keyboard = tll.InlineKeyboard([[
            tll.InlineKeyboardCallbackButton(
                text=t.PLAY_BUTON_AGAIN,
                payload={'action': 'again'},
            ),
        ]])
        url =  context["url"]
        conversation_id = self.request.conversation.id
        send_photo(url, conversation_id)

        current_datetime_str = get_current_datetime()

        used_ids = len(context["used_ids"])

        self.send(
            lyrText(t.CONGRATS),
            lyrText(t("REJECTS_PHOTOS_LEN", used_ids=used_ids)),
            lyrText(current_datetime_str),
            lyrText(t.ICON_CONGRATS),
            keyboard
        )
