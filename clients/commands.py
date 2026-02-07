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
@click.option("-u", "--uid", type=str, prompt=True, help="The client's UID to update")
@click.pass_context
def update(ctx, uid):
    """Update an existing client identified by UID."""
    service = ClientService(ctx.obj["clients_table"])
    
    # Verificar si el cliente existe primero
    existing_client = service.get_client_by_uid(uid)
    if not existing_client:
        click.echo(f"Error: Client with UID {uid} not found")
        return
    
    # Si existe, pedir los nuevos datos
    click.echo(f"Updating client {uid}...")
    click.echo("Press Enter to keep current value or type new value:")
    
    name = click.prompt(f"Name [{existing_client.name}]", default=existing_client.name, show_default=False)
    company = click.prompt(f"Company [{existing_client.company}]", default=existing_client.company, show_default=False)
    email = click.prompt(f"Email [{existing_client.email}]", default=existing_client.email, show_default=False)
    position = click.prompt(f"Position [{existing_client.position}]", default=existing_client.position, show_default=False)
    
    updated_client = Client(name.title(), company.title(), email, position.title(), uid)
    service.update_client(updated_client)
    click.echo(f"Client {uid} updated successfully!")


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Delete a client identified by name."""
    click.echo(f"Deleting client {client_uid}...")
