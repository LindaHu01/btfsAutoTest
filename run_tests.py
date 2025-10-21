import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime

import pytest

from utils.report_util import get_test_results
from utils.telegram_bot import TelegramBot

# 配置Telegram机器人
TELEGRAM_TOKEN = "7108929540:AAGhGbpcVjEFss34OLoZErz8_WtHxbReeGc"
TELEGRAM_CHAT_ID = "-1002612587832"
# 报告路径
REPORT_URL = ""

# 获取项目根目录
PROJECT_ROOT = Path(__file__).parent.absolute()


def generate_text_report(results, duration, report_url, test_failed):
    """生成简洁的文本报告"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    duration_str = str(duration).split('.')[0]

    status_emoji = "❌" if test_failed else "✅"
    status_text = "失败" if test_failed else "成功"

    # 添加失败详情
    failure_details = ""
    if results['failed'] > 0:
        failure_details = f"\n🔴 失败测试: {results['failed']}"

    # 添加报告路径信息
    report_path_line = f"报告路径：{report_url}" if report_url else "报告路径：未生成"

    return f"""
Hi, BTFS v4.0自动化测试报告~~
⏰时间: {timestamp}
📊测试结果: ✅成功: {results['passed']} ❌失败: {results['failed']} ⚠️跳过: {results['skipped']}
📋总数: {results['passed'] + results['failed'] + results['skipped']}
{report_path_line}
"""


def main():
    global REPORT_URL
    start_time = datetime.now()
    test_failed = False
    report_dir = ""

    try:
        print("Starting test execution...")
        # 在项目根目录下运行pytest（添加插件参数）
        result = subprocess.run(
            [
                "pytest",
                "-v",
                "--alluredir=allure-results",
                "-p", "pytest_order",  # 显式加载插件
                "testcases"
            ],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )

        print("Test Output:\n", result.stdout)
        if result.stderr:
            print("Test Errors:\n", result.stderr)

        # result.returncode == 0 表示测试成功，否则失败，失败后 test_failed 为 True
        test_failed = (result.returncode != 0)

    except Exception as e:
        print(f"测试执行发生异常: {str(e)}")
        test_failed = True

    # 生成Allure报告
    try:
        print("Generating Allure report...")
        report_dir = f"allure-report-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        report_path = PROJECT_ROOT / report_dir

        subprocess.run([
            "allure",
            "generate",
            "allure-results",
            "-o",
            report_dir,
            "--clean"
        ], check=True, cwd=PROJECT_ROOT)

        # 更新报告URL - 使用PyCharm内置服务器格式
        REPORT_URL = f"http://localhost:63342/{os.path.basename(PROJECT_ROOT)}/{report_dir}/index.html"
        print(f"报告生成在: {REPORT_URL}")

    except Exception as e:
        print(f"生成报告失败: {str(e)}")
        test_failed = True
        REPORT_URL = ""  # 确保报告URL为空

    # 获取测试结果
    try:
        test_results = get_test_results()
        print(f"Test results: {test_results}")
    except Exception as e:
        print(f"获取测试结果失败: {str(e)}")
        test_results = {'total': 0, 'passed': 0, 'failed': 0, 'skipped': 0}
        test_failed = True

    # 生成报告摘要
    duration = datetime.now() - start_time
    summary = generate_text_report(test_results, duration, REPORT_URL, test_failed)

    # 发送报告到Telegram
    try:
        bot = TelegramBot(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID)

        # 发送文本摘要
        bot.send_message(summary)

        # 压缩报告
        zip_report = f"{report_dir}.zip"
        zip_path = PROJECT_ROOT / zip_report

        # 压缩报告目录
        subprocess.run(["zip", "-r", zip_report, report_dir],
                       cwd=PROJECT_ROOT,
                       check=True)

        # 发送压缩报告
        if zip_path.exists():
            bot.send_document(str(zip_path))
            print(f"已发送压缩报告: {zip_report}")
        else:
            print(f"压缩报告未生成: {zip_report}")

        print("报告已发送到Telegram")
    except Exception as e:
        print(f"发送报告到Telegram失败: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # 确保项目根目录在PYTHONPATH中
    sys.path.insert(0, str(PROJECT_ROOT))

    # 检查插件是否安装
    try:
        import pytest_order

        print("✅ pytest-order 插件已安装")
    except ImportError:
        print("❌ 错误: pytest-order 插件未安装")
        print("请执行: pip install pytest-order")
        sys.exit(1)

    main()