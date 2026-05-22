from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage

from init_llm import deepseek_v4_flash
from middlewares.model_calls import dynamic_select_model
from tools.static_tools import get_weather, get_location

agent = create_agent(
    model=deepseek_v4_flash,
    tools=[get_weather, get_location],
    middleware=[dynamic_select_model]
)

messages = [SystemMessage("你是一个天气查询小助手，你需要为用户提供对应的天气状况"), HumanMessage("今天的天气怎么样？")]

resp = agent.invoke({'messages': messages})

# print(type(resp))
for msg in resp['messages']:
    msg.pretty_print()
