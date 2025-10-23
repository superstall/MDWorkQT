from API.util import *
from API.init_fuzzywuzzy import get_list_fuzzywuzzy
import uuid
from globalUtile import get_RootDirName
import os

def Request_search_ALLbackupFileContent(filepath,Pointer):
    # 获取文档目录下的所有备份文件文件名，并进行文件名时间排序
    if not exists_filepath(filepath):
        return []
    this_file = filepath.rsplit('\\',1)
    ALLfilename = get_filepath_ALLfilename(this_file[0])
    print(ALLfilename)
    if not ALLfilename:
        return []
    # 好像不用对文件进行排序，就不排了
    isTrue = False # 用来给外部信号，Pointer是否不能再大了
    if Pointer  >= len(ALLfilename):
        this_filename = ALLfilename[-1]
        isTrue = True
    else:
        this_filename = ALLfilename[Pointer]
    this_filepath = this_file[0] + '\\' + this_filename
    return  (isTrue,this_filepath,read_file(this_filepath))

def Request_init_package(DOCUMENTPATH=None) -> list:
    # 初始化项目包
    if DOCUMENTPATH == None:
        DOCUMENTPATH = str(get_RootDirName()) + '\markdownfile'  # 动态目录
    ALLTEXTIDPATH = os.path.join(DOCUMENTPATH, 'alltextID.json')
    return_json = []
    # is_createALLTEXTIDPATH = False
    # 检查ID存放文件是否存在，不存在则创建
    if exists_filepath(ALLTEXTIDPATH) is False:
        create_filepath(ALLTEXTIDPATH)
        # is_createALLTEXTIDPATH = True

    # 文档目录规范：md + '_' + 对应时间，例如md_2025-9
    # 文档名规范：id + '_' + 文章标题  + '.md' id格式00001 共5位数，超出99999，00001a，00001b设置
    # 查询存储所有文档信息的文件
    document_Timelist = get_dirpath_ALLdirname(DOCUMENTPATH)

    # # 读取最新alltextID.json文件内容
    # old_alltestID_list = []
    # # 文件已存在读取
    # if is_createALLTEXTIDPATH == False:
    #     # 文件内容行数正常读取
    #     if read_json_file_isExistence(ALLTEXTIDPATH):
    #         old_alltestID_list = read_json_file(ALLTEXTIDPATH)
    # return_json = old_alltestID_list

    # 处理所有文档信息包-初始化
    for package in document_Timelist:
        # 获取时间包内所有文档包
        timedir_path = os.path.join(DOCUMENTPATH,package)
        document_namelist = get_dirpath_ALLdirname(timedir_path)
        # 文档包录入ID存储文件alltextID.json
        for filename in document_namelist:
            # 获取文件包
            mdfile_path = os.path.join(timedir_path, filename)
            this_mdfile_namelist = get_filepath_ALLfilename(mdfile_path)
            this_mdfile_name = [thisfilename for thisfilename in this_mdfile_namelist if thisfilename == str(filename)+".md"][0]
            this_mdfile_path = os.path.join(mdfile_path, this_mdfile_name)
            # old_allfilename_list = [thisfilename for thisfilename in old_alltestID_list if thisfilename['filename'] == str(filename)+".md"]
            # # 文件已经录入不再重复录入
            # if len(old_allfilename_list):
            #     continue
            # 文件信息存入
            return_json.append(
                {
                    "fileID": create_uuid(),
                    "isLANshared": False,
                    "name":str(filename).split('_')[2],
                    "label":str(filename).split('_')[1],
                    "filepath": this_mdfile_path,
                    "filename": str(filename) + ".md",
                    "mddirpath":mdfile_path,
                    "mddirname": filename,
                    "timedirpath": timedir_path,
                    "timedirname":package

                }
            )
    # 一起写入
    write_json_file(ALLTEXTIDPATH,return_json)
    write_json_file(ALLTEXTIDPATH,return_json)
    return return_json

def Request_search_fileID_package(fileID,return_json) -> dict:
    return_list = [package for package in return_json if package['fileID'] == fileID]
    if return_list:
        return return_list[0]
    else:
        return False

def Request_search_package(search_string,return_json) -> list:
    # 查询功能
    # 初始化操作，其实这里不推荐，因为本地操作用户只有一个人不必要的耗时操作
    return_list = [name['name'] for name in return_json]
    return_list = get_list_fuzzywuzzy(return_list,search_string,limit=20)
    return_list = [packet[0] for packet in return_list]
    return_packageList = []
    for package in return_json:
        if package['name'] in return_list:
            return_packageList.append(package)

    return return_packageList

def Request_update_package(fileID,content,return_json,name,label,homeUI) -> str:
    is_newfile = True #文件是否存在
    md_file_dir = str(homeUI.DOCUMENTPATH)  # 项目所在根目录
    # 修改文档功能
    try:
        this_json = [packet for packet in return_json if packet['fileID'] == fileID][0]
        this_read_content = read_file(this_json['filepath'])
    except:
        is_newfile = False
        # 构造创建
        nowtime_tuple = get_now_time() # 当前时间
        time_dir_name = 'md_' + str(nowtime_tuple[0]) + '-' + str(nowtime_tuple[1]) # 时间所在目录
        md_num = str(len(return_json)).zfill(5)  # 生成5位数
        md_dir_file_name = md_num + "_" + label + "_" + name  #md文件夹名称
        md_file_name = md_num + "_" + label + "_" + name + ".md"  # md文件名
        #构造内容
        filepath = md_file_dir + "\\" + time_dir_name + "\\" + md_dir_file_name + "\\" + md_file_name
        filename = md_file_name
        mddirpath = md_file_dir + "\\" + time_dir_name + "\\" + md_dir_file_name
        mddirname = md_dir_file_name
        timedirpath = md_file_dir + "\\" + time_dir_name
        timedirname = time_dir_name

        # 新文档构造目录
        create_dir(timedirpath)
        create_dir(mddirpath)

        this_json = {
                "fileID": fileID,
                "isLANshared": False,
                "name": name,
                "label": label,
                "filepath": filepath,
                "filename": filename,
                "mddirpath": mddirpath,
                "mddirname": mddirname,
                "timedirpath": timedirpath,
                "timedirname": timedirname
            }
        this_read_content = ""

    # 文件内容校验
    if this_read_content == content:
        return this_read_content


    # 覆盖文件内容
    write_file(this_json['filepath'],content)
    # 备份修改
    if is_newfile:
        # 备份文件名规范: id + '_' + 文章标签 + '_' +文章标题  + "_20250930_175121" + '.md' id格式00001 共5位数，超出99999，00001a，00001b设置
        backup_filename = timenow_filename(this_json['mddirname'],suffix='md')
        backup_filepath = os.path.join(this_json['mddirpath'],backup_filename)
        shutil_file(this_json['filepath'],backup_filepath)
    # 初始化文档根目录
    Request_init_package(md_file_dir)
    return content

def Request_delete_package(fileID,return_json) -> bool:
    # 删除文档功能
    try:
        this_json = [packet for packet in return_json if packet['fileID'] == fileID][0]
        return remove_dir(this_json['mddirpath'])
    except:
        return False

















