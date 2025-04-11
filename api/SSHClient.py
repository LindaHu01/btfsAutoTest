import paramiko
import yaml
import os
import logging


class SSHClient:
    def __init__(self, hostname, username, private_key_path=None, private_key_password=None, password=None, port=22, timeout=10):
        """
        初始化 SSH 客户端

        :param hostname: 服务器地址（IP 或域名）
        :param username: SSH 用户名
        :param private_key_path: 私钥文件路径（可选）
        :param private_key_password: 私钥文件密码（可选）
        :param password: 密码（可选）
        :param port: SSH 端口，默认 22
        :param timeout: 超时时间，默认 10 秒
        """
        self.hostname = hostname
        self.username = username
        self.private_key_path = private_key_path
        self.private_key_password = private_key_password
        self.password = password
        self.port = port
        self.timeout = timeout
        self.client = None
        self.is_connected = False

        # 日志配置
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("SSHClient")

    def connect(self):
        """
        连接到远程服务器
        :return: None
        """
        try:
            # 初始化 SSH 客户端
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # 加载私钥
            if self.private_key_path:
                private_key = paramiko.RSAKey.from_private_key_file(
                    os.path.expanduser(self.private_key_path), password=self.private_key_password
                )
                self.client.connect(
                    hostname=self.hostname,
                    port=self.port,
                    username=self.username,
                    pkey=private_key,
                    timeout=self.timeout,
                )
            else:
                # 使用密码登录
                self.client.connect(
                    hostname=self.hostname,
                    port=self.port,
                    username=self.username,
                    password=self.password,
                    timeout=self.timeout,
                )

            self.is_connected = True
            self.logger.info(f"成功连接到服务器：{self.hostname}")
        except (paramiko.AuthenticationException, paramiko.SSHException, Exception) as e:
            self.logger.error(f"连接服务器失败：{e}")
            raise

    def disconnect(self):
        """
        断开与远程服务器的连接
        :return: None
        """
        if self.client:
            self.client.close()
            self.is_connected = False
            self.logger.info(f"已断开与服务器 {self.hostname} 的连接。")

    def execute_command(self, command):
        """
        在远程服务器上执行命令
        :param command: 要执行的命令
        :return: (stdout, stderr)
        """
        if not self.is_connected:
            raise ConnectionError("未连接到服务器，请先调用 connect 方法连接。")

        try:
            stdin, stdout, stderr = self.client.exec_command(command)
            stdout_result = stdout.read().decode().strip()
            stderr_result = stderr.read().decode().strip()
            return stdout_result, stderr_result
        except Exception as e:
            self.logger.error(f"执行命令失败：{e}")
            raise

    def __enter__(self):
        """
        进入上下文管理器时自动连接服务器
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        退出上下文管理器时自动断开连接
        """
        self.disconnect()


def load_yaml_config(file_path):
    """
    加载 YAML 配置文件
    :param file_path: 配置文件路径
    :return: 配置字典
    """
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        logging.error(f"加载 YAML 配置文件失败：{e}")
        raise


def main():
    # 加载连接配置
    connection_config = load_yaml_config("../data/connection_config.yaml")
    hostname = connection_config["hostname"]
    username = connection_config["username"]
    private_key_path = connection_config["private_key_path"]
    private_key_password = connection_config.get("private_key_password")
    port = connection_config.get("port", 22)
    timeout = connection_config.get("timeout", 10)

    # 加载命令配置
    commands_config = load_yaml_config("../data/commands.yaml")
    commands = commands_config.get("commands", [])

    try:
        # 使用上下文管理器自动管理连接
        with SSHClient(
                hostname=hostname,
                username=username,
                private_key_path=private_key_path,
                private_key_password=private_key_password,
                port=port,
                timeout=timeout,
        ) as ssh:
            # 执行命令列表
            for command in commands:
                stdout, stderr = ssh.execute_command(command)
                print(f"命令: {command}")
                print("标准输出:", stdout)
                print("标准错误:", stderr)
                print("-" * 50)

    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    main()