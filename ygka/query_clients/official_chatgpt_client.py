import os
from typing import Optional

from revChatGPT.V3 import Chatbot

from ygka.exceptions import UnauthorizedAccessError

from .query_client import QueryClient


class OfficialChatGPTClient(QueryClient):

    def __init__(
        self,
        openai_api_key: Optional[str] = None,
    ):
        OPENAI_API_KEY: Optional[str] = os.environ.get('OPENAI_API_KEY', openai_api_key)
        if OPENAI_API_KEY is None:
            raise UnauthorizedAccessError('OPENAI_API_KEY should not be none')

        self.OPENAI_API_KEY = OPENAI_API_KEY

    def query(self, prompt: str) -> str:
        chatbot = Chatbot(api_key=self.OPENAI_API_KEY)
        response_text = chatbot.ask(prompt)
        return response_text
