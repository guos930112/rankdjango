# -*- coding: utf-8 -*-
"""
@Time   ： 2020/6/24 8:42 上午
@Author ： guos
@File   ：additional_exercises.py
@IDE    ：PyCharm

"""


def version_compare(version1, version2):
    if isinstance(version1, str) and isinstance(version2, str):
        if not version1 and version2:
            return -1
        if version1 and not version2:
            return 1
        if not version1 and not version2:
            return 0
        v_1_list = version1.split('.')
        v_2_list = version2.split('.')
        length1 = len(v_1_list)
        length2 = len(v_2_list)
        if length1 < length2:
            v_1_list += ['0'] * (length2 - length1)
        elif length1 > length2:
            v_2_list += ['0'] * (length1 - length2)
        index1 = 0
        while index1 < max(length1, length2):
            if int(v_1_list[index1]) > int(v_2_list[index1]):
                return 1
            elif int(v_1_list[index1]) < int(v_2_list[index1]):
                return -1
            else:
                index1 += 1
        return 0


if __name__ == '__main__':
    version1 = "1.0"
    version2 = "1.0.0"
    res = version_compare(version1, version2)
    print(res)
