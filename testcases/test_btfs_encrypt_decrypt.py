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
COMMANDS_FILE = project_root / 'data' / 'btfs_encrypt_decrypt.yml'
# 全局变量用于存储加密后的 CID
encrypted_cid = None
encrypted_cid_to = None
encrypted_cid_p = None

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

@pytest.mark.order(1)
def test_btfs_encrypt(btfs_handler):
    global encrypted_cid  # 声明使用全局变量
    """
    Test the 'test_btfs_encrypt' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_encrypt']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']

    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
    print("标准输出1:", stdout)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 提取 CID (更健壮的正则表达式)
    cid_match = re.search(r'(Qm[1-9A-HJ-NP-Za-km-z]{44,})', stdout)
    assert cid_match, "未在输出中找到有效的CID"

    encrypted_cid = cid_match.group(1)
    print(f"提取到的CID: {encrypted_cid}")

    # Assert the command output
    assert "Qm" in stdout

@pytest.mark.order(2)
def test_btfs_decrypt(btfs_handler):
    """
    Test the 'test_btfs_decrypt' command.
    """
    global encrypted_cid
    assert encrypted_cid is not None, "未获取到加密后的 CID"
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_decrypt']
    key1 = btfs_handler.commands['version_path']['value']
    key2 = btfs_handler.commands['BTFS_PATH']['value']

    # Execute the command
    stdout, stderr = btfs_handler.execute_command(
        command_template,
        key1=key1,
        key2=key2,
        key3=encrypted_cid
    )
    print("解密标准输出:", stdout)
    print("解密错误输出:", stderr)

    # 添加更详细的错误输出
    if "sjdklerjjaff" not in stdout:
        print(f"输出不包含 'sjdklerjjaff'，实际输出: {stdout}")
        print(f"使用的CID: {encrypted_cid}")
        print(f"错误输出: {stderr}")
        print(f"stdout: {stdout}")

    # Assert the command output
    assert "sjdklerjjaff" in stdout


@pytest.mark.order(3)
def test_btfs_encrypt_to(btfs_handler):
    global encrypted_cid_to  # 声明使用全局变量
    """
    Test the 'test_btfs_encrypt_to' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_encrypt_to']
    key1 = btfs_handler.commands['version_path']['value']
    key4 = btfs_handler.commands['BTFS_PATH']['value2']

    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key4=key4)
    print("标准输出1:", stdout)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 提取 CID (更健壮的正则表达式)
    cid_match = re.search(r'(Qm[1-9A-HJ-NP-Za-km-z]{44,})', stdout)
    assert cid_match, "未在输出中找到有效的CID"

    encrypted_cid_to = cid_match.group(1)
    print(f"提取到的CID: {encrypted_cid_to}")

    # Assert the command output
    assert "Qm" in stdout


@pytest.mark.order(4)
def test_btfs_decrypt_from(btfs_handler):
    """
    Test the 'test_btfs_decrypt_from' command.
    """
    global encrypted_cid_to
    assert encrypted_cid_to is not None, "未获取到加密后的 CID"
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_decrypt_from']
    key1 = btfs_handler.commands['version_path']['value']
    key4 = btfs_handler.commands['BTFS_PATH']['value2']

    # Execute the command
    stdout, stderr = btfs_handler.execute_command(
        command_template,
        key1=key1,
        key4=key4,
        key5=encrypted_cid_to
    )
    print("解密标准输出:", stdout)
    print("解密错误输出:", stderr)

    # 添加更详细的错误输出
    if "sjdklerjjaff" not in stdout:
        print(f"输出不包含 'sjdklerjjaff'，实际输出: {stdout}")
        print(f"使用的CID: {encrypted_cid_to}")
        print(f"错误输出: {stderr}")
        print(f"stdout: {stdout}")

    # Assert the command output
    assert "sjdklerjjaff" in stdout


@pytest.mark.order(5)
def test_btfs_encrypt_p(btfs_handler):
    global encrypted_cid_p  # 声明使用全局变量
    """
    Test the 'test_btfs_encrypt_p' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_encrypt_p']
    key1 = btfs_handler.commands['version_path']['value']
    key4 = btfs_handler.commands['BTFS_PATH']['value2']

    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key4=key4)
    print("标准输出1:", stdout)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 提取 CID (更健壮的正则表达式)
    cid_match = re.search(r'(Qm[1-9A-HJ-NP-Za-km-z]{44,})', stdout)
    assert cid_match, "未在输出中找到有效的CID"

    encrypted_cid_p = cid_match.group(1)
    print(f"提取到的CID: {encrypted_cid_p}")

    # Assert the command output
    assert "Qm" in stdout

@pytest.mark.order(6)
def test_btfs_decrypt_p(btfs_handler):
    global encrypted_cid_p
    assert encrypted_cid_p is not None, "未获取到加密后的 CID"
    """
    Test the 'test_btfs_decrypt_p' command.
    """
    # Read the command and parameters from YAML
    command_template = btfs_handler.commands['btfs']['btfs_decrypt_p']
    key1 = btfs_handler.commands['version_path']['value']
    key4 = btfs_handler.commands['BTFS_PATH']['value2']

    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key4=key4, key5=encrypted_cid_p)
    print("解密标准输出:", stdout)
    print("解密错误输出:", stderr)

    # 添加更详细的错误输出
    if "sjdklerjjaff" not in stdout:
        print(f"输出不包含 'sjdklerjjaff'，实际输出: {stdout}")
        print(f"使用的CID: {encrypted_cid_p}")
        print(f"错误输出: {stderr}")
        print(f"stdout: {stdout}")

    # Assert the command output
    assert "sjdklerjjaff" in stdout

