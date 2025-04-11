import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
COMMANDS_FILE = "../data/btfs_add_commands.yml"


@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_add(btfs_handler):
    """
    Test the 'btfs add' command.
    """
    # Start the BTFS daemon
    # btfs_handler.start_daemon()

    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_add']
    key = btfs_handler.commands['test_cases'][0]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key)
    print("标准输出:", stdout)
    # Assert the command output
    assert "added" in stdout

def test_btfs_add_r(btfs_handler):
    """
    Test the 'btfs add' command.
    """
    # Start the BTFS daemon
    # btfs_handler.start_daemon()

    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_add_r']
    key = btfs_handler.commands['test_cases'][1]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key)
    print("标准输出:", stdout)
    # Assert the command output
    assert "added" in stdout