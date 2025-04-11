import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
COMMANDS_FILE = "../data/btfs_bootstrap_commands.yml"
global access_key

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_bootstrap_add(btfs_handler):
    """
    Test the 'test_btfs_bootstrap_add ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_bootstrap_add']
    key = btfs_handler.commands['test_cases'][0]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "added" not in stdout:
        print("输出不包含 'added'，实际输出:", stdout)
    # Assert the command output
    assert "added" in stdout


def test_btfs_bootstrap_add_default(btfs_handler):
    """
    Test the 'test_btfs_bootstrap_add_default ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_bootstrap_add_default']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=None)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "added" not in stdout:
        print("输出不包含 'added'，实际输出:", stdout)
    # Assert the command output
    assert "added" in stdout


def test_btfs_bootstrap_list(btfs_handler):
    """
    Test the 'test_btfs_bootstrap_list ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_bootstrap_list']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=None)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "/ip4" not in stdout:
        print("输出不包含 '/ip4'，实际输出:", stdout)
    # Assert the command output
    assert "/ip4" in stdout




