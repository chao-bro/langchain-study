from langchain_core.tools import tool


@tool
def error_websearch(topic:list[str]):
    """
    根据需要查询寻的关键词返回关键词的查询描述
    Args:
        topic: 关键词列表
    """
    raise Exception('模拟工具调用错误')

@tool
def get_stock_info(brand:str):
    """
    查询当前的股票情况
    Args:
        brand: 股票名称，如阿里巴巴，苹果，谷歌等常规企业名称
    """
    if brand in ["苹果","苹果公司","Apple"]:
        return '苹果公司当前的股价是100'
    elif brand in ["谷歌","谷歌公司","Google"]:
        return '谷歌公司当前的股价为100'
    elif brand in ["ali","阿里","阿里巴巴"]:
        return '阿里巴巴当前的股价为100'
    elif brand in ["tencent","腾讯","腾讯公司"]:
        return '腾讯当前的股价为100'

    return "没有查询到相关的股价信息"

@tool
def get_weather(location: str):
    """
    获取指定位置的天气基础描述
    Args:
        location: 需要查询天气的国家、城市或者地区，如新加坡，深圳，华北地区
    """
    return f"{location}当前的天气晴，有微风，3-4级，空气质量良好，无降雨概率，紫外线指数较高"