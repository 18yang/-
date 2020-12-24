import csv
import matplotlib.pyplot as plt
# 读取csv至字典
csvFile = open("C:/data/model/pro_result.csv", "r", encoding='utf-8')
reader = csv.reader(csvFile)

# 建立空字典
x = []
y = []
for item in reader:
    # 忽略第一行
    if reader.line_num == 1:
        continue
    x.append(item[0])
    y.append(item[1][0:4])
csvFile.close()
plt.rcParams['font.sans-serif'] = ['fangsong']
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x, y)
# plt.plot(x, y)
plt.show()
