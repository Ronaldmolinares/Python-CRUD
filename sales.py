import click

from clients import commands as client_commands


@click.group()  # agrega un grupo de comandos
@click.pass_context  # pasa el contexto entre comandos
def cli(ctx):
    ctx.obj = {}  # inicializa el objeto de contexto


cli.add_command(
    client_commands.all
)  # agrega los comandos de clientes al grupo principal

if __name__ == "__main__":
    cli()
