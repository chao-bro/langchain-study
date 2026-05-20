from typing import Literal, Annotated, TypedDict

from init_llm import qwen_plus
from tools.static_tools import get_weather


class Actor(TypedDict):
    """
    演员信息
    """
    name: Annotated[str, "演员名"]
    sex: Annotated[Literal["男", "女"], "演员性别"]


class Movie(TypedDict):
    """
    电影相关信息
    """
    director: Annotated[str, '电影的导演，需要使用中文，如：克劳德·斯汀']
    release_date: Annotated[str, '上映时间，示例：2001年5月']
    rate: Annotated[float, '电影评分，示例：9.1']
    actors: Annotated[list[Actor], '主演列表，列举主演即可，如男主，女主，男儿，女二这些']


qwen_plus.bind_tools([get_weather])

structed_output_model = qwen_plus.with_structured_output(Movie)

resp = structed_output_model.invoke("给我介绍一下《绿皮书》")
# <class 'dict'>
print(type(resp))
# {'actors': [{'name': '维果·莫腾森', 'sex': '男'}, {'name': '马赫沙拉·阿里', 'sex': '男'}], 'director': '彼得·法雷里', 'rate': 8.9, 'release_date': '2018年11月'}
print(resp)
