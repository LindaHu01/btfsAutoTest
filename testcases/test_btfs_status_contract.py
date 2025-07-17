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
COMMANDS_FILE = project_root / 'data' / 'btfs_status_contract.yml'

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_status_daily_last_report_time(btfs_handler):
    """
    Test the 'test_btfs_status_daily_last_report_time' command.
    """
    # Read the command and parameters from YAML
    command_rm_template = btfs_handler.commands['btfs']['btfs_status_daily_last_report_time']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key1=key1, key2=key2)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "every_day_seconds" not in stdout:
        print("输出不包含 'every_day_seconds'，实际输出:", stdout)
    # Assert the command output
    assert "every_day_seconds" in stdout

# def test_btfs_status_daily_report_online_server(btfs_handler):
#     """
#     Test the 'test_btfs_status_daily_last_report_time' command.
#     """
#     # Read the command and parameters from YAML
#     command_rm_template = btfs_handler.commands['btfs']['btfs_status_daily_report_online_server']
#     # Execute the command
#     stdout, stderr = btfs_handler.execute_command(command_rm_template, key=None)
#     print("标准输出1:", stdout)
#     print("错误输出2:", stderr)
#     if "success" not in stdout:
#         print("输出不包含 'success'，实际输出:", stdout)
#     # Assert the command output
#     assert "success" in stdout

def test_btfs_status_btfs_daily_total(btfs_handler):
    """
    Test the 'test_btfs_status_btfs_daily_total' command.
    """
    # Read the command and parameters from YAML
    command_rm_template = btfs_handler.commands['btfs']['btfs_status_btfs_daily_total']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key1=key1, key2=key2)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "total_count" not in stdout:
        print("输出不包含 'total_count'，实际输出:", stdout)
    # Assert the command output
    assert "total_count" in stdout

def test_btfs_status_contract_lastinfo (btfs_handler):
    """
    Test the 'test_btfs_status_contract_lastinfo' command.
    """
    # Read the command and parameters from YAML
    command_rm_template = btfs_handler.commands['btfs']['btfs_status_contract_lastinfo']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key1=key1, key2=key2)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "last_signed_info" not in stdout:
        print("输出不包含 'last_signed_info'，实际输出:", stdout)
    # Assert the command output
    assert "last_signed_info" in stdout

def test_btfs_status_contract_report_online_server (btfs_handler):
    """
    Test the 'test_btfs_status_contract_report_online_server' command.
    """
    # Read the command and parameters from YAML
    command_rm_template = btfs_handler.commands['btfs']['btfs_status_contract_report_online_server']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key1=key1, key2=key2)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "ok" not in stdout:
        print("输出不包含 'ok'，实际输出:", stdout)
    # Assert the command output
    assert "ok" in stdout



