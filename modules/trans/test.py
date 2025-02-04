# 使用Deepseek-V3模型进行翻译（如果后期存在需要，可以更换为R1）
import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

api_key = "sk-qgbzvfurvbsagkmonzajvbrpdirervpuznuvelzyadvupwhl"

model_type = "DeepSeek-V3"  # 用V3经典模型
# model_type = "DeepSeek-R1"  # 用R1强推理模型

# 模型随机度（翻译时选择较小值0.3）
temperature = 0.3

# 提示词
prompt = ("请将以下对话翻译成中文，不要添加任何额外的说明或解释(请注意，这是漫画中的对话，请尽可能使用更加强烈和夸张的语气进行翻译，"
          "或是可以根据对话内容自行判断漫画内容类型来决定翻译风格)：")

# 对话内容
chat = ("A: こんにちは、元気ですか？\n"
        "B: はい、元気です。あなたは？\n")

# 将prompt和对话内容拼接到一起
content = prompt + chat

payload = {
    "temperature": temperature,
    "model": "deepseek-ai/{}".format(model_type),
    "messages": [
        {
            "role": "user",
            "content": content
        }
    ]
}
headers = {
    "Authorization": "Bearer {}".format(api_key),
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
