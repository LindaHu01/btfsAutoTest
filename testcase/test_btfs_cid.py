import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
COMMANDS_FILE = "../data/btfs_cid_commands.yml"

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
    key = btfs_handler.commands['test_cases'][0]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "bafybeify4" not in stdout:
        print("输出不包含 'bafybeify4'，实际输出:", stdout)
    # Assert the command output
    assert "bafybeify4" in stdout


def test_btfs_cid_bases(btfs_handler):
    """
    Test the 'test_btfs_cid_bases ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_cid_bases']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=None)
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
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=None)
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
    key = btfs_handler.commands['test_cases'][1]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "QmanM91RNzhU3Wr4md1ugknMhhhG4CuLWfV5UjYCtA3v31" not in stdout:
        print("输出不包含 'QmanM91RNzhU3Wr4md1ugknMhhhG4CuLWfV5UjYCtA3v31'，实际输出:", stdout)
    # Assert the command output
    assert "QmanM91RNzhU3Wr4md1ugknMhhhG4CuLWfV5UjYCtA3v31" in stdout


def test_btfs_hashes(btfs_handler):
    """
    Test the 'test_btfs_hashes ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_cid_hashes']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=None)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "blake2s-256" not in stdout:
        print("输出不包含 'blake2s-256'，实际输出:", stdout)
    # Assert the command output
    assert "blake2s-256" in stdout

