from langchain.agents.middleware import wrap_model_call, ModelResponse, ModelRequest


@wrap_model_call
def dynamic_select_model(request:ModelRequest,handler) -> ModelResponse:
    """
    根据消息的长度动态选择模型
    """
    # TODO 处理消息
    return handler(request)
