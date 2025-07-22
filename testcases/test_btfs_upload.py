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
COMMANDS_FILE = project_root / 'data' / 'btfs_upload.yml'

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_upload(btfs_handler):
    """
    Test the 'test_btfs_upload' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_upload']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][0]['params']['key3']

    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "ID" not in stdout:
        print("输出不包含 'ID'，实际输出:", stdout)
    # Assert the command output
    assert "ID" in stdout


def test_btfs_upload_sp(btfs_handler):
    """
    Test the 'test_btfs_upload_sp' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_upload_sp']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][0]['params']['key3']
    key4 = btfs_handler.commands['test_cases'][0]['params']['key4']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3, key4=key4)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "ID" not in stdout:
        print("输出不包含 'ID'，实际输出:", stdout)
    # Assert the command output
    assert "ID" in stdout


def test_btfs_upload_sp_copy1(btfs_handler):
    """
    Test the 'test_btfs_upload_sp_copy1' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_upload_sp_copy1']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][0]['params']['key3']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
    print("标准输出1:", command_template)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "ID" not in stdout:
        print("输出不包含 'ID'，实际输出:", stdout)
    # Assert the command output
    assert "ID" in stdout


def test_btfs_upload_sp_copy3(btfs_handler):
    """
    Test the 'test_btfs_upload_sp_copy3' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_upload_sp_copy3']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][0]['params']['key3']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
    print("标准输出1:", command_template)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "ID" not in stdout:
        print("输出不包含 'ID'，实际输出:", stdout)
    # Assert the command output
    assert "ID" in stdout

def test_btfs_upload_sp_copy5(btfs_handler):
    """
    Test the 'test_btfs_upload_sp_copy5' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_upload_sp_copy5']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][0]['params']['key3']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
    print("标准输出1:", command_template)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "ID" not in stdout:
        print("输出不包含 'ID'，实际输出:", stdout)
    # Assert the command output
    assert "ID" in stdout

def test_btfs_upload_token_usdd(btfs_handler):
    """
    Test the 'test_btfs_upload_token_usdd' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_upload_token_usdd']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key5 = btfs_handler.commands['test_cases'][0]['params']['key5']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key5=key5)
    print("标准输出1:", command_template)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "ID" not in stdout:
        print("输出不包含 'ID'，实际输出:", stdout)
    # Assert the command output
    assert "ID" in stdout

def test_btfs_upload_token_usdt(btfs_handler):
    """
    Test the 'test_btfs_upload_token_usdt' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_upload_token_usdt']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key6 = btfs_handler.commands['test_cases'][0]['params']['key6']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key6=key6)
    print("标准输出1:", command_template)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "ID" not in stdout:
        print("输出不包含 'ID'，实际输出:", stdout)
    # Assert the command output
    assert "ID" in stdout


