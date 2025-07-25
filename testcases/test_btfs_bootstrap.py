from pathlib import Path

import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
project_root = Path(__file__).parent.parent
COMMANDS_FILE = project_root / 'data' / 'btfs_bootstrap_commands.yml'
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
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][0]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
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
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
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
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "/ip4" not in stdout:
        print("输出不包含 '/ip4'，实际输出:", stdout)
    # Assert the command output
    assert "/ip4" in stdout

# def test_btfs_bootstrap_rm(btfs_handler):
#     """
#     Test the 'test_btfs_bootstrap_rm ' command.
#     """
#     # Read the command and parameters from YAML
#     command_template = btfs_handler.commands['btfs']['btfs_bootstrap_rm']
#     key = btfs_handler.commands['test_cases'][1]['params']['key']
#     # Execute the command
#     stdout, stderr = btfs_handler.execute_command(command_template, key=key)
#     print("标准输出1:", stdout)
#     print("错误输出2:", stderr)
#     # 查看输出内容是否包含 key
#     if "removed" not in stdout:
#         print("输出不包含 'removed'，实际输出:", stdout)
#     # Assert the command output
#     assert "removed" in stdout

# def test_btfs_bootstrap_rm_all(btfs_handler):
#     """
#     Test the 'test_btfs_bootstrap_rm_all ' command.
#     """
#     # Read the command and parameters from YAML
#     command_template = btfs_handler.commands['btfs']['btfs_bootstrap_rm_all']
#     # Execute the command
#     stdout, stderr = btfs_handler.execute_command(command_template, key=None)
#     print("标准输出1:", stdout)
#     print("错误输出2:", stderr)
#     # 查看输出内容是否包含 key
#     if "removed" not in stdout:
#         print("输出不包含 'removed'，实际输出:", stdout)
#     # Assert the command output
#     assert "removed" in stdout



