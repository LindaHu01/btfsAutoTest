
import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
COMMANDS_FILE = "../data/version_path.yml"
global access_key

@pytest.fixture(autouse=True)
def btfs_handler(COMMANDS_FILE):
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def go_version_path(btfs_handler):
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['version_path']
    print("标准输出:", command_template)
    key = btfs_handler.commands['version_path']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key)