from domain.cloud_resource import CloudResource
from resources import register

@register("CacheDB")
class CacheDB(CloudResource):
    def validate_config(self):
        if self.config.get("eviction_policy") not in {"LRU", "FIFO"}:
            raise ValueError("Invalid eviction policy.")
        if self.config.get("ttl_seconds", 0) <= 0:
            raise ValueError("ttl_seconds must be positive.")

    def get_details(self):
        return f"{self.name} (ttl={self.config['ttl_seconds']}s, policy={self.config['eviction_policy']})"