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

    # 创建一个字典来存储合并后的DataFrame
    merged_tables_data = {}

    # 遍历所有表，尝试将它们与其他表根据公共列连接
    merged_table_names = set()  # 用于存储已合并的表名组合，避免重复
    for table_name1, table_df1 in tables_data.items():
        for table_name2, table_df2 in tables_data.items():
            if table_name1 != table_name2 and (table_name2, table_name1) not in merged_table_names:
                # 检查两个表是否有公共列
                common_columns = set(table_df1.columns).intersection(set(table_df2.columns))
                if common_columns:
                    # 如果有公共列，则进行等值连接
                    merged_df = pd.merge(table_df1, table_df2, on=list(common_columns), how='outer')
                    # 创建新表名，并确保表名按字母顺序排序
                    sorted_table_names = sorted([table_name1, table_name2])
                    merged_table_name = "_".join(sorted_table_names)
                    # 将合并后的DataFrame添加到merged_tables_data
                    merged_tables_data[merged_table_name] = merged_df
                    # 添加已合并的表名组合到集合中，避免重复
                    merged_table_names.add((table_name1, table_name2))
                    # 标记表名1和表名2已被合并，不需要单独添加
                    merged_table_names.add(table_name1)
                    merged_table_names.add(table_name2)

    # 添加没有被合并的原始表到结果字典
    for table_name, table_df in tables_data.items():
        if table_name not in merged_table_names:
            merged_tables_data[table_name] = table_df

    return merged_tables_data


if __name__ == "__main__":
    data = get_data_from_db()
    print(type(data), "\n")
    for table_name, table_df in data.items():
        print(f"Table: {table_name}")
        print(table_df)
        print(type(table_df))
        print("###########################################\n\n")
