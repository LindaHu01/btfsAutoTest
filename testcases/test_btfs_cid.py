from pathlib import Path

import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
project_root = Path(__file__).parent.parent
COMMANDS_FILE = project_root / 'data' / 'btfs_cid_commands.yml'

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_cid_base32(btfs_handler):
    """
    Test the 'test_btfs_cid_base32 ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_cid_base32']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][0]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "bafybei" not in stdout:
        print("输出不包含 'bafybei'，实际输出:", stdout)
    # Assert the command output
    assert "bafybei" in stdout


def test_btfs_cid_bases(btfs_handler):
    """
    Test the 'test_btfs_cid_bases ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_cid_bases']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "base64urlpad" not in stdout:
        print("输出不包含 'base64urlpad'，实际输出:", stdout)
    # Assert the command output
    assert "base64urlpad" in stdout

def test_btfs_cid_codecs(btfs_handler):
    """
    Test the 'test_btfs_cid_codecs ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_cid_codecs']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "json-jcs" not in stdout:
        print("输出不包含 'json-jcs'，实际输出:", stdout)
    # Assert the command output
    assert "json-jcs" in stdout


def test_btfs_cid_format(btfs_handler):
    """
    Test the 'test_btfs_cid_format ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_cid_format']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    key3 = btfs_handler.commands['test_cases'][1]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "Qmaq8oBSDVFHPP4BcRJPHU5Q2ydvtUTFKe28VGspzfeSU8" not in stdout:
        print("输出不包含 'Qmaq8oBSDVFHPP4BcRJPHU5Q2ydvtUTFKe28VGspzfeSU8'，实际输出:", stdout)
    # Assert the command output
    assert "Qmaq8oBSDVFHPP4BcRJPHU5Q2ydvtUTFKe28VGspzfeSU8" in stdout


def test_btfs_hashes(btfs_handler):
    """
    Test the 'test_btfs_hashes ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_cid_hashes']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "blake2s-256" not in stdout:
        print("输出不包含 'blake2s-256'，实际输出:", stdout)
    # Assert the command output
    assert "blake2s-256" in stdout

