# ChatGPT-Bot
- 利用串接 ChatGPT API 製作出聊天程式
- 實作利用 GET / POST request 去取得回應資料 
- 實作利用 python openai 模組去取得回應資料

## 取得 secret key
登入 OpenAI 官網 https://openai.com/
![image](https://github.com/mrisland112/ChatGPT-bot/assets/132718430/6cb647b7-7443-4b13-a6ae-cc2e590798da)

選取 API block，進入 OpenAI platform
![image](https://github.com/mrisland112/ChatGPT-bot/assets/132718430/7abd90d0-b6bb-4722-8cec-b52e264a0e05)

建立 API key，輸入應用程式名稱 create 後，會得到 secret key，需保存下來之後會用到
![image](https://github.com/Nashexplorer/ChatGPT-bot/assets/132718430/2df79239-e987-48b5-9e1a-ddefaed5a2c8)


## 參考 API 使用方式來源
在 OpenAI platform 選 API reference，可以看到詳細的 API 的開發文件
https://platform.openai.com/docs/api-reference
![image](https://github.com/mrisland112/ChatGPT-bot/assets/132718430/2548eab2-34d6-4608-ad34-a4d1ef034cdf)

查看 Models 資訊，可以參考 Models 部分的內容 [GET]
![image](https://github.com/mrisland112/ChatGPT-bot/assets/132718430/be6efc84-d997-4a6d-9718-f9b833e3d3b5)


使用 Completions 功能，可以參考 Completions 部分的內容 [POST]
![image](https://github.com/mrisland112/ChatGPT-bot/assets/132718430/a6411aa8-9e85-4c81-80e5-78a4cbaa2c5a)


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
![image](https://github.com/Nashexplorer/ChatGPT-bot/assets/132718430/fb46cc34-6593-48ee-937b-0975caf5d4c9)

