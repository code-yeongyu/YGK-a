from rich import print as pprint

from .cli_app import cli_app


@cli_app.command()
def ygka_command():
    pprint('[bold]Hello World![/bold]')
