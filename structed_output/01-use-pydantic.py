from typing import Literal

from pydantic import BaseModel, Field

from init_llm import qwen_plus
from tools.static_tools import get_weather


class Actor(BaseModel):
    """
    演员信息
    """
    name: str = Field(description='演员姓名，需要使用中文转译英文')
    sex: Literal["男", "女"] = Field(description='演员性别，男或女')


class Movie(BaseModel):
    """
    电影相关信息
    """
    director: str = Field(description='电影的导演，需要使用中文，如：克劳德·斯汀')
    release_date: str = Field(description='上映时间，示例：2001年5月')
    rate: float = Field(description='电影评分，示例：9.1')
    actors: list[Actor] = Field(description='主演列表，列举主演即可，如男主，女主，男儿，女二这些')


qwen_plus.bind_tools([get_weather])

structed_output_model = qwen_plus.with_structured_output(Movie)

resp = structed_output_model.invoke("给我介绍一下《绿皮书》")
# <class '__main__.Movie'>
print(type(resp))
# director='彼得·法雷利' release_date='2018-09-11（多伦多电影节首映）；2019-03-01（中国大陆）' rate=8.9 actors=[Actor(name='维果·莫腾森', sex='男'), Actor(name='马赫沙拉·阿里', sex='男')]
print(resp)
