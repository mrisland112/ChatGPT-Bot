import pprint
import openai

openai.api_key = "{API_KEY}"
openai.organization = "org-FrKxqLIjH0qagDIJ2EVRdzi7"

#List model
model_list = openai.Model.list()
# pprint.pprint(model_list)


#Create completion
prompt = None
while True:
    prompt = input(">>")
    if prompt=='end' or not prompt.strip():
        break
    res1 = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        temperature=0
        )

    ans = res1.choices[0]["text"]
    # pprint.pprint(res1)
    print("Output", ans)