from .cli import cli_app
from .cli.retrieve_stdin import retrieve_stdin as retrieve_stdin
from .models.ygka_config_model import YGKAConfigModel as YGKAConfigModel
from .utils.ygka_config_manager import YGKAConfigManager as YGKAConfigManager


def main():
    cli_app()
