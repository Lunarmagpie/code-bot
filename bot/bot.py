import crescent
from bot.config import CONFIG


class CodeBot(crescent.Bot):
    def __init__(self):
        super().__init__(token=CONFIG.token)

        self.plugins.load("bot.plugins.eval")
