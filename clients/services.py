import csv

from clients.models import Client


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, "r") as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            clients = []
            for row in reader:
                clients.append(
                    Client(
                        name=row["name"],
                        company=row["company"],
                        email=row["email"],
                        position=row["position"],
                        uid=row["uid"],
                    )
                )
            return clients

    def get_client_by_uid(self, uid):
        """Find and return a client by UID, or None if not found."""
        clients = self.list_clients()
        for client in clients:
            if client.uid == uid:
                return client
        return None

    def update_client(self, updated_client):
        clients = self.list_clients()
        found = False
        with open(self.table_name, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            for client in clients:
                if client.uid == updated_client.uid:
                    writer.writerow(updated_client.to_dict())
                    found = True
                else:
                    writer.writerow(client.to_dict())
        return found

    def delete_client(self, uid):
        clients = self.list_clients()
        found = False
        with open(self.table_name, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            for client in clients:
                if client.uid == uid:
                    found = True
                    continue  # Skip writing this client to effectively delete it
                writer.writerow(client.to_dict())
        return found
