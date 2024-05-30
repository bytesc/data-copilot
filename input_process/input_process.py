from llm_access.LLM import llm
from llm_access.call_llm_test import call_llm


def get_chart_type(question):
    ask = question + "Based on the task described, which is most suitable: " \
                     "bar chart, pie chart, line graph, or scatter plot?" \
                     "You can only choice one of them. "\
                     "If you really not sure, you can choice a ramdom one, but do not suggest more than one" \
                    "Please output only the chart names without any explanation. "

    graph_type = call_llm(ask, llm)
    return ", please draw " + graph_type


if __name__ == "__main__":
    print(get_chart_type("几位同事的工资对比"))
