import paramiko
import yaml


class BtfsHandler:
    def __init__(self, host, username, private_key_path, commands_file):
        self.host = host
        self.username = username
        self.private_key_path = private_key_path
        self.ssh_client = None
        self.commands = self._load_commands(commands_file)

    def _load_commands(self, commands_file):
        """Load commands from a YAML file."""
        with open(commands_file, 'r') as file:
            return yaml.safe_load(file)

    def connect(self):
        """Establish an SSH connection to the server."""
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            private_key = paramiko.RSAKey.from_private_key_file(self.private_key_path,password="1234")
            self.ssh_client.connect(hostname=self.host, username=self.username, pkey=private_key)
            print("SSH connection established.")
        except Exception as e:
            raise Exception(f"Failed to connect: {e}")

    def disconnect(self):
        """Close the SSH connection."""
        if self.ssh_client:
            self.ssh_client.close()
            print("SSH connection closed.")

    def execute_command(self, command, **kwargs):
        """
        Execute a command on the server and return its output.
        """
        if not self.ssh_client:
            raise Exception("SSH client is not connected.")

        # Replace placeholders in the command with actual values
        command = command.format(**kwargs)
        # try:
        #     stdin, stdout, stderr = self.ssh_client.exec_command(command)
        #     output = stdout.read().decode().strip()
        #     error = stderr.read().decode().strip()
        #     if error:
        #         raise Exception(f"Command Error: {error}")
        #     return output
        # except Exception as e:
        #     raise Exception(f"Failed to execute command '{command}': {e}")
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            stdout_result = stdout.read().decode().strip()
            stderr_result = stderr.read().decode().strip()
            return stdout_result, stderr_result
        except Exception as e:
            self.logger.error(f"执行命令失败：{e}")
            raise

    def start_daemon(self):
        """Start the BTFS daemon."""
        try:
            start_command = self.commands['btfs']['start_daemon']
            self.execute_command(start_command)
            print("BTFS daemon started.")
        except Exception as e:
            raise Exception(f"Failed to start BTFS daemon: {e}")