from domain.cloud_resource import CloudResource
from resources import register

@register("AppService")
class AppService(CloudResource):
    VALID_RUNTIMES = {"python", "nodejs", "dotnet"}
    VALID_REGIONS = {"EastUS", "WestEurope", "CentralIndia"}
    VALID_REPLICAS = {1, 2, 3}

    def validate_config(self):
        r = self.config
        if r.get("runtime") not in self.VALID_RUNTIMES:
            raise ValueError("Invalid runtime.")
        if r.get("region") not in self.VALID_REGIONS:
            raise ValueError("Invalid region.")
        if r.get("replica_count") not in self.VALID_REPLICAS:
            raise ValueError("Invalid replica count.")

    def get_details(self):
        return f"{self.name} ({self.config['runtime']} in {self.config['region']})"