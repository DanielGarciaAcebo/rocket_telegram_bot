from pathlib import Path
from random import SystemRandom

from bernard.platforms.telegram import layers as tll
from bernard.platforms.telegram.layers import (
    TextLayer as lyText
)

from ..baseStates import *
from ..services import *

random = SystemRandom()

MEDIA = Path(__file__).parent.parent.joinpath('media')


class MiddleXSendImage(TelegramBotState):

    @page_view("/bot/guess-rocket")
    @cs.inject()
    async def handle(self, context) -> None:
        if "used_ids" not in context:
            context["used_ids"] = []

        used_ids = context["used_ids"]

        conversation_id = self.request.conversation.id

        photo_id = get_random_id(used_ids)
        context["photo_id"] = photo_id

        url, rocket_lunch = get_photo_by_id(photo_id)

        context["rocket_lunch"] = rocket_lunch
        context["url"] = url

        send_photo(url, conversation_id)

        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.SELECT_IMAGE_BUTTON,
                payload={'action': 'select_image'},
            )],

            [tll.InlineKeyboardCallbackButton(
                text=t.REJECT_IMAGE_BUTTON,
                payload={'action': 'reject_image'},
            )]
        ])

        self.send(
            lyText(t.TEXT_SEND_IMAGE_MIDDLE),
            keyboard
        )

class MiddleXCheckTrue(TelegramBotState):

    @page_view("/bot/guess-rocket-true")
    @cs.inject()
    async def handle(self, context) -> None:
        photo_id = context.get("photo_id")
        rocket_lunch = context["rocket_lunch"]


        if not rocket_lunch == 1:
            if "used_ids" not in context:
                context["used_ids"] = []

            if photo_id is not None:
                context["used_ids"].append(photo_id)
            keyboard = tll.InlineKeyboard([
                [tll.InlineKeyboardCallbackButton(
                    text=t.NEXT_IMAGE_BUTTON,
                    payload={'action': 'Next'},
                )],
            ])
            self.send(
                lyText(t.IMAGE_FALSE_SELECT_TRUE),
                lyText(t.ICON_FAIL),
                keyboard
            )
            return
        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.IMAGE_CORRECT_SELECT_TRUE_BUTTON,
                payload={'action': 'finish_congrats'},
            )],
        ])
        self.send(
            lyText(t.IMAGE_CORRECT_SELECT_TRUE),
            keyboard
        )


class MiddleXCheckFalse(TelegramBotState):

    @page_view("/bot/guess-rocket-false")
    @cs.inject()
    async def handle(self, context) -> None:
        photo_id = context.get("photo_id")
        rocket_lunch = context["rocket_lunch"]
        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.NEXT_IMAGE_BUTTON,
                payload={'action': 'Next'},
            )],
        ])
        if rocket_lunch == 1:

            self.send(
                lyText(t.IMAGE_CORRECT_SELECT_FALSE),
                lyText(t.ICON_FAIL),
                keyboard
            )
            pass
        else:
            if "used_ids" not in context:
                context["used_ids"] = []

            if photo_id is not None:
                context["used_ids"].append(photo_id)

            self.send(
                lyText(t.IMAGE_FALSE_SELECT_FALSE),
                lyText(t.ICON_CONGRATS),
                keyboard,
            )
            return
