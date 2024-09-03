from bernard.platforms.telegram import layers as tll


from ..services import *
from ..baseStates import *

class StartXWelcome(TelegramBotState):
    """
    Welcome the user with inline keyboard options.
    """

    @page_view('/bot/welcome')
    @cs.inject()
    async def handle(self, context) -> None:
        name = await self.request.user.get_friendly_name()
        context["used_ids"] = []
        context["test"] = False

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

class StartXWelcomeTest(TelegramBotState):
    """
    Welcome the user with inline keyboard options.
    """

    @page_view('/bot/welcome-test')
    @cs.inject()
    async def handle(self, context) -> None:
        name = await self.request.user.get_friendly_name()
        context["used_ids"] = []
        context["test"] = True

        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.PLAY_BUTTON_START,
                payload={'action': 'play'},
            )],
        ])

        self.send(
            lyrText(t.TEST_TXT_PRESENTATION),
            lyrText(t.ICON_ROCKET),
            keyboard
        )

class StartXHelp(TelegramBotState):
    """
    Welcome the user with inline keyboard options.
    """

    @page_view('/bot/welcome')
    @cs.inject()
    async def handle(self, context) -> None:
        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.PLAY_BUTTON_START,
                payload={'action': 'back_welcome'},
            )],
            [tll.InlineKeyboardCallbackButton(
                text=t.PLAY_BUTTON_TEST_BOT,
                payload={'action': 'start_text'},
            )],
        ])

        self.send(
            lyrText(t.HELP),
            keyboard
        )

