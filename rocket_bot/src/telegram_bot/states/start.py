from bernard.platforms.telegram import layers as tll

from bernard.i18n import  translate as t


from ..baseStates import *

class StartXWelcome(TelegramBotState):
    """
    Welcome the user with inline keyboard options.
    """

    @page_view('/bot/welcome')
    async def handle(self) -> None:
        name = await self.request.user.get_friendly_name()
        rocket = '🚀'

        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.PLAY,
                payload={'action': 'play'},
            )],

            [tll.InlineKeyboardCallbackButton(
                text=t.HELP2,
                payload={'action': 'help'},
            )]
        ])

        self.send(
            lyrText(t("HELLO", name=name)),
            lyrText(rocket),
            keyboard
        )

class StartXHelp(TelegramBotState):
    """
    Welcome the user with inline keyboard options.
    """

    @page_view('/bot/welcome')
    async def handle(self) -> None:
        help_text = t.HELP
        keyboard = tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.OKAY,
                payload={'action': 'back_welcome'},
            )]
        ])

        self.send(
            lyrText(help_text),
            keyboard
        )
