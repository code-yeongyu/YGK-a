from ygka.models import LanguageModel, YGKAConfigModel


class QueryClientFactory:
    '''Factory for creating query clients.'''

    def __init__(self, config: YGKAConfigModel):
        self.config = config

    def create(self, language_model: LanguageModel):
        '''Create a query client.'''
        if language_model == LanguageModel.REVERSE_ENGINEERED_CHATGPT:
            from .reverse_engineered_chatgpt_client import ReverseEngineeredChatGPTClient
            return ReverseEngineeredChatGPTClient(config=self.config.chatgpt_config)
        elif language_model == LanguageModel.OFFICIAL_CHATGPT:
            from .official_chatgpt_client import OfficialChatGPTClient
            return OfficialChatGPTClient(openai_api_key=self.config.openai_api_key)
        else:
            raise ValueError('Invalid language model.')
