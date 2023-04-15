from typing import cast

from revChatGPTAuth import get_access_token

from ygka.models import LanguageModel, RevChatGPTChatbotConfigModel, YGKAConfigModel


class QueryClientFactory:
    '''Factory for creating query clients.'''

    def __init__(self, config_model: YGKAConfigModel):
        self.config_model = config_model

    def create(self):
        '''Create a query client.'''
        if self.config_model.language_model == LanguageModel.REVERSE_ENGINEERED_CHATGPT:
            from .reverse_engineered_chatgpt_client import ReverseEngineeredChatGPTClient
            browser_name: str = \
                cast(str, self.config_model.browser_name)  # REVERSE_ENGINEERED_CHATGPT means browser_name is not None
            access_token = get_access_token(browser_name)
            rev_chatgpt_config_model = RevChatGPTChatbotConfigModel(access_token=access_token)
            return ReverseEngineeredChatGPTClient(config=rev_chatgpt_config_model)
        elif self.config_model.language_model == LanguageModel.OFFICIAL_CHATGPT:
            from .official_chatgpt_client import OfficialChatGPTClient
            return OfficialChatGPTClient(openai_api_key=self.config_model.openai_api_key)
        else:
            raise ValueError('Invalid language model.')
