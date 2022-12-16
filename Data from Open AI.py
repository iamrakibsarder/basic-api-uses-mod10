import os
import openai

openai.api_key = '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'
prompt = input("Enter your sentence to get Blog : ")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
output = response.get('choices')[0].get('text')
print(output)