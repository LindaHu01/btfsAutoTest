from pathlib import Path

import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
project_root = Path(__file__).parent.parent
COMMANDS_FILE = project_root / 'data' / 'btfs_block_commands.yml'
global access_key

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_block_stat(btfs_handler):
    """
    Test the 'test_btfs_block_stat ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_block_stat']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][0]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "Key" not in stdout:
        print("输出不包含 'Key'，实际输出:", stdout)
    # Assert the command output
    assert "Key" in stdout


def test_btfs_block_get(btfs_handler):
    """
    Test the 'test_btfs_block_get ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_block_get']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][1]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "fj" not in stdout:
        print("输出不包含 'fj'，实际输出:", stdout)
    # Assert the command output
    assert "fj" in stdout


def test_btfs_block_put(btfs_handler):
    """
    Test the 'test_btfs_block_get ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_block_put']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][2]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template,key1=key1, key2=key2, key3=key3)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "Qm" not in stdout:
        print("输出不包含 'Qm'，实际输出:", stdout)
    # Assert the command output
    assert "Qm" in stdout

# def test_btfs_block_rm(btfs_handler):
#     """
#     Test the 'test_btfs_block_get ' command.
#     """
#     # Read the command and parameters from YAML
#     command_template = btfs_handler.commands['btfs']['btfs_block_rm']
#     key = btfs_handler.commands['test_cases'][3]['params']['key']
#     # Execute the command
#     stdout, stderr = btfs_handler.execute_command(command_template, key=key)
#     print("标准输出1:", stdout)
#     print("错误输出2:", stderr)
#     # 查看输出内容是否包含 key
#     if "removed" not in stdout:
#         print("输出不包含 'removed'，实际输出:", stdout)
#     # Assert the command output
#     assert "removed" in stdout





