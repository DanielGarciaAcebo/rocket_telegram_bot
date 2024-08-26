from bernard import layers as lyr
from bernard.engine.triggers import BaseTrigger
from .store import cs

class Rocket(BaseTrigger):
    """
    This trigger attempts to interpret the user's input as a number and compares
    it with the number stored in the context. The `is_right` parameter dictates
    whether the trigger should activate when the guess is correct or not.
    """

    def __init__(self, request, is_right: bool) -> None:
        super().__init__(request)
        self.rocket_number = None
        self.is_right = is_right

    @cs.inject()
    async def rank(self, context):
        rocket_number = context.get('rocket_number')

        if rocket_number is None:
            return 0.0

        try:
            self.rocket_number = int(self.request.get_layer(lyr.RawText).text.strip())
        except (KeyError, ValueError, TypeError):
            return None

        is_correct = (rocket_number == self.rocket_number)

        return 1.0 if is_correct == self.is_right else 0.0
