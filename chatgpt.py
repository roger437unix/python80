# https://www.youtube.com/watch?v=ZwfZlqTzsuA
# https://platform.openai.com/docs/api-reference/authentication

from chatgpt_key import API_KEY
import requests, json

headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}

# link = 'https://api.openai.com/v1/models'
# req = requests.get(link, headers=headers)

id_modelo = "gpt-3.5-turbo"

link = 'https://api.openai.com/v1/chat/completions'

body_mensagem = {
	"model" : id_modelo,
	"messages" : [{"role": "user", "content": "Me traga somente o nome de 50 paises do mundo"}]
}

body_mensagem = json.dumps(body_mensagem)

req = requests.post(link, headers=headers, data=body_mensagem)

resposta = req.json()
# print(resposta['choices'][0]['message']['content'])
print(resposta)
