# CloudConnect

CloudConnect is a modular and extensible system for managing cloud resources. It provides a CLI-based interface to create, start, stop, delete, and manage various cloud resources such as App Services, Storage Accounts, and Cache Databases.

## Features

- **Resource Management**: Create, start, stop, delete, and list cloud resources.
- **Extensibility**: Easily add new resource types using the `@register` decorator.
- **State Management**: Resources follow a lifecycle with states like `created`, `started`, `stopped`, and `deleted`.
- **Logging**: Logs all resource operations for auditing and debugging.
- **Factory Pattern**: Uses a factory pattern for resource creation.
- **Decorator Pattern**: Adds logging functionality to resource operations.

## Project Structure

```
CloudConnect/
├── application/
│   └── resource_manager.py  # Facade for managing resources
├── cloudconnect/
│   ├── __init__.py          # Package initialization
│   └── main.py              # CLI entry point
├── core/
│   ├── __init__.py          # Package initialization
│   ├── decorator.py         # Logging decorator for resources
│   └── factory.py           # Factory for creating resources
├── domain/
│   ├── __init__.py          # Package initialization
│   ├── cloud_resource.py    # Abstract base class for resources
│   └── state.py             # State pattern implementation
├── resources/
│   ├── __init__.py          # Resource registry
│   ├── app_service.py       # AppService resource
│   ├── cache_db.py          # CacheDB resource
│   └── storage_account.py   # StorageAccount resource
├── utils/
│   ├── __init__.py          # Package initialization
│   └── logger_utils.py      # Utility for logging
└── run_cloudconnect.py      # Script to run the CLI
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Ensure you have the required permissions to create directories and files for logging.

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CloudConnect
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the CLI:
   ```bash
   python run_cloudconnect.py
   ```

2. Follow the on-screen instructions to manage resources.

### Example Workflows

#### Create a Resource

1. Select the resource type (e.g., AppService, StorageAccount, CacheDB).
2. Provide the required configuration (e.g., runtime, region, encryption settings).
3. The resource will be created and logged.

#### Start, Stop, or Delete a Resource

1. Choose the operation from the main menu.
2. Select the resource by name.
3. The operation will be performed, and the state will be updated.

#### View Logs

1. Select "View Logs" from the main menu.
2. Choose a specific log file or view all logs.

## Adding New Resource Types

1. Create a new file in the `resources` directory.
2. Define a class that inherits from `CloudResource`.
3. Implement the `validate_config` and `get_details` methods.
4. Use the `@register` decorator to register the resource.

Example:
```python
from domain.cloud_resource import CloudResource
from resources import register

@register("NewResource")
class NewResource(CloudResource):
    def validate_config(self):
        # Validate configuration
        pass

    def get_details(self):
        # Return resource details
        return "Details about NewResource"
```

## Logs

Logs are stored in the `cloudconnect/logs` directory. Each resource has its own log file, which records all operations performed on it.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.