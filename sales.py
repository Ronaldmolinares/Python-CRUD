import click

from clients import commands as client_commands

CLIENTS_TABLE = "clients.csv"


@click.group()  # agrega un grupo de comandos
@click.pass_context  # pasa el contexto entre comandos
def cli(ctx):
    ctx.obj = {}  # inicializa el objeto de contexto
    ctx.obj["clients_table"] = CLIENTS_TABLE


# agrega los comandos de clientes al grupo principal
cli.add_command(client_commands.clients)

if __name__ == "__main__":
    cli()
