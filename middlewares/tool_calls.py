from langchain.agents.middleware import wrap_tool_call
from langchain_core.messages import ToolMessage
from langgraph.prebuilt.tool_node import ToolCallRequest


@wrap_tool_call
def handle_error(request:ToolCallRequest,handler) -> ToolMessage:
    """
    手动处理 tool_call 的异常
    """
    try:
        return handler(request)
    except Exception as e:
        return ToolMessage(content=f'工具调用失败，{e}')