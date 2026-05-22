from typing import TypedDict

from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage

from init_llm import qwen3_6_plus, deepseek_v4_flash_no_thinking
from middlewares.dynamic_prompt import weather_query_by_account_type
from tools.static_tools import get_weather, get_location


class User(TypedDict):
    account_type: str


agent = create_agent(
    model=deepseek_v4_flash_no_thinking,
    tools=[get_weather, get_location],
    middleware=[weather_query_by_account_type],
    context_schema=User
)

messages = [SystemMessage("你是一个天气查询小助手，你需要为用户提供对应的天气状况"), HumanMessage("深圳的天气怎么样？")]

resp = agent.invoke(
    {'messages': messages},
    context={
        'account_type': 'vip',
    }
)

print('vip', resp['messages'][-1].content)

resp = agent.invoke(
    {'messages': messages},
    context={
        'account_type': 'common',
    }
)
print('common', resp['messages'][-1].content)
