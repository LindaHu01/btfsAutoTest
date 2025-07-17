import json
import os
from pathlib import Path


def get_test_results():
    """解析Allure结果获取测试统计"""
    results_dir = "allure-results"
    passed = 0
    failed = 0
    broken = 0
    skipped = 0
    unknown = 0

    # 确保结果目录存在
    if not os.path.exists(results_dir):
        return {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "broken": 0,
            "skipped": 0,
            "unknown": 0
        }

    for result_file in Path(results_dir).glob("*-result.json"):
        try:
            with open(result_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                status = data.get("status", "unknown")

                if status == "passed":
                    passed += 1
                elif status == "failed":
                    failed += 1
                elif status == "broken":
                    broken += 1
                elif status == "skipped":
                    skipped += 1
                else:
                    unknown += 1
        except Exception as e:
            print(f"Error processing {result_file}: {str(e)}")
            continue

    total = passed + failed + broken + skipped + unknown
    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "broken": broken,
        "skipped": skipped,
        "unknown": unknown
    }