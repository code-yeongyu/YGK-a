from typing import Optional

from pydantic import BaseModel, root_validator

from .language_model import LanguageModel


class YGKAConfigModel(BaseModel):
    language_model: LanguageModel = LanguageModel.REVERSE_ENGINEERED_CHATGPT
    browser_name: Optional[str] = None
    openai_api_key: Optional[str] = None

    @root_validator
    def check_required_info_provided(cls, values: dict[str, Optional[str]]):
        language_model = values.get('language_model')
        if language_model == LanguageModel.REVERSE_ENGINEERED_CHATGPT:
            if not values.get('browser_name'):
                raise ValueError(f'browser_name should not be none if language_model is {language_model}')
        elif language_model == LanguageModel.OFFICIAL_CHATGPT:
            if not values.get('openai_api_key'):
                raise ValueError(f'openai_api_key should not be none if language_model is {language_model}')

        return values
