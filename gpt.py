import openai
openai.api_key=""

def main(input_to_chatgpt,history):
    global res_content

    messages=[
                {"role":"system","content": "You are a helpful assistant."},
        ]
    
    history.append({"role": "user", "content": input_to_chatgpt})
    messages+=history

    #print(messages)
    print("")
    
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100
    )
    
    res_content=res["choices"][0]["message"]["content"]
    print("chatGPT:",res_content)
    history.append({"role": "assistant", "content": res_content})

if __name__=="__main__":
    input_to_chatgpt=""
    res_content=""
    history = []
    
    while True:
        if input_to_chatgpt != "exit":
            input_to_chatgpt=input('You:')
            main(input_to_chatgpt,history)
        else:
            break
    
    