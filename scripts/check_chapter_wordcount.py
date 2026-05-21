#!/usr/bin/env python3
"""
章节字数检查脚本
检查指定章节文件的中文字数是否在目标范围内（默认 3000-5000）
"""

import sys
import re
import os
from pathlib import Path

def count_chinese_chars(text: str) -> int:
    """统计中文字符数量（不含标点、空格、英文）"""
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
    return len(chinese_chars)

def count_all_chars(text: str) -> int:
    """统计所有可见字符数量"""
    # 移除空白字符
    cleaned = re.sub(r'\s+', '', text)
    return len(cleaned)

def check_chapter(filepath: str, min_words: int = 3000, max_words: int = 5000) -> dict:
    """检查章节字数

    Returns:
        dict: {
            "file": str,
            "chinese_chars": int,
            "all_chars": int,
            "passed": bool,
            "status": "ok" | "too_short" | "too_long",
            "message": str
        }
    """
    path = Path(filepath)
    if not path.exists():
        return {
            "file": filepath,
            "chinese_chars": 0,
            "all_chars": 0,
            "passed": False,
            "status": "file_not_found",
            "message": f"文件不存在: {filepath}"
        }

    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    chinese_count = count_chinese_chars(text)
    all_count = count_all_chars(text)

    if chinese_count < min_words:
        return {
            "file": str(path.name),
            "chinese_chars": chinese_count,
            "all_chars": all_count,
            "passed": False,
            "status": "too_short",
            "message": f"❌ 字数不足: {chinese_count} 字（目标 {min_words}-{max_words}）需扩写约 {min_words - chinese_count} 字"
        }
    elif chinese_count > max_words:
        return {
            "file": str(path.name),
            "chinese_chars": chinese_count,
            "all_chars": all_count,
            "passed": False,
            "status": "too_long",
            "message": f"⚠️ 字数超标: {chinese_count} 字（目标 {min_words}-{max_words}）超出 {chinese_count - max_words} 字"
        }
    else:
        return {
            "file": str(path.name),
            "chinese_chars": chinese_count,
            "all_chars": all_count,
            "passed": True,
            "status": "ok",
            "message": f"✅ 字数达标: {chinese_count} 字"
        }

def check_all_chapters(directory: str, min_words: int = 3000, max_words: int = 5000) -> list:
    """检查目录下所有章节"""
    results = []
    dir_path = Path(directory)

    # 查找所有章节文件
    chapter_files = sorted(dir_path.glob("第*章*.md"))

    for f in chapter_files:
        result = check_chapter(str(f), min_words, max_words)
        results.append(result)

    return results

def main():
    if len(sys.argv) < 2:
        print("用法: python check_chapter_wordcount.py <章节文件或目录> [最小字数] [最大字数]")
        print("示例: python check_chapter_wordcount.py 第01章.md")
        print("示例: python check_chapter_wordcount.py ./正文 3000 5000")
        sys.exit(1)

    target = sys.argv[1]
    min_words = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
    max_words = int(sys.argv[3]) if len(sys.argv) > 3 else 5000

    # 判断是目录还是文件
    target_path = Path(target)
    if target_path.is_dir():
        results = check_all_chapters(target, min_words, max_words)
    else:
        results = [check_chapter(target, min_words, max_words)]

    # 输出结果
    total_passed = 0
    for r in results:
        print(f"{r['message']}")
        if r['passed']:
            total_passed += 1

    print(f"\n总计: {total_passed}/{len(results)} 章节达标")

    # 返回码
    if total_passed == len(results):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
