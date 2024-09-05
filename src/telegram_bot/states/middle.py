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
        conversation_id = self.request.conversation.id
        if context["upper_limit"] - context["lower_limit"] > 3:
            photo_id = get_random_id(context["lower_limit"], context["upper_limit"])
            context["photo_id"] = photo_id
            context["used_id"].append(photo_id)

            url, rocket_lunch = get_photo_by_id(photo_id)
            context["rocket_lunch"] = rocket_lunch
            context["url"] = url

            send_photo(url, conversation_id)

            keyboard = tll.InlineKeyboard([
                [tll.InlineKeyboardCallbackButton(
                    text=t.SELECT_IMAGE_UP_BUTTON,
                    payload={'action': 'select_image'},
                )],

                [tll.InlineKeyboardCallbackButton(
                    text=t.SELECT_IMAGE_DOWN_BUTTON,
                    payload={'action': 'reject_image'},
                )]
            ])
            self.send(
                lyrText(t("TEXT_SEND_ID_MIDDLE", id=photo_id)),
                lyText(t.TEXT_SEND_IMAGE_MIDDLE),
                lyText(t.ICON_INDECISION),
                keyboard
            )
        else:
            keyboard = tll.InlineKeyboard([
                [tll.InlineKeyboardCallbackButton(
                    text=t.SELECT_IMAGE_BUTTON,
                    payload={'action': 'finish_congrats'},
                )],
            ])
            used_id_len =len(context["used_id"])
            self.send(
                lyrText(t("SELECTED_PHOTO", photo_id=context["photo_id"],used_id_len=used_id_len)),
                lyText(t.IMAGE_SELECT_TRUE),
                lyrText(t.ICON_CONGRATS),
                keyboard
            )


class MiddleXSelectUp(TelegramBotState):
    @page_view("/bot/guess-rocket-false-up")
    @cs.inject()
    async def handle(self, context) -> None:
        context["upper_limit"]= context.get("photo_id")

        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.NEXT_IMAGE_BUTTON,
                payload={'action': 'next'},
            )],
        ])

        self.send(
            lyText(t.IMAGE_SELECTED_UP),
            lyrText(t.ICON_INDECISION),
            keyboard
        )


class MiddleXSelectDown(TelegramBotState):
    @page_view("/bot/guess-rocket-false-down")
    @cs.inject()
    async def handle(self, context) -> None:
        context["lower_limit"] = context.get("photo_id")

        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.NEXT_IMAGE_BUTTON,
                payload={'action': 'next'},
            )],
        ])
        self.send(
            lyText(t.IMAGE_SELECTED_DOWN),
            lyrText(t.ICON_INDECISION),
            keyboard
        )
