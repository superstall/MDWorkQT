import os
from pathlib import Path

def get_RootDirName():
    # 获取当前文件所在的目录
    current_dir = Path(__file__).parent

    # 向上移动一级到父目录
    return current_dir.parent

def get_package_root_dir():
    return Path(__file__).parent

