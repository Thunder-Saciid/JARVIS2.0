import os
from openai import OpenAI
import gradio as gr


client = OpenAI(
    api_key = "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"

)

#print(client.models.list())

def gpt_clone(input,history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ''.join(s)
    output = gpt(inp)
    history.append((input,output))
    return history,history

prompt ="what is AI?"

def gpt (prompt):
    chat_completion = client.chat.completions.create(

        messages=[
            {
                "role":"user",
                "content": prompt
            }
        ],
        model = "gpt-3.5-turbo",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return chat_completion.choices[0].message.content


# while True:
#     query = input("Ask me anything: \n")
#     gpt(query)


block = gr.Blocks()

with block:
    gr.Markdown(""" <h1><center> AGI AIAssistant</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state=gr.State()
    submit =gr.Button("SEND")
    submit.click(gpt_clone,inputs=[message,state],outputs=[chatbot,state])

block.launch(debug=True)