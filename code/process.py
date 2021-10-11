import pandas as pd

filename = '../data/origin_data_new.xlsx'

# 修改headers
quest_cnt = [9, 23, 13, 13, 4, 2]
headers = list(range(100, 100+quest_cnt[0]+1))
for i in range(2, len(quest_cnt)+1):
    headers.extend(range(i * 100 + 1, i * 100 + quest_cnt[i-1] + 1))

# 为了读取数据，为其他列添加名称，都是数字，便于后续删除该列
all_headers = list(range(0, 6))
all_headers.extend(headers)
all_headers.append(6)

# 读取数据，并删除不需要的列
df_origin_data = pd.read_excel(filename)
df_origin_data.columns = all_headers
for i in range(7):
    del df_origin_data[i]
del df_origin_data[107] # 家长职业
del df_origin_data[109] # 获取信息途径
del df_origin_data[601] # 满意和不满意
del df_origin_data[602] # 建议改善
print(df_origin_data)

# 删除headers中获取信息的途径对应的数字
headers.remove(107)
headers.remove(109)
headers.remove(601)
headers.remove(602)

# 修改表格中的值为数字：是1否2，选项1-5，跳过0
for idx in headers:
    item = df_origin_data[idx]
    for i, x in enumerate(item.values):
        # if x == '是' | x == '完全不符合'| x == '很好':
        if x in ['是', '非常不愿意', '完全不符合', '不好', '5人制', '初一', '1年及以内', '男']:
            item.values[i] = 1
        elif x in ['否', '不愿意', '不太符合', '比较差', '8人制', '初二', '1-2年', '女']:
            item.values[i] = (0 if idx == 100 else 2)
        elif x in ['一般', '5人制┋8人制', '初三', '3-4年']:
            item.values[i] = 3
        elif x in ['比较符合', '愿意', '比较好', '高一', '5年及以上']:
            item.values[i] = 4
        elif x in ['完全符合', '非常愿意', '很好', '高二']:
            item.values[i] = 5
        elif x in ['高三']:
            item.values[i] = 6
        elif x in ['(跳过)']:
            item.values[i] = 0
        else:
            if idx == 103:
                item.values[i] = 1

df_origin_data.to_csv('../data/to_num_new.csv', index=False)
print(df_origin_data)