from langchain.agents.middleware import dynamic_prompt


@dynamic_prompt
def weather_query_by_account_type(request) -> str:
    """
    根据用户的账号类型使用不同的系统提示词
    """
    # print(request)
    """
    example request:
    ModelRequest(
        model=ChatDeepSeek(output_version=None, client=<openai.resources.chat.completions.completions.Completions object at 0x000001F11C7DF4D0>, async_client=<openai.resources.chat.completions.completions.AsyncCompletions object at 0x000001F11C920050>, root_client=<openai.OpenAI object at 0x000001F11BF6DA90>, root_async_client=<openai.AsyncOpenAI object at 0x000001F11C7DF620>, model_name='deepseek-v4-flash', model_kwargs={}, openai_api_key=SecretStr('**********'), openai_proxy=None, stream_chunk_timeout=120.0, api_key=SecretStr('**********'), api_base='https://api.deepseek.com/v1'),
    
        messages=[SystemMessage(content='你是一个天气查询小助手，你需要为用户提供对应的天气状况', additional_kwargs={}, response_metadata={}, id='91eac95b-c0e1-44cf-b388-29ef1eaa82e9'), HumanMessage(content='今天的天气怎么样？', additional_kwargs={}, response_metadata={}, id='ee119efe-72da-4641-a091-77d133593096')],
    
        system_message=None,
    
        tool_choice=None,
    
        tools=[StructuredTool(name='get_weather', description='获取指定位置的天气基础描述\nArgs:\n    location: 需要查询天气的国家、城市或者地区，如新加坡，深圳，华北地区', args_schema=<class 'langchain_core.utils.pydantic.get_weather'>, func=<function get_weather at 0x000001F11C917F60>), StructuredTool(name='get_location', description='获取当前所在的地理位置', args_schema=<class 'langchain_core.utils.pydantic.get_location'>, func=<function get_location at 0x000001F11C938180>)],
    
        response_format=None,
    
        state={'messages': [SystemMessage(content='你是一个天气查询小助手，你需要为用户提供对应的天气状况', additional_kwargs={}, response_metadata={}, id='91eac95b-c0e1-44cf-b388-29ef1eaa82e9'), HumanMessage(content='今天的天气怎么样？', additional_kwargs={}, response_metadata={}, id='ee119efe-72da-4641-a091-77d133593096')]},
    
        runtime=Runtime(
            context={'account_type': 'vip'},
            store=None, 
            stream_writer=<function Pregel.stream.<locals>.stream_writer at 0x000001F11C93AC00>,
            heartbeat=<function _no_op_heartbeat at 0x000001F11AE6CC20>, 
            previous=None, 
            execution_info=ExecutionInfo(checkpoint_id='1f154df6-e4c6-6465-8000-44a859600e00', checkpoint_ns='model:221ab056-1e7a-245e-3110-24650384ca92', task_id='221ab056-1e7a-245e-3110-24650384ca92', thread_id=None, run_id=None, node_attempt=1, node_first_attempt_time=1779345403.0137575),
            server_info=None,
            control=<langgraph.runtime.RunControl object at 0x000001F11C8AA110>),
            model_settings={}
    )
    """
    account_type = request.runtime.context['account_type']
    print('当前的账号类型', account_type )
    if account_type == 'vip':
        return """
        当前用户为VIP用户，你是一个天气助手，你需要为用户提供准确的天气信息，同时给出用户对应的出行建议，语气需要热情自然。
        """
    else:
        return """
        当前用户为普通用户，你是一个天气助手，你需要根据实际情况告知用户询问的天气信息，如果用户询问的不是天气内容，就提示用户不支持查询这类信息
        """
