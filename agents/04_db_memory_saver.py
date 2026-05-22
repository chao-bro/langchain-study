from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from init_llm import qwen3_6_plus

from langgraph.checkpoint.sqlite import SqliteSaver

write_config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
read_config = {"configurable": {"thread_id": "1"}}

with SqliteSaver.from_conn_string("db/langchain.db") as checkpointer:
    checkpointer.setup()
    checkpoint = {
        "v": 4,
        "ts": "2024-07-31T2019.804150+00:00",
        "id": "1ef4f797-8335-6428-8001-8a1503f9b875",
        "channel_values": {
            "my_key": "meow",
            "node": "node"
        },
        "channel_versions": {
            "__start__": 2,
            "my_key": 3,
            "start:node": 3,
            "node": 3
        },
        "versions_seen": {
            "__input__": {},
            "__start__": {
                "__start__": 1
            },
            "node": {
                "start:node": 2
            }
        },
    }

    # store checkpoint
    checkpointer.put(write_config, checkpoint, {}, {})

    # load checkpoint
    checkpointer.get(read_config)

    # list checkpoints
    list(checkpointer.list(read_config))

    agent = create_agent(
        model=qwen3_6_plus,
        tools=[],
        checkpointer=checkpointer
    )

    config = {
        'configurable': {
            'thread_id': 'session01'
        }
    }

    msg1 = HumanMessage("我叫张三，我喜欢小狗狗")
    msg2 = HumanMessage('我喜欢什么小动物？')

    resp = agent.invoke({'messages': [msg1]}, config=config)
    # first round answer 你好，张三！很高兴认识你～🐶 小狗狗确实特别可爱，毛茸茸的又通人性，很多人都会被它们瞬间治愈。你平时最喜欢什么品种的小狗呀？或者有没有正在养/曾经养过的小狗狗？如果有想聊的狗狗日常、养护小知识，或者单纯想分享可爱的照片/故事，随时告诉我哦！
    print('first round answer：', resp['messages'][-1].content)

    resp = agent.invoke({'messages': [msg2]}, config=config)
    # second round answer 你刚才告诉我啦，你喜欢**小狗狗**！🐶 是不是想考考我的记性呢？如果还有其他喜欢的小动物，或者想聊聊狗狗的日常、养护心得，随时跟我说哦～
    print('second round answer：', resp['messages'][-1].content)
