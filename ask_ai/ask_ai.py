from pandasai import SmartDatalake

from input_process import input_process


def ask(data, question, llm, graph=True):
    graph_type = "!!!return a single pandas dataframe only!!! "\
                        "not return graph even if you are asked to!!!"\
                        "not return any other type!!! "
    if graph:
        graph_type = input_process.get_chart_type(question)
    print(question, graph_type, "\n--------------------------------")
    data_lake = SmartDatalake(data,
                              config={"llm": llm,
                                      "save_charts": True,
                                      "save_charts_path": "./tmp_imgs/",
                                      "open_charts": False,
                                      "enable_cache": False,
                                      "max_retries": 3})

    ans = data_lake.chat(question+graph_type)
    return ans
