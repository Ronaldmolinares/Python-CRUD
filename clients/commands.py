import click
from tabulate import tabulate

from clients.models import Client
from clients.services import ClientService


@click.group()
def clients():
    """Manages the clients lifecycle."""
    pass


@clients.command()
@click.option("-n", "--name", type=str, prompt=True, help="The client's name")
@click.option("-c", "--company", type=str, prompt=True, help="The client's company")
@click.option("-e", "--email", type=str, prompt=True, help="The client's email")
@click.option("-p", "--position", type=str, prompt=True, help="The client's position")
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client with the provided details."""
    click.echo("Creating client...")
    client = Client(name.title(), company.title(), email, position.title())
    service = ClientService(ctx.obj["clients_table"])
    service.create_client(client)
    click.echo(f"Client {name} created successfully!")


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients."""
    click.echo("Listing clients...")
    service = ClientService(ctx.obj["clients_table"])
    clients = service.list_clients()
    click.echo(
        tabulate(
            [
                (client.uid, client.name, client.company, client.email, client.position)
                for client in clients
            ],
            headers=["UID", "NAME", "COMPANY", "EMAIL", "POSITION"],
        )
    )


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Update an existing client identified by name."""
    click.echo(f"Updating client {client_uid}...")


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Delete a client identified by name."""
    click.echo(f"Deleting client {client_uid}...")
