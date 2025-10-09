import os
import json
import shutil
import uuid
import copy
import time
from datetime import datetime
from markdown import markdown

def get_file_open_time(file_path):
    # 获取文件或文件夹创建的时间和最后一次修改时间
    # 获取最后修改时间（等同于“创建日期”在很多系统中）
    mtime = os.path.getmtime(file_path)
    # 转换为人类可读的日期格式
    mtime_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
    # 获取最后访问时间
    atime = os.path.getatime(file_path)
    # 转换为人类可读的日期格式
    atime_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(atime))
    return (mtime_str, atime_str)

def create_uuid():
    # 生成一个随机的UUID
    return str(uuid.uuid1())

def timenow_filename(filename,suffix):
    # 获取当前时间，精确到秒
    now = datetime.now()
    # 格式化时间字符串
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    # 使用时间字符串作为文件名
    filename = f"{filename}_{timestamp}.{suffix}"
    return filename


class constOS:
    @staticmethod
    def get_symbol():
        if os.name == 'nt':
            return '\\'
        elif os.name == 'posix':
            return '/'
        else:
            raise OSError('OS not supported')

def exists_filepath(filename):
    # 查询当前文件夹或文件是否存在
    filepath = os.path.join(os.path.dirname(__file__), filename)
    return os.path.exists(filepath)

def create_dir(dirpath):
    # 文件夹不存在就创建
    if exists_filepath(dirpath) is False:
        os.makedirs(dirpath,exist_ok=True) # exist_ok如果目录已存在不会抛出异常
        return True
    return True


def create_filepath(filepath,context=''):
    # 创建文件，坚决创建
    # 判断是否文件目录
    if '.' not in filepath.rsplit(constOS.get_symbol(), 1)[1]:
        return False

    # 判断文件夹是否存在，不存在就创建
    this_dir = filepath.rsplit(constOS.get_symbol(), 1)[0]
    if exists_filepath(this_dir) is False:
        create_dir(filepath.rsplit(constOS.get_symbol(), 1)[0])

    # 创建文件，如果文件不存在则创建
    if exists_filepath(filepath) is False:
        with open(filepath, 'w') as file:
            file.write(context)
        return True
    return True


def get_filepath_ALLfilename(filepath):
    # 获取文件夹下文件名
    return [name for name in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, name))]

def get_dirpath_ALLdirname(dirpath):
    # 获取文件夹下文件夹名称
    return [name for name in os.listdir(dirpath) if os.path.isdir(os.path.join(dirpath, name))]


def read_json_file_isExistence(filepath) -> list:
    # 获取json文件是否存在内容
    with open(filepath,'r') as json_file:
        if json_file.read().count('\n') == 0:
            return False
        return True
def read_json_file(filepath) -> list:
    # 获取json文件内容
    with open(filepath,'r') as json_file:
        return json.load(json_file)

def write_json_file(filepath,data):
    # 写入json文件内容
    with open(filepath,'w',encoding='utf-8') as json_file:
        json.dump(data,json_file,indent=4)
    return True

def read_file(filepath) -> str:
    # 获取文件内容
    with open(filepath,'r',encoding='utf-8') as file:
        return file.read()

def write_file(filepath,data):
    # 写入文件内容
    with open(filepath,'w',encoding='utf-8') as file:
        file.write(data)
    return True

def shutil_file(source_file,target_dir):
    # 备份文件，复制文件并重命名
    shutil.copy(source_file,target_dir)
    return True

def remove_dir(folder_path):
    # 检查文件夹是否存在
    if exists_filepath(folder_path):
        # 删除文件夹及其所有内容
        shutil.rmtree(folder_path)
    return True