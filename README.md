# ChatBot com IA

Um chatbot simples e intuitivo desenvolvido com Streamlit e integração com a API da OpenAI (GPT-4).

## 🚀 Funcionalidades

- Interface web interativa e responsiva
- Integração com GPT-4 da OpenAI
- Histórico de conversas em tempo real
- Mensagens persistentes durante a sessão
- Design clean e fácil de usar

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit** - Framework para criação de aplicações web
- **OpenAI API** - Integração com GPT-4
- **Session State** - Gerenciamento de estado da aplicação

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de ter:

- Python 3.8 ou superior instalado
- Conta na OpenAI com API key válida
- Pip para instalação das dependências

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/chatbot-ia.git
cd chatbot-ia
```

2. Instale as dependências:
```bash
pip install streamlit openai
```

3. Configure sua API key da OpenAI:
   - Substitua a chave API no código pela sua própria chave
   - **⚠️ IMPORTANTE**: Nunca compartilhe sua API key publicamente

## 🚀 Como Executar

1. Execute o aplicativo Streamlit:
```bash
streamlit run app.py
```

2. Acesse a aplicação no navegador:
```
http://localhost:8501
```

## 💡 Como Usar

1. Digite sua mensagem no campo de entrada na parte inferior da tela
2. Pressione Enter ou clique no botão de envio
3. Aguarde a resposta da IA
4. Continue a conversa - o histórico será mantido durante a sessão

## 🔒 Segurança

- **Nunca committen sua API key** no repositório
- Considere usar variáveis de ambiente para armazenar credenciais
- Para produção, implemente autenticação adequada

### Exemplo de configuração segura:

```python
import os
from openai import OpenAI

# Use variável de ambiente
api_key = os.getenv("OPENAI_API_KEY")
modelo = OpenAI(api_key=api_key)
```

## 📁 Estrutura do Projeto

```
chatbot-ia/
├── app.py              # Aplicação principal
├── README.md           # Documentação
└── requirements.txt    # Dependências (opcional)
```

## 🔄 Melhorias Futuras

- [ ] Implementar autenticação de usuários
- [ ] Adicionar diferentes modelos de IA
- [ ] Salvar histórico de conversas
- [ ] Implementar temas personalizáveis
- [ ] Adicionar export de conversas
- [ ] Implementar rate limiting

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

**Seu Nome**
- GitHub: [@paulo_roberto](https://github.com/PaulodiasDeveloper)
- LinkedIn: [Paulo Roberto](https://www.linkedin.com/in/paulo-roberto/)

## 🙏 Agradecimentos

- [Streamlit](https://streamlit.io/) pela excelente framework
- [OpenAI](https://openai.com/) pela API poderosa
- Comunidade Python pelo suporte contínuo

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!