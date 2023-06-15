import pprint
import requests

api_secret_key = "{API_KEY}"

headers = {
    "Authorization": f"Bearer {api_secret_key}",
    "OpenAI-Organization": "org-FrKxqLIjH0qagDIJ2EVRdzi7"
    # "Content-Type: application/json"
}

#List model
api_url = "https://api.openai.com/v1/models"
res = requests.get(api_url, headers=headers)
# pprint.pprint(res.json())

#Create completion
prompt = None
while True:
    prompt = input(">>")
    if prompt=='end' or not prompt.strip():
        break
    prompt_data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 1000,
        # "temperature": 0,
        # "top_p": 1,
        # "n": 5,
        # "stream": False,
        # "logprobs": None,
        # "stop": "\n"
    }

    prompt_url = "https://api.openai.com/v1/completions"
    res1 = requests.post(prompt_url, headers=headers, json=prompt_data)
    ans = res1.json()["choices"][0]["text"]
    # pprint.pprint(res1.json())
    print("Output", ans)




