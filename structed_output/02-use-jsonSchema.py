from init_llm import qwen_plus
from tools.static_tools import get_weather

movie = {
    "title": "movie description",
    'type': 'object',
    'properties': {
        'director': {
            'type': 'string',
            'description': '电影的导演，需要使用中文，如：克劳德·斯汀'
        },
        'release_date': {
            'type': 'string',
            'description': '上映时间，示例：2001年5月'
        },
        'rate': {
            'type': 'number',
            'description': '电影评分，示例：9.1'
        },
        'actors': {
            'title': 'actor description',
            'description': '主演列表，列举主演即可，如男主，女主，男儿，女二这些, 不超过四个',
            'type': 'array',
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "演员名"
                    },
                    "sex": {
                        "type": "string",
                        "enum": ["男", "女"],
                        "description": "演员性别"
                    }
                },
                "required": ["name", "sex"]
            },
        },
    },
    'required': ['title', 'director', 'release_date', 'rate', 'actors']
}

qwen_plus.bind_tools([get_weather])

structed_output_model = qwen_plus.with_structured_output(movie)

resp = structed_output_model.invoke("给我介绍一下《绿皮书》")
# <class 'dict'>
print(type(resp))
# {'actors': [{'name': '维果·莫腾森', 'sex': '男'}, {'name': '马赫沙拉·阿里', 'sex': '男'}, {'name': '琳达·卡德里尼', 'sex': '女'}], 'director': '彼得·法雷里', 'rate': 8.9, 'release_date': '2018年11月'}
print(resp)
