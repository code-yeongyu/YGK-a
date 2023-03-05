import os
from typing import Optional, Union, cast

from revChatGPT.V1 import Chatbot

from ygka.exceptions import UnauthorizedAccessError
from ygka.models import RevChatGPTChatbotConfigModel

from .query_client import QueryClient


class ReverseEngineeredChatGPTClient(QueryClient):
    _config: RevChatGPTChatbotConfigModel

    @property
    def revchatgpt_config(self) -> dict[str, Union[str, bool]]:
        return self._config.dict(exclude_none=True)

    def __init__(
        self,
        config: Optional[RevChatGPTChatbotConfigModel] = None,
        access_token: Optional[str] = None,
        session_token: Optional[str] = None,
    ):
        if config:
            self._config = config
        else:
            CHATGPT_ACCESS_TOKEN = os.environ.get('CHATGPT_ACCESS_TOKEN', access_token)
            CHATGPT_SESSION_TOKEN = os.environ.get('CHATGPT_SESSION_TOKEN', session_token)
            if CHATGPT_ACCESS_TOKEN:
                self._config = RevChatGPTChatbotConfigModel(access_token=CHATGPT_ACCESS_TOKEN)
            elif CHATGPT_SESSION_TOKEN:
                self._config = RevChatGPTChatbotConfigModel(session_token=CHATGPT_SESSION_TOKEN)
            else:
                raise UnauthorizedAccessError('No access token or session token provided.')

    def query(self, prompt: str) -> str:
        chatbot = Chatbot(config=self.revchatgpt_config)  #  pyright: ignore [reportGeneralTypeIssues]
        # ignore for wrong type hint of revchatgpt

        response_text = ''
        for data in chatbot.ask(prompt):
            response_text = data['message']

        response_text = cast(str, response_text)
        return response_text
