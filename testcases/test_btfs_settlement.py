import json
import random
import re
import shlex
from pathlib import Path

import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
project_root = Path(__file__).parent.parent
COMMANDS_FILE = project_root / 'data' / 'btfs_settlement_commands.yml'

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_settlement_list(btfs_handler):
    """
    Test the 'test_btfs_settlement_list' command.
    """
    # Read the command and parameters from YAML
    # 操作元数据（metadata）的前提条件需要pin
    command_rm_template = btfs_handler.commands['btfs']['btfs_settlement_list']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key1=key1, key2=key2)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "settlements" not in stdout:
        print("输出不包含 'settlements'，实际输出:", stdout)
    # Assert the command output
    assert "settlements" in stdout
