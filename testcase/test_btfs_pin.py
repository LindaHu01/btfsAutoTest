import json
import random
import re
import shlex

import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
COMMANDS_FILE = "../data/btfs_pin_commands.yml"

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_pin_add(btfs_handler):
    """
    Test the 'test_btfs_pin_add ' command.
    """
    # Read the command and parameters from YAML
    # 操作元数据（metadata）的前提条件需要pin
    command_pin_template = btfs_handler.commands['btfs']['btfs_pin_add']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][0]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_pin_template, key1=key1, key2=key2, key3=key3)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "pinned" not in stdout:
        print("输出不包含 'pinned'，实际输出:", stdout)
    # Assert the command output
    assert "pinned" in stdout
# def test_btfs_pin_rm(btfs_handler):
#     """
#     Test the 'test_btfs_pin_rm ' command.
#     """
#     # Read the command and parameters from YAML
#     # 操作元数据（metadata）的前提条件需要pin
#     command_pin_template = btfs_handler.commands['btfs']['btfs_pin_rm']
#     key = btfs_handler.commands['test_cases'][1]['params']['key']
#     print("标准输出1:", command_pin_template)
#     print("标准输出2:", key)
#     # Execute the command
#     stdout, stderr = btfs_handler.execute_command(command_pin_template, key=key)
#     print("标准输出1:", stdout)
#     print("错误输出2:", stderr)
#     # 查看输出内容是否包含 key
#     if "unpinned" not in stdout:
#         print("输出不包含 'unpinned'，实际输出:", stdout)
#     # Assert the command output
#     assert "unpinned" in stdout