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
prompt = "Suggest a name for my food company."
#System role
# message_system = {
#     "role": "system",
#     "content": "You are my strict Office colleague who is also my manager"
# }
message_system = {
    "role": "system",
    "content": "You are a brand manager who suggests Bangla name for my food company.name should be in one word.suggest one name only. "
}
message = {
    "role": role,
    "content": prompt
}
messages = [message_system,message]
# 4->
#temperature is by default is 0 meaning safe.range is [0,2]
response = client.chat.completions.create(model=model, messages=messages,temperature=2)
# print(response)
print("######################################################")
answer=response.choices[0].message.content
print(answer)