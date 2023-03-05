from ygka.models import LanguageModel, YGKAConfigModel


class QueryClientFactory:
    '''Factory for creating query clients.'''

    def __init__(self, config_model: YGKAConfigModel):
        self.config_model = config_model

    def create(self):
        '''Create a query client.'''
        if self.config_model.language_model == LanguageModel.REVERSE_ENGINEERED_CHATGPT:
            from .reverse_engineered_chatgpt_client import ReverseEngineeredChatGPTClient
            return ReverseEngineeredChatGPTClient(config=self.config_model.chatgpt_config)
        elif self.config_model.language_model == LanguageModel.OFFICIAL_CHATGPT:
            from .official_chatgpt_client import OfficialChatGPTClient
            return OfficialChatGPTClient(openai_api_key=self.config_model.openai_api_key)
        else:
            raise ValueError('Invalid language model.')
