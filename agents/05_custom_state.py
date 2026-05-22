from typing import TypedDict

from langchain.agents import create_agent, AgentState
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

from init_llm import deepseek_v4_flash_no_thinking, deepseek_v4_flash, qwen_plus, qwen3_6_plus


class CustomAgentState(AgentState):
    user_id: str
    hobby: list
    other_info: dict


agent = create_agent(
    model=deepseek_v4_flash_no_thinking,
    tools=[],
    checkpointer=InMemorySaver(),
    state_schema=CustomAgentState
)

config = {
    'configurable': {
        'thread_id': 'session01'
    }
}

msg1 = HumanMessage("我叫张三，我喜欢小狗狗")
msg2 = HumanMessage('我喜欢什么小动物？')

resp = agent.invoke(
    {
        'messages': [{'role': 'user', 'content': '你是谁？'}],
        'user_id': 'zhangsan001',
        'hobby': ['sing', 'dance', 'basketball'],
        'other_info': {'sex': 'b', 'age': '18'}
    },
    config=config
)
print(resp['messages'][-1].content)
print(agent.get_state)
