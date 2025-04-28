import random

import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
COMMANDS_FILE = "../data/btfs_key_commands.yml"

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_key_gen(btfs_handler):
    """
    Test the 'test_btfs_key_gen ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_key_gen']
    # 生成随机的三位数字
    random_number = random.randint(100, 999999)
    key = btfs_handler.commands['test_cases'][0]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=key+str(random_number))
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "k51" not in stdout:
        print("输出不包含 'k51'，实际输出:", stdout)
    # Assert the command output
    assert "k51" in stdout

def test_btfs_key_list(btfs_handler):
    """
    Test the 'test_btfs_key_list ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_key_list']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=None)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "mykey" not in stdout:
        print("输出不包含 'mykey'，实际输出:", stdout)
    # Assert the command output
    assert "mykey" in stdout


def test_btfs_key_rename(btfs_handler):
    """
    Test the 'test_btfs_key_rename ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_key_rename']
    key = btfs_handler.commands['test_cases'][1]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key0='mykeyname',key1=key)
    # 查看输出内容是否包含 key
    if "renamed" not in stdout:
        print("输出不包含 'renamed'，实际输出:", stdout)
    # Assert the command output
    assert "renamed" in stdout

def test_btfs_key_rm(btfs_handler):
    """
    Test the 'test_btfs_key_rm ' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_key_list']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=None)
    # 假设 stdout 是一个字符串
    first_key = stdout.splitlines()[2]
    # 假设 stdout 是一个列表
    # first_key = stdout[2]
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_key_rm']
    print("first:", str(first_key))
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key=str(first_key))
    print("执行结果:", stdout)
    # 查看输出内容是否包含 key
    if str(first_key) not in stdout:
        print("输出不包含"+ str(first_key)+" 实际输出:", stdout)
    # Assert the command output
    assert str(first_key) in stdout


