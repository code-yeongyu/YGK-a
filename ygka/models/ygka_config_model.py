from typing import Optional

from pydantic import BaseModel, root_validator

from .language_model import LanguageModel
from .revchatgpt_chatbot_config_model import RevChatGPTChatbotConfigModel


class YGKAConfigModel(BaseModel):
    language_model: LanguageModel = LanguageModel.REVERSE_ENGINEERED_CHATGPT
    chatgpt_config: Optional[RevChatGPTChatbotConfigModel] = None
    openai_api_key: Optional[str] = None

    @root_validator
    def check_required_info_provided(cls, values: dict[str, Optional[str]]):
        language_model = values.get('language_model')
        if language_model == LanguageModel.REVERSE_ENGINEERED_CHATGPT:
            if not values.get('chatgpt_config'):
                raise ValueError(f'chatgpt_config should not be none if language_model is {language_model}')
        elif language_model == LanguageModel.OFFICIAL_CHATGPT:
            if not values.get('openai_api_key'):
                raise ValueError(f'openai_api_key should not be none if language_model is {language_model}')

        return values
