from openai import OpenAI

# Configurações da OpenAI
API_KEY = "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"
client = OpenAI(api_key=API_KEY)

class Openai:
    # Função para enviar mensagem para a OpenAI e obter a resposta
    def send_message_to_openai( message, history ):

        with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()


        response = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=100,
            temperature=0.1,
            messages=[
                {"role": "system","content": "Você é um assistente virtual que irá ajudar o usuário a combater a procrastinação, e melhorar os hábitos de estudo e produtividade. Dê dicas, crie cronogramas, e motive o usuário na concentração de suas tarefas"},
                {"role": "user", "content": message},
            ],
        )
        print(f"resposta : {response.choices[0].message.content} ")
        return  response.choices[0].message.content