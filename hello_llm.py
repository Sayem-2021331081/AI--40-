import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
# 1->
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)
# 2->
model = "openai/gpt-oss-20b"
# 3->
role = "user"
prompt = "Do you know Elon Mask"
message = {
    "role": role,
    "content": prompt
}
messages = [message]
# 4->
response = client.chat.completions.create(model=model, messages=messages)
print(response.choices[0].message.content)