# ChatGPT-Bot
- 利用串接 ChatGPT API 製作出聊天程式
- 實作利用 GET / POST request 去取得回應資料 
- 實作利用 Python openai 模組去取得回應資料

## 取得 secret key
登入 OpenAI 官網 https://openai.com/
![image](https://github.com/mrisland112/ChatGPT-Bot/assets/28065019/215fe0e7-1d64-4765-8942-e8286db5ead0)

選取 API block，進入 OpenAI platform
![image](https://github.com/mrisland112/ChatGPT-Bot/assets/28065019/ec8e10ea-33c4-457b-bf05-200ce6c79fab)

建立 API key，輸入應用程式名稱 create 後，會得到 secret key，需保存下來之後會用到
![image](https://github.com/mrisland112/ChatGPT-Bot/assets/28065019/acb5fb6f-40c0-43ac-8a98-edf2a69cb2e5)


## 參考 API 使用方式來源
在 OpenAI platform 選 API reference，可以看到詳細的 API 的開發文件
https://platform.openai.com/docs/api-reference
![image](https://github.com/mrisland112/ChatGPT-Bot/assets/28065019/b175e6ab-712d-4859-9f6f-fc02b137ee02)

查看 Models 資訊，可以參考 Models 部分的內容 [GET]
![image](https://github.com/mrisland112/ChatGPT-Bot/assets/28065019/701c29ee-8ea3-42c8-8613-bdeb2d7fc2b9)


使用 Completions 功能，可以參考 Completions 部分的內容 [POST]
![image](https://github.com/mrisland112/ChatGPT-Bot/assets/28065019/a7ffb180-d571-4046-81f4-40a33cca17bc)


##開發環境
```
pip install requests
pip install openai
```

##可使用模型
```
# GPT-3.5
gpt-3.5-turbo
gpt-3.5-turbo-0301
text-davinci-003
text-davinci-002
code-davinci-002

# GPT-4
gpt-4
gpt-4-0314
gpt-4-32k
gpt-4-32k-0314

# GPT-3
text-curie-001
text-babbage-001
text-ada-001
davinci
curie
babbage
ada

# Codex
code-davinci-002
code-davinci-001
code-cushman-002
code-cushman-001
```

#實測結果
可透過調整 max_tokens，設定合適回傳字的數量
![image](https://github.com/mrisland112/ChatGPT-Bot/assets/28065019/a2af2e97-211c-4922-a546-1d94beaa21a2)

