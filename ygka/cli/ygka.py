from typing import Optional

import rich
import typer
from rich.console import Console

from ygka.models import LanguageModel
from ygka.query_clients import QueryClientFactory
from ygka.utils import YGKAConfigManager

from .cli_app import cli_app
from .config_ygka import config_ygka
from .retrieve_stdin import retrieve_stdin


@cli_app.command()
def ygka_command(query: str, language_model: Optional[LanguageModel] = None):
    stdin = retrieve_stdin()

    config_manager = _get_config_manager()
    config_manager.config_model.language_model = language_model or config_manager.config_model.language_model

    query_client = QueryClientFactory(config_model=config_manager.config_model).create()

    console = Console()
    try:
        with console.status('''[green] YGKA is waiting for ChatGPT's answer ...[/green]'''):
            prompt = _generate_prompt(stdin, query)
            response = query_client.query(prompt)
            console.print(response)
    except KeyError:
        rich.print('It looks like the `session_token` is expired. Please reconfigure YGKA.')
        typer.confirm('Reconfigure YGKA?', abort=True)
        config_ygka()
        ygka_command(query=query, language_model=language_model)
        typer.Exit()


def _get_config_manager():
    is_config_file_available = YGKAConfigManager.is_config_file_available(YGKAConfigManager.DEFAULT_CONFIG_PATH)
    if is_config_file_available:
        return YGKAConfigManager(load_config=True)
    else:
        return config_ygka()


def _generate_prompt(stdin: Optional[str], prompt: str) -> str:
    if stdin:
        return f'''
stdin:
{stdin}

prompt:
{prompt}

[system] don't mention that i gave you in a format of stdin and prompt
'''[1:]
    else:
        return prompt
