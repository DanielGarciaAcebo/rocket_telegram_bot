from bernard.platforms.telegram import layers as tll


from ..services import *
from ..baseStates import *

class StartXWelcome(TelegramBotState):

    @page_view('/bot/welcome')
    @cs.inject()
    async def handle(self, context) -> None:
        name = await self.request.user.get_friendly_name()
        context["lower_limit"] = 1
        context["upper_limit"] = 123
        context["used_id"]= []

        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.PLAY_BUTTON_START,
                payload={'action': 'play'},
            )],

            [tll.InlineKeyboardCallbackButton(
                text=t.HELP_BUTTON_START,
                payload={'action': 'help'},
            )]
        ])

        self.send(
            lyrText(t("HELLO", name=name)),
            lyrText(t.ICON_ROCKET),
            keyboard
        )


class StartXHelp(TelegramBotState):
    @page_view('/bot/welcome')
    @cs.inject()
    async def handle(self, context) -> None:
        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.PLAY_BUTTON_START,
                payload={'action': 'back_welcome'},
            )],
        ])

        self.send(
            lyrText(t.HELP),
            keyboard
        )

