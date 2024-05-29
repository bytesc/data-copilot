import pandas as pd

from db_conn import connection

# 创建一个DataFrame
sales_by_country = pd.DataFrame({
    "国家": ["美国", "英国", "法国", "德国", "意大利", "西班牙", "加拿大", "澳大利亚", "日本", "中国"],
    "销量": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000],
    "进行订单": [142, 80, 70, 90, 60, 50, 40, 30, 110, 120],
    "结束订单": [120, 70, 60, 80, 50, 40, 30, 20, 100, 110]
})

# 创建一个cursor对象
cursor = connection.cursor()

# 创建表的SQL语句
create_table_query = '''
CREATE TABLE IF NOT EXISTS sales_data (
    国家 VARCHAR(255),
    销量 INT,
    进行订单 INT,
    结束订单 INT
)
'''

# 执行SQL语句
cursor.execute(create_table_query)

# 将DataFrame的每一行插入到MySQL表中
for i, row in sales_by_country.iterrows():
    insert_query = f'''
    INSERT INTO sales_data (国家, 销量, 进行订单, 结束订单)
    VALUES ("{row['国家']}", {row['销量']}, {row['进行订单']}, {row['结束订单']})
    '''
    cursor.execute(insert_query)

# 提交事务
connection.commit()

# 关闭cursor和连接
cursor.close()

# 创建一个游标对象
cursor = connection.cursor()

# 创建employees表的SQL语句
create_employees_table_sql = '''
CREATE TABLE IF NOT EXISTS employees (
    员工号 INT PRIMARY KEY,
    姓名 VARCHAR(50),
    部门 VARCHAR(50)
);
'''

# 创建salaries表的SQL语句
create_salaries_table_sql = '''
CREATE TABLE IF NOT EXISTS salaries (
    员工号 INT PRIMARY KEY,
    工资 INT,
    FOREIGN KEY (员工号) REFERENCES employees(员工号)
);
'''

# 执行SQL语句创建表
cursor.execute(create_employees_table_sql)
cursor.execute(create_salaries_table_sql)

# 准备employees数据
employees_data = {
    '员工号': [1, 2, 3, 4, 5],
    '姓名': ['John', 'Emma', 'Liam', 'Olivia', 'William'],
    '部门': ['HR', 'Sales', 'IT', 'Marketing', 'Finance']
}

# 准备salaries数据
salaries_data = {
    '员工号': [1, 2, 3, 4, 5],
    '工资': [5000, 6000, 4500, 7000, 5500]
}

# 插入employees数据的SQL语句
insert_employees_sql = "INSERT INTO employees (员工号, 姓名, 部门) VALUES (%s, %s, %s)"

# 插入salaries数据的SQL语句
insert_salaries_sql = "INSERT INTO salaries (员工号, 工资) VALUES (%s, %s)"

# 插入employees数据
for employee in zip(employees_data['员工号'], employees_data['姓名'], employees_data['部门']):
    cursor.execute(insert_employees_sql, employee)

# 插入salaries数据
for 工资 in zip(salaries_data['员工号'], salaries_data['工资']):
    cursor.execute(insert_salaries_sql, 工资)

# 提交事务
connection.commit()

# 关闭游标和连接
cursor.close()
connection.close()