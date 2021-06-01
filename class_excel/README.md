##1、excel操作
    WorkBook
    Sheet
    Cell
##2、测试数据文件，提前准备好
```python
wb = laod_workbook(filepath)
```
###表单
```python
sh = wb["表单名"]
```
###获取所有数据 - 按行获取
```python
sh.rows => list(sh.rows)
```
###遍历行，获取每一行当中，所有列表数据。每一行数据储存在字典当中，一行代码一个测试用力数据。
```python
key:value

key：遍历第一行：
for row in list(sh.rows)[0]:
key = cel.value
```
从第二行开始，每一行是一个测试数据，先遍历行，在行当中，在遍历列。
```python
for row in list(sh.rows)[1:]:
    values = []
    for cel in row：
        values.append(cel.value)
    case_data = dict(zip(title.values))
    # 有一个key的值，要求是字典
    case_data["check"] = eval(case_data["check"])
    all_case.append(case_data)
```
