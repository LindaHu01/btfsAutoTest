import json
import random
import re
import shlex
from pathlib import Path

import allure
import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
project_root = Path(__file__).parent.parent
COMMANDS_FILE = project_root / 'data' / 'btfs_metadata_commands.yml'

@allure.suite("BTFS Metadata Tests")
class TestBtfsMetadata:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    @allure.story("BTFS Metadata add")
    @allure.title("test_btfs_metadata_add")
    def test_btfs_metadata_add(self, btfs_handler):
        """
        Test the 'test_btfs_metadata_add ' command.
        """
        # Read the command and parameters from YAML
        # 操作元数据（metadata）的前提条件需要pin
        with allure.step("Prepare command parameters"):
            command_pin_template = btfs_handler.commands['btfs']['btfs_pin_add']
            command_template = btfs_handler.commands['btfs']['btfs_metadata_add']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key0']
            key4 = btfs_handler.commands['test_cases'][0]['params']['key1']
            # 确保 key2 是单行 JSON
            if isinstance(key4, str):
                key4 = json.dumps(json.loads(key4))  # 去除换行符
            elif isinstance(key4, dict):
                key4 = json.dumps(key4)

            # 安全拼接命令
            safe_key4 = shlex.quote(key4)  # 转义特殊字符
        # Execute the command
        with allure.step("Execute command"):
            btfs_handler.execute_command(command_pin_template, key1=key1, key2=key2, key3=key3)
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3, key4=safe_key4)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            # 查看输出内容是否包含 key
            if "Hash" not in stdout:
                print("输出不包含 'Hash'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "Hash" in stdout

    @allure.story("BTFS metadata rm")
    @allure.title("test_btfs_metadata_rm")
    def test_btfs_metadata_rm(self, btfs_handler):
        """
        Test the 'test_btfs_metadata_rm ' command.
        """
        global metadata_hash
        """
            Test the 'test_btfs_metadata_add ' command.
            """
        # Read the command and parameters from YAML
        # 操作元数据（metadata）的前提条件需要pin
        with allure.step("Prepare command parameters"):
            command_pin_template = btfs_handler.commands['btfs']['btfs_pin_add']
            command_template = btfs_handler.commands['btfs']['btfs_metadata_add']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key0']
            key4 = btfs_handler.commands['test_cases'][0]['params']['key1']
            # 确保 key4 是单行 JSON
            if isinstance(key4, str):
                key4 = json.dumps(json.loads(key4))  # 去除换行符
            elif isinstance(key4, dict):
                key4 = json.dumps(key4)

            # 安全拼接命令
            safe_key4 = shlex.quote(key4)  # 转义特殊字符
        # Execute the command
        with allure.step("Execute command"):
            btfs_handler.execute_command(command_pin_template, key1=key1, key2=key2, key3=key3)
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3, key4=safe_key4)
            print("stdout: " + stdout)
            # 获取 metadata add的hash
            try:
                # 解析 JSON 获取 Hash
                result = json.loads(stdout)
                metadata_hash = result["Hash"]
                print("成功获取 Hash:", metadata_hash)

                # 可以在这里添加断言验证
                with allure.step("Validate output"):
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
        stdout, stderr = btfs_handler.execute_command(command_template,key1=key1, key2=key2, key3=metadata_hash, key4=key)
        # 查看输出内容是否包含 key
        if "Hash" not in stdout:
            print("输出不包含 'Hash'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "Hash" in stdout
