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
COMMANDS_FILE = "../data/btfs_metadata_commands.yml"

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_metadata_add(btfs_handler):
    """
    Test the 'test_btfs_metadata_add ' command.
    """
    # Read the command and parameters from YAML
    # 操作元数据（metadata）的前提条件需要pin
    command_pin_template = btfs_handler.commands['btfs']['btfs_pin_add']
    command_template = btfs_handler.commands['btfs']['btfs_metadata_add']
    key0 = btfs_handler.commands['test_cases'][0]['params']['key0']
    key1 = btfs_handler.commands['test_cases'][0]['params']['key1']
    # 确保 key2 是单行 JSON
    if isinstance(key1, str):
        key1 = json.dumps(json.loads(key1))  # 去除换行符
    elif isinstance(key1, dict):
        key1 = json.dumps(key1)

    # 安全拼接命令
    safe_key1 = shlex.quote(key1)  # 转义特殊字符
    # Execute the command
    btfs_handler.execute_command(command_pin_template, key=key0)
    stdout, stderr = btfs_handler.execute_command(command_template, key0=key0, key1=safe_key1)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if "Hash" not in stdout:
        print("输出不包含 'Hash'，实际输出:", stdout)
    # Assert the command output
    assert "Hash" in stdout

def test_btfs_metadata_rm(btfs_handler):
    """
    Test the 'test_btfs_metadata_rm ' command.
    """
    global metadata_hash
    """
        Test the 'test_btfs_metadata_add ' command.
        """
    # Read the command and parameters from YAML
    # 操作元数据（metadata）的前提条件需要pin
    command_pin_template = btfs_handler.commands['btfs']['btfs_pin_add']
    command_template = btfs_handler.commands['btfs']['btfs_metadata_add']
    key0 = btfs_handler.commands['test_cases'][0]['params']['key0']
    key1 = btfs_handler.commands['test_cases'][0]['params']['key1']
    # 确保 key1 是单行 JSON
    if isinstance(key1, str):
        key1 = json.dumps(json.loads(key1))  # 去除换行符
    elif isinstance(key1, dict):
        key1 = json.dumps(key1)

    # 安全拼接命令
    safe_key1 = shlex.quote(key1)  # 转义特殊字符
    # Execute the command
    btfs_handler.execute_command(command_pin_template, key=key0)
    stdout, stderr = btfs_handler.execute_command(command_template, key0=key0, key1=safe_key1)
    print("stdout: " + stdout)
    # 获取 metadata add的hash
    try:
        # 解析 JSON 获取 Hash
        result = json.loads(stdout)
        metadata_hash = result["Hash"]
        print("成功获取 Hash:", metadata_hash)

        # 可以在这里添加断言验证
        assert metadata_hash.startswith("Qm"), "不是有效的 CIDv0 Hash"

    except json.JSONDecodeError:
        print("错误：stdout 不是有效的 JSON")
        print("原始输出:", stdout)
    print("hash: " + str(metadata_hash))
    if not metadata_hash:
        pytest.fail(f"No Hash found in output: {stdout}")
    command_template = btfs_handler.commands['btfs']['btfs_metadata_rm']
    key = btfs_handler.commands['test_cases'][1]['params']['key']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key0=metadata_hash, key1=key)
    # 查看输出内容是否包含 key
    if "Hash" not in stdout:
        print("输出不包含 'Hash'，实际输出:", stdout)
    # Assert the command output
    assert "Hash" in stdout
