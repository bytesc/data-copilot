import pandas as pd
import pymysql


def get_data_from_db():

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 database='data_copilot')
    # 创建一个cursor对象
    cursor = connection.cursor()

    # 执行SHOW TABLES命令获取所有表名
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    # 准备一个字典来存储所有表的DataFrame
    tables_data = {}

    # 遍历所有表名
    for table_name in tables:
        table_name = table_name[0]  # 表名是一个元组，取第一个元素
        query = f"SELECT * FROM {table_name}"  # 构造查询语句
        tables_data[table_name] = pd.read_sql(query, connection)  # 读取表内容到DataFrame

    # 关闭cursor和连接
    cursor.close()
    connection.close()

    # 打印每个表的内容
    # for table_name, table_df in tables_data.items():
    #     print(f"Table: {table_name}")
    #     print(table_df)
    #     print("###########################################\n\n")

    return tables_data


if __name__ == "__main__":
    data = get_data_from_db()
    print(type(data), "\n")
    for table_name, table_df in  data.items():
        print(f"Table: {table_name}")
        print(table_df)
        print(type(table_df))
        print("###########################################\n\n")
