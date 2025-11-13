from application.resource_manager import ResourceManager
from core.factory import AppResourceFactory
from resources.app_service import AppService
from resources.storage_account import StorageAccount
from resources.cache_db import CacheDB
import os

def cli_main():
    """Main CLI entry point with improved UX."""
    manager = ResourceManager(factory=AppResourceFactory, use_decorator=True)

    print("\nWelcome to CloudConnect CLI")
    print("=" * 50)
    
    while True:
        try:
            _display_main_menu()
            choice = input("\nEnter choice (1-7): ").strip()

            if choice == "1":
                _create_resource_workflow(manager)
            elif choice == "2":
                _start_resource_workflow(manager)
            elif choice == "3":
                _stop_resource_workflow(manager)
            elif choice == "4":
                _delete_resource_workflow(manager)
            elif choice == "5":
                _view_logs()
            elif choice == "6":
                _list_resources_workflow(manager)
            elif choice == "7":
                print("\nExiting CloudConnect. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-7.")
                
        except KeyboardInterrupt:
            print("\n\nExiting CloudConnect. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

def _display_main_menu():
    """Display the main menu with better formatting."""
    print("\n" + "=" * 50)
    print("Main Menu:")
    print("-" * 20)
    print("1. Create Resource")
    print("2. Start Resource")
    print("3. Stop Resource")
    print("4. Delete Resource")
    print("5. View Logs")
    print("6. List Resources")
    print("7. Exit")

def _create_resource_workflow(manager):
    """Improved resource creation workflow."""
    print("\nCreate New Resource")
    print("-" * 25)
    print("Select resource type:")
    print("1. AppService (Web Applications)")
    print("2. StorageAccount (Data Storage)")
    print("3. CacheDB (Fast Data Access)")
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice not in ["1", "2", "3"]:
        print("Invalid choice. Please select 1, 2, or 3.")
        return
    
    name = _get_resource_name()
    if not name:
        return
    
    try:
        if choice == "1":
            config = _config_app_service()
            result = manager.create_resource("AppService", name, config)
        elif choice == "2":
            config = _config_storage_account()
            result = manager.create_resource("StorageAccount", name, config)
        elif choice == "3":
            config = _config_cache_db()
            result = manager.create_resource("CacheDB", name, config)
        
        print(f"\n{result}")
        
    except Exception as e:
        print(f"Creation failed: {e}")

def _get_resource_name() -> str:
    """Get and validate resource name."""
    while True:
        name = input("Enter resource name: ").strip()
        if len(name) == 0:
            print("Resource name cannot be empty.")
            continue
        if len(name) > 50:
            print("Resource name cannot exceed 50 characters.")
            continue
        return name

def _config_app_service():
    """Configure AppService with validation."""
    print("\nAvailable runtimes: python, nodejs, dotnet")
    while True:
        runtime = input("Runtime (python/nodejs/dotnet): ").strip().lower()
        if runtime in ["python", "nodejs", "dotnet"]:
            break
        print("Invalid runtime. Please choose: python, nodejs, or dotnet")
    
    print("Available regions: EastUS, WestEurope, CentralIndia")
    while True:
        region = input("Region (EastUS/WestEurope/CentralIndia): ").strip()
        if region in ["EastUS", "WestEurope", "CentralIndia"]:
            break
        print("Invalid region. Please choose: EastUS, WestEurope, or CentralIndia")
    
    while True:
        try:
            replica = int(input("Replica count (1/2/3): ").strip())
            if replica in [1, 2, 3]:
                break
            print("Invalid replica count. Please choose: 1, 2, or 3")
        except ValueError:
            print("Please enter a valid number (1, 2, or 3)")
    
    return {"runtime": runtime, "region": region, "replica_count": replica}

def _config_storage_account():
    """Configure StorageAccount with validation."""
    while True:
        enc_input = input("Encryption enabled? (y/n): ").strip().lower()
        if enc_input in ['y', 'n', 'yes', 'no']:
            enc = enc_input in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no")
    
    while True:
        access_key = input("Access key (min 8 chars): ").strip()
        if len(access_key) >= 8:
            break
        print("Access key must be at least 8 characters long")
    
    while True:
        try:
            max_size = int(input("Max size (GB): ").strip())
            if max_size > 0:
                break
            print("Size must be a positive number")
        except ValueError:
            print("Please enter a valid positive number")
    
    return {"encryption_enabled": enc, "access_key": access_key, "max_size_gb": max_size}

def _config_cache_db():
    """Configure CacheDB with validation."""
    while True:
        try:
            ttl = int(input("TTL seconds: ").strip())
            if ttl > 0:
                break
            print("TTL must be a positive number")
        except ValueError:
            print("Please enter a valid positive number")
    
    while True:
        try:
            cap = int(input("Capacity (MB): ").strip())
            if cap > 0:
                break
            print("Capacity must be a positive number")
        except ValueError:
            print("Please enter a valid positive number")
    
    while True:
        evict = input("Eviction policy (LRU/FIFO): ").strip().upper()
        if evict in ["LRU", "FIFO"]:
            break
        print("Invalid eviction policy. Please choose: LRU or FIFO")
    
    return {"ttl_seconds": ttl, "capacity_mb": cap, "eviction_policy": evict}

def _start_resource_workflow(manager):
    """Improved start resource workflow."""
    resources = manager.list_resources()
    if not resources:
        print("No resources available to start.")
        return
    
    print("\nStart Resource")
    print("-" * 18)
    _show_available_resources(resources)
    
    name = input("Enter resource name to start: ").strip()
    if name:
        try:
            result = manager.start_resource(name)
            print(f"\n{result}")
        except Exception as e:
            print(f"Error: {e}")

def _stop_resource_workflow(manager):
    """Improved stop resource workflow."""
    resources = manager.list_resources()
    if not resources:
        print("No resources available to stop.")
        return
    
    print("\nStop Resource")
    print("-" * 17)
    _show_available_resources(resources)
    
    name = input("Enter resource name to stop: ").strip()
    if name:
        try:
            result = manager.stop_resource(name)
            print(f"\n{result}")
        except Exception as e:
            print(f"Error: {e}")

def _delete_resource_workflow(manager):
    """Improved delete resource workflow."""
    resources = manager.list_resources()
    if not resources:
        print("No resources available to delete.")
        return
    
    print("\nDelete Resource")
    print("-" * 19)
    _show_available_resources(resources)
    
    name = input("Enter resource name to delete: ").strip()
    if name:
        confirm = input(f"Are you sure you want to delete '{name}'? (y/N): ").strip().lower()
        if confirm == 'y':
            try:
                result = manager.delete_resource(name)
                print(f"\n{result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Deletion cancelled.")

def _show_available_resources(resources):
    """Show available resources in a formatted way, excluding deleted ones."""
    active_resources = {name: meta for name, meta in resources.items() if not meta.get('deleted', False)}
    
    if not active_resources:
        print("No active resources available.")
        return
    
    print("Available resources:")
    for name, meta in active_resources.items():
        if meta['status'] == 'started':
            status = "[RUNNING]"
        elif meta['status'] == 'stopped':
            status = "[STOPPED]"
        else:
            status = "[CREATED]"
        print(f"  {status} {name} ({meta['type']}) - {meta['status']}")

def _list_resources_workflow(manager):
    """Enhanced resource listing with statistics."""
    resources = manager.list_resources()
    counts = manager.get_resource_count()
    
    print("\nResource Overview")
    print("-" * 22)
    print(f"Total Resources: {counts['total']}")
    
    if counts['total'] > 0:
        print("\nBy Type:")
        for resource_type, count in counts.get('by_type', {}).items():
            print(f"  {resource_type}: {count}")
        
        print("\nBy Status:")
        for status, count in counts.get('by_status', {}).items():
            print(f"  {status.upper()}: {count}")
        
        # Separate active and deleted resources
        active_resources = {}
        deleted_resources = {}
        
        for name, meta in resources.items():
            if meta.get('deleted', False):
                deleted_resources[name] = meta
            else:
                active_resources[name] = meta
        
        if active_resources:
            print("\nActive Resources:")
            for name, meta in active_resources.items():
                if meta['status'] == 'started':
                    status = "[RUNNING]"
                elif meta['status'] == 'stopped':
                    status = "[STOPPED]"
                else:
                    status = "[CREATED]"
                print(f"  {status} {name}")
                print(f"    Type: {meta['type']}, Status: {meta['status']}")
                print(f"    Details: {meta['details']}")
        
        if deleted_resources:
            print("\nDeleted Resources:")
            for name, meta in deleted_resources.items():
                print(f"  [DELETED] {name}")
                print(f"    Type: {meta['type']}, Status: {meta['status']}")
                print(f"    Details: {meta['details']}")
    else:
        print("No resources found. Create some resources first!")

def _view_logs():
    """Enhanced log viewing with better organization."""
    logs_dir = os.path.join("cloudconnect", "logs")
    if not os.path.exists(logs_dir):
        print("No logs directory found.")
        return
    
    files = [f for f in os.listdir(logs_dir) if f.endswith('.log')]
    if not files:
        print("No logs found.")
        return
    
    print(f"\nFound {len(files)} log files:")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")
    
    choice = input("\nEnter log file number to view (or 'all' for all logs): ").strip().lower()
    
    if choice == 'all':
        for f in sorted(files):
            print(f"\n{'='*60}")
            print(f"Logs for {f}")
            print(f"{'='*60}")
            try:
                with open(os.path.join(logs_dir, f), 'r', encoding='utf-8') as file:
                    content = file.read().strip()
                    if content:
                        print(content)
                    else:
                        print("No log entries found.")
            except Exception as e:
                print(f"Error reading log file: {e}")
    else:
        try:
            file_index = int(choice) - 1
            if 0 <= file_index < len(files):
                selected_file = files[file_index]
                print(f"\n{'='*60}")
                print(f"Logs for {selected_file}")
                print(f"{'='*60}")
                with open(os.path.join(logs_dir, selected_file), 'r', encoding='utf-8') as file:
                    content = file.read().strip()
                    if content:
                        print(content)
                    else:
                        print("No log entries found.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number or 'all'.")
        except Exception as e:
            print(f"Error reading log file: {e}")
