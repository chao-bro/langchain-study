from langchain.chat_models import init_chat_model

from env_loader import DEEPSEEK_BASE_URL, DEEPSEEK_API_KEY, QWEN_BASE_URL, QWEN_API_KEY

deepseek_v4_flash = init_chat_model(
    model='deepseek-v4-flash',
    model_provider='deepseek',
    base_url=DEEPSEEK_BASE_URL,
    api_key=DEEPSEEK_API_KEY
)

deepseek_v4_pro = init_chat_model(
    model='deepseek-v4-pro',
    model_provider='deepseek',
    base_url=DEEPSEEK_BASE_URL,
    api_key=DEEPSEEK_API_KEY
)

qwen3_6_plus = init_chat_model(
    model='qwen3.6-plus',
    model_provider='openai',
    base_url=QWEN_BASE_URL,
    api_key=QWEN_API_KEY
)

qwen_plus = init_chat_model(
    model='qwen-plus',
    model_provider='openai',
    base_url=QWEN_BASE_URL,
    api_key=QWEN_API_KEY
)
