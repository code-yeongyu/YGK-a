from rich import print as pprint

from .cli_app import cli_app
from .retrieve_stdin import retrieve_stdin


@cli_app.command()
def ygka_command(query: str):
    stdin = retrieve_stdin()
    pprint({'stdin': stdin, 'query': query})
