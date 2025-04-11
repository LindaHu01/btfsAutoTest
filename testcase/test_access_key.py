
import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
COMMANDS_FILE = "../data/access_key_commands.yml"
global access_key

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_accessKey_generate(btfs_handler):
    """
    Test the 'test_accessKey_generate ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_accesskey_gen']
    print("标准输出:", command_template)
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=None)
    print("标准输出1:", stdout)
    print("标准输出2:", stderr)
    # Assert the command output
    assert "key" in stdout

def test_accessKey_get(btfs_handler):
    """
    Test the 'test_accessKey_get ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_accesskey_get']
    key = btfs_handler.commands['test_cases'][0]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "key" not in stdout:
        print("输出不包含 'key'，实际输出:", stdout)
    # Assert the command output
    assert "key" in stdout

def test_accessKey_list(btfs_handler):
    """
    Test the 'test_accessKey_list ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_accesskey_list']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=None)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "key" not in stdout:
        print("输出不包含 'key'，实际输出:", stdout)
    # Assert the command output
    assert "key" in stdout

def test_accessKey_disable(btfs_handler):
    """
    Test the 'test_accessKey_disable ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_accesskey_disable']
    key = btfs_handler.commands['test_cases'][1]['params']['key']
    print("标准输出1:", key)
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)

def test_accessKey_enable(btfs_handler):
    """
    Test the 'test_accessKey_disable ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_accesskey_enable']
    key = btfs_handler.commands['test_cases'][2]['params']['key']
    print("标准输出1:", key)
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)

def test_accessKey_reset(btfs_handler):
    """
    Test the 'test_accessKey_disable ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_accesskey_reset']
    key = btfs_handler.commands['test_cases'][3]['params']['key']
    print("标准输出1:", key)
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)

# def test_accessKey_delete(btfs_handler):
#     """
#     Test the 'test_accessKey_disable ' command.
#     """
#     # Read the command and parameters from YAML
#     command_template = btfs_handler.commands['btfs']['btfs_accesskey_delete']
#     key = btfs_handler.commands['test_cases'][4]['params']['key']
#     print("标准输出1:", key)
#     # Execute the command
#     stdout, stderr = btfs_handler.execute_command(command_template, key=key)
#     print("标准输出1:", stdout)
#     print("错误输出2:", stderr)




