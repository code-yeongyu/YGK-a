import sys

import rich
import typer
from revChatGPTAuth import SupportedBrowser

from ygka.models.ygka_config_model import YGKAConfigModel
from ygka.utils import YGKAConfigManager


def config_ygka():
    SUPPORTED_BROWSERS = [browser.value for browser in SupportedBrowser]
    rich.print('''
Hi! 🙌 I am [bold blue]YGKA[/bold blue]!
[yellow][blue bold underline]Y[/blue bold underline]our
[blue bold underline]G[/blue bold underline]enius,
[blue bold underline]K[/blue bold underline]nowledgeable assistant
[blue bold underline]A[/blue bold underline]n advanced ChatGPT client[/yellow] 🔥
I am here to assist you with configuring YGKA. 💪

Please make sure that you have logged into chat.openai.com on your browser before we continue. 🗝️

'''[1:])
    typer.confirm('Are you ready to proceed? 🚀', abort=True)

    rich.print(f'''
Which browser did you use to log in to chat.openai.com?

We support the following browsers: [{SUPPORTED_BROWSERS}]'''[1:])
    browser_name = typer.prompt('Please enter your choice here: ')
    if browser_name not in SUPPORTED_BROWSERS:
        rich.print(f'Browser {browser_name} is not supported. Supported browsers are: {SUPPORTED_BROWSERS}')
        sys.exit(1)

    config_manager = save_config(browser_name)

    rich.print(f'''
[green bold]Excellent![/green bold] You are now ready to use [bold blue]YGKA[/bold blue] 🚀

Enjoy your AI powered terminal assistant! 🎉

[dim]To check your settings file, it's at: {config_manager.config_path}[/dim]

'''[1:])
    return config_manager


def save_config(browser_name: str):
    config_manager: YGKAConfigManager = YGKAConfigManager()

    is_config_file_available = YGKAConfigManager.is_config_file_available(YGKAConfigManager.DEFAULT_CONFIG_PATH)
    if is_config_file_available:
        config_manager = YGKAConfigManager(load_config=True)
        config_manager.config_model.browser_name = browser_name
    else:
        YGKA_config = YGKAConfigModel(browser_name=browser_name)
        config_manager = YGKAConfigManager(config_model=YGKA_config)

    config_manager.save_config()
    return config_manager
