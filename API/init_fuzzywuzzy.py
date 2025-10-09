# 此包用来实现模糊查询
from fuzzywuzzy import process

def get_list_fuzzywuzzy(return_list,return_string,limit=20) -> list:
    return_list = process.extract(return_string, return_list,limit=limit)
    return_list = [packet for packet in return_list if packet[1] > 0]
    return return_list

