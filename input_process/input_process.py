from llm_access.qwen_access import call_llm


def process_question(question):
    ask = question + "Based on the task described, which is most suitable: bar chart, pie chart, line graph, or scatter plot?"\
          +"If you are not sure, use bar chart. Please output only the chart names without any explaination. "
    graph_type = call_llm(ask)
    return question + "，please draw " + graph_type


if __name__ == "__main__":
    print(process_question("几位同事的工资对比"))
