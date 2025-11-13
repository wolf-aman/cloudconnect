from domain.cloud_resource import CloudResource
from resources import register

@register("StorageAccount")
class StorageAccount(CloudResource):
    def validate_config(self):
        if not isinstance(self.config.get("encryption_enabled"), bool):
            raise ValueError("encryption_enabled must be bool.")
        if len(self.config.get("access_key", "")) < 8:
            raise ValueError("access_key must be at least 8 characters.")
        if not isinstance(self.config.get("max_size_gb"), int):
            raise ValueError("max_size_gb must be int.")

    def get_details(self):
        return f"{self.name} (encrypted={self.config['encryption_enabled']}, size={self.config['max_size_gb']}GB)"
