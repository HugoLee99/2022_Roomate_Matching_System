import pymysql
import xlwt
host='localhost'
port=3306
user='root'
password='Mcqmyxh2$'
database='matching'
charset='utf8'
conn = pymysql.connect(host='localhost',port=3306,user='root',password="roots",database='matching',charset='utf8')
cursor = conn.cursor()

table = 'matching1'
count = cursor.execute("select * from {table};".format(table=table))
print(count)

# 重置游标的位置
cursor.scroll(0, mode='absolute')
# 拿到该条SQL所有结果
results = cursor.fetchall()
print(results)

# 拿到该表里面的字段名称
fields = cursor.description
print(fields)

workbook = xlwt.Workbook()
sheet = workbook.add_sheet(table, cell_overwrite_ok=True)

# 写上字段信息
for field in range(0, len(fields)):
   sheet.write(0, field, fields[field][0])

# 获取并写入数据段信息
row = 1
col = 0
for row in range(1, len(results) + 1):
   for col in range(0, len(fields)):
      value = results[row - 1][col]
      if not value:
         value = ''
      sheet.write(row, col, '%s' % value)

workbook.save(r'./{db}_{table}.xlsx'.format(db=database, table=table))

table2 = 'matching2'
count = cursor.execute("select * from {table};".format(table=table2))
print(count)

# 重置游标的位置
cursor.scroll(0, mode='absolute')
# 拿到该条SQL所有结果
results = cursor.fetchall()
print(results)

# 拿到该表里面的字段名称
fields = cursor.description
print(fields)

workbook = xlwt.Workbook()
sheet = workbook.add_sheet(table, cell_overwrite_ok=True)

# 写上字段信息
for field in range(0, len(fields)):
   sheet.write(0, field, fields[field][0])

# 获取并写入数据段信息
row = 1
col = 0
for row in range(1, len(results) + 1):
   for col in range(0, len(fields)):
      value = results[row - 1][col]
      if not value:
         value = ''
      sheet.write(row, col, '%s' % value)

workbook.save(r'./{db}_{table}.xlsx'.format(db=database, table=table2))
