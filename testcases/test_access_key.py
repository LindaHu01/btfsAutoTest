from pathlib import Path

import allure
import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
# 获取项目根目录
project_root = Path(__file__).parent.parent
COMMANDS_FILE = project_root / 'data' / 'access_key_commands.yml'
global access_key


@allure.suite("BTFS Access Key Tests")
class TestBtfsAccessKey:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    @allure.story("BTFS Access Key Generate Tests")
    @allure.title("test_accessKey_generate")
    def test_accessKey_generate(self, btfs_handler):
        """
        Test the 'test_accessKey_generate ' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_accesskey_gen']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            print("标准输出:", command_template)
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("标准输出2:", stderr)
        # Assert the command output
        with allure.step("Validate output"):
            assert "key" in stdout

    @allure.story("BTFS Access key get Test")
    @allure.title("test_accessKey_get")
    def test_accessKey_get(self, btfs_handler):
        """
        Test the 'test_accessKey_get ' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_accesskey_get']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            # 查看输出内容是否包含 key
            if "key" not in stdout:
                print("输出不包含 'key'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "key" in stdout

    @allure.story("BTFS Access key delete Test")
    @allure.title("test_accessKey_list")
    def test_accessKey_list(self, btfs_handler):
        """
        Test the 'test_accessKey_list ' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_accesskey_list']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            # 查看输出内容是否包含 key
            if "key" not in stdout:
                print("输出不包含 'key'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "key" in stdout

    @allure.story("BTFS Access key disable Test")
    @allure.title("test_accessKey_disable")
    def test_accessKey_disable(self, btfs_handler):
        """
        Test the 'test_accessKey_disable ' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_accesskey_disable']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][1]['params']['key']
            print("标准输出1:", key3)
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)

    @allure.story("BTFS Access key enable Test")
    @allure.title("test_accessKey_enable")
    def test_accessKey_enable(self, btfs_handler):
        """
        Test the 'test_accessKey_enable ' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_accesskey_enable']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][2]['params']['key']
            print("标准输出1:", key3)
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)

    @allure.story("BTFS Access key reset Test")
    @allure.title("test_accessKey_reset")
    def test_accessKey_reset(self, btfs_handler):
        """
        Test the 'test_accessKey_disable ' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_accesskey_reset']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][3]['params']['key']
            print("标准输出1:", key3)
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)

    # def test_accessKey_delete(self, btfs_handler):
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




