import click


@click.group()
def clients():
    """Manages the clients lifecycle."""
    pass


@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client with the provided details."""
    client = {
        "name": name,
        "company": company,
        "email": email.lower(),
        "position": position,
    }
    # Aquí iría la lógica para guardar el cliente en la base de datos o archivo
    click.echo(f"Client {client['name']} created successfully.")


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients."""
    click.echo("Listing all clients...")


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


all = clients
