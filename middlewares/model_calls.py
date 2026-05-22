from langchain.agents.middleware import wrap_model_call, ModelResponse, ModelRequest

from init_llm import deepseek_v4_flash, qwen_plus, qwen3_6_plus

basic_model = qwen_plus

advanced_model = qwen3_6_plus


@wrap_model_call
def dynamic_select_model(request: ModelRequest, handler) -> ModelResponse:
    """
    根据消息的长度动态选择模型
    """
    """
    example request object:
    ModelRequest(
        model=ChatDeepSeek(output_version=None, client=<openai.resources.chat.completions.completions.Completions object at 0x00000206B7E3CD70>, async_client=<openai.resources.chat.completions.completions.AsyncCompletions object at 0x00000206B7E3D7F0>, root_client=<openai.OpenAI object at 0x00000206B71AF230>, root_async_client=<openai.AsyncOpenAI object at 0x00000206B7E3CEC0>, model_name='deepseek-v4-flash', model_kwargs={}, openai_api_key=SecretStr('**********'), openai_proxy=None, stream_chunk_timeout=120.0, api_key=SecretStr('**********'), api_base='https://api.deepseek.com/v1'),
    
        messages=[
            SystemMessage(content='你是一个天气查询小助手，你需要为用户提供对应的天气状况', additional_kwargs={}, response_metadata={}, id='09c112fc-239b-4a5f-990b-98ee07a35c5f'), 
            HumanMessage(content='今天的天气怎么样？', additional_kwargs={}, response_metadata={}, id='43dc6f95-cfc0-421b-9120-599b1b2bd6c6')
        ], 
        
        system_message=None,
    
        tool_choice=None, 
        
        tools=[StructuredTool(name='get_weather', description='获取指定位置的天气基础描述\nArgs:\n    location: 需要查询天气的国家、城市或者地区，如新加坡，深圳，华北地区', args_schema=<class 'langchain_core.utils.pydantic.get_weather'>, func=<function get_weather at 0x00000206B7EFD080>), StructuredTool(name='get_location', description='获取当前所在的地理位置', args_schema=<class 'langchain_core.utils.pydantic.get_location'>, func=<function get_location at 0x00000206B7EFD260>)],
    
        response_format=None, 
        
        state={'messages': [SystemMessage(content='你是一个天气查询小助手，你需要为用户提供对应的天气状况', additional_kwargs={}, response_metadata={}, id='09c112fc-239b-4a5f-990b-98ee07a35c5f'), HumanMessage(content='今天的天气怎么样？', additional_kwargs={}, response_metadata={}, id='43dc6f95-cfc0-421b-9120-599b1b2bd6c6')]},
    
        runtime=Runtime(context=None, store=None, stream_writer=<function Pregel.stream.<locals>.stream_writer at 0x00000206B7EFFEC0>, heartbeat=<function _no_op_heartbeat at 0x00000206B63E6A20>, previous=None, execution_info=ExecutionInfo(checkpoint_id='1f154dcc-2cb1-6f74-8000-cdacd4b10eeb', checkpoint_ns='model:f3bf4566-381d-fa17-539f-b25875d0f383', task_id='f3bf4566-381d-fa17-539f-b25875d0f383', thread_id=None, run_id=None, node_attempt=1, node_first_attempt_time=1779344256.2827344), server_info=None, control=<langgraph.runtime.RunControl object at 0x00000206B7A86D10>),
    
        model_settings={}
    )
    """
    # print(request)
    print(f"当前上下文消息条数{len(request.messages)}")
    if len(request.messages) > 3:
        # use another model
        model = advanced_model
    else:
        model = basic_model

    print(f"本次请求使用{model.model_name}")
    return handler(request.override(model=model))
