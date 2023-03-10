import pytest
from yt_dlp.cookies import SUPPORTED_BROWSERS

from ygka.adapters import OpenAICookieAdapter


class TestChatGPTAccessTokenAdapterInit:

    def test_fail_when_invalid_browser_name_is_given(self) -> None:
        '''잘못된 브라우저 이름을 입력했을 때 ValueError가 발생한다.'''
        with pytest.raises(ValueError):
            OpenAICookieAdapter('invalid_browser_name')

    @pytest.mark.parametrize('browser_name', SUPPORTED_BROWSERS)
    def test_success_when_valid_browser_name_is_given(self, browser_name: str) -> None:
        '''올바른 브라우저 이름을 입력했을 때 ValueError가 발생하지 않는다'''
        OpenAICookieAdapter(browser_name)
