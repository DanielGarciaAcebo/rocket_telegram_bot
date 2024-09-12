from bernard.platforms.telegram import layers as tll
from pathlib import Path

from ..services import (
get_current_datetime,
send_photo
)
MEDIA = Path(__file__).parent.parent.joinpath('media')

from ..baseStates import *
from ..services import *


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

        photo_id = context["photo_id"]
        used_id_len = len(context["used_id"])

        self.send(
            lyrText(t.CONGRATS),
            lyrText(t("SELECTED_PHOTO", photo_id=photo_id, used_id_len=used_id_len)),
            lyrText(t.ICON_CONGRATS),
            keyboard
        )
