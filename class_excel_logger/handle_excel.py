# @Time:2021/5/8 5:32 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

"""

excel类：明确需求
1、读取表头
2、读取数据 - 读取表头以外的所有数据


初始化工作：加载一个excel，打开一个表单
"""
from openpyxl import load_workbook
import os


class Test_Handel_Excel:

    def __init__(self, file_path, sheet_name):
        # 初始化函数如果在后续需要使用，需要实例化
        self.wb = load_workbook(file_path)
        self.sh = self.wb[sheet_name]

    # 取key
    def test_read_titles(self):
        titles = []
        for item in list(self.sh.rows)[0]:
            titles.append(item.value)
        return titles

    # 取value，拼接
    def test_all_datas(self):
        all_datas = []
        titles = self.test_read_titles()
        for item in list(self.sh.rows)[1:]:
            values = []
            for val in item:
                values.append(val.value)
            res = dict(zip(titles, values))
            # res["check"] = eval(res["check"])
            all_datas.append(res)
        return all_datas

    def close_file(self):
        self.wb.close()


if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")
    exc = Test_Handel_Excel(file_path, "login")
    cases = exc.test_all_datas()
    exc.close_file()
    print(cases)
