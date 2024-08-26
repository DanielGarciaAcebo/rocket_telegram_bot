from bernard.i18n import (
    translate as t,
)


from bernard.analytics import page_view
from bernard.engine import BaseState
from bernard.layers import (
    Text as lyrText,
)


class TelegramBotState(BaseState):
    """
    Root class for Telegram Bot.

    Here you must implement "error" and "confused" to suit your needs. They
    are the default functions called when something goes wrong. The ERROR and
    CONFUSED texts are defined in `i18n/en/responses.csv`.
    """

    @page_view("/bot/error")
    async def error(self) -> None:
        """
        This happens when something goes wrong (it's the equivalent of the
        HTTP error 500).
        """
        self.send(lyrText(t.ERROR))

    @page_view("/bot/confused")
    async def confused(self) -> None:
        """
        This is called when the user sends a message that triggers no
        transitions.
        """
        self.send(lyrText(t.CONFUSED))

    async def handle(self) -> None:
        raise NotImplementedError
