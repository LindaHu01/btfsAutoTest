import subprocess
import pytest
import time
import os

# 配置
BTFS_PATH = "/home/ec2-user/btfs/.btfs.staging333_01"
BTFS_CMD_PATH = "/home/ec2-user/go/src/github.com/bittorrent/3.3.0_new/go-btfs/cmd/btfs"
HOST = "54.151.1.17"  # 假设你已经连接到远程主机
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # 更新为你的私钥路径

def start_btfs_daemon():
    """启动 btfs daemon 并运行在后台"""
    env = os.environ.copy()
    env["BTFS_PATH"] = BTFS_PATH  # 设置 BTFS_PATH 环境变量
    start_command = f"cd {BTFS_CMD_PATH} && ./btfs daemon &"  # 进入目录并启动 daemon

    process = subprocess.Popen(
        start_command,
        shell=True,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return process

def check_btfs_running():
    """检查 btfs daemon 是否在运行"""
    result = subprocess.run(
        ["ps", "aux"],
        capture_output=True,
        text=True
    )
    return "btfs daemon" in result.stdout

def stop_btfs_daemon():
    """停止 btfs daemon 进程"""
    subprocess.run(["killall", "btfs"])

@pytest.fixture
def btfs_daemon():
    """启动 btfs daemon 并检查其是否成功启动"""
    # 启动 btfs daemon
    process = start_btfs_daemon()

    # 等待 10 秒钟让 btfs daemon 启动
    for _ in range(10):
        if check_btfs_running():
            yield process  # 成功启动后继续执行测试
            break
        time.sleep(3)
    else:
        pytest.fail("btfs daemon did not start in time")

    # 测试完成后，停止 btfs daemon
    stop_btfs_daemon()
    process.wait()

def test_btfs_daemon_start(btfs_daemon):
    """测试 btfs daemon 是否启动成功"""
    assert check_btfs_running(), "btfs daemon did not start successfully"
