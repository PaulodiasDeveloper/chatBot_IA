import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="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")

st.title("ChatBot com IA")

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui...")

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []
    
# Adiciona uma mensagem
#st.session_state["lista_mensagens"].append(mensagem)

# Exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    if mensagem["role"] == "user":
        st.chat_message("user").write(mensagem["content"])
    else:
        st.chat_message("assistant").write(mensagem["content"])

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)
    
    
    # Resposta da IA (simulada)
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    print(resposta_modelo)
    resposta_ia = resposta_modelo.choices[0].message.content
    
    # Resposta da IA
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
    
    print(st.session_state["lista_mensagens"])  # Para depuração, pode ser removido depois
# Exibe todas as mensagens