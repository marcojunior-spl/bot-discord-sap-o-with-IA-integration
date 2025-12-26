# bot-discord-sap-o-with-IA-integration
A Discord bot with Groq integration, coin system, and log reporting.

# 🐸 Sapão Bot V9

Um bot de Discord multifuncional desenvolvido em Python, focado em interatividade com Inteligência Artificial, Música de alta qualidade e um sistema de Economia divertido.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Discord.py](https://img.shields.io/badge/Discord.py-2.0%2B-5865F2)
![AI Model](https://img.shields.io/badge/AI-Llama%203.3-orange)
![JSON](https://img.shields.io/badge/Data-JSON-lightgrey?style=flat&logo=json&logoColor=000000)


## ✨ Funcionalidades

### 🧠 Inteligência Artificial (Groq API)
- **Chat Inteligente:** Converse com o Sapão usando o modelo `llama-3.3-70b-versatile` (Llama 3). Ele responde de forma curta, engraçada e em PT-BR.
- **Comando:** `/sapao [pergunta]` ou apenas mencione `@Sapão` no chat.
- **Geração de Imagens:** Cria imagens baseadas em texto usando Pollinations AI via comando `/imaginar`.

### 🎵 Música (DJ Sapão)
- Reprodução de áudio do YouTube com alta qualidade.
- Comandos: `/tocar [busca/link]` e `/parar`.
- *Requer FFmpeg instalado no sistema.*

### 💰 Economia (MoscaCoins)
- **Ganho Automático:** Ganhe moedas enviando mensagens no chat.
- **Banco de Dados:** Sistema local em JSON (`banco.json`).
- **Transferências:** Envie dinheiro para amigos com `/pix`.
- **Saldo:** Verifique sua fortuna com `/saldo`.

### 🛡️ Moderação & Utilitários
- **Logs de Auditoria:**
  - Mensagens apagadas vão para um canal secreto (Anti-snipe).
  - Mensagens editadas são registradas no canal de logs.
- **Auto-Mod:** Filtro automático de palavras proibidas com aviso temporário.
- **Painel de Cargos:** Menu interativo (Dropdown) para auto-atribuição de cargos.
- **Limpeza:** Comando `/limpar` para apagar mensagens em massa.

---

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior.
- [FFmpeg](https://ffmpeg.org/download.html) (Necessário para música).
  - **Linux:** `sudo pacman -S ffmpeg` (Arch) ou `sudo apt install ffmpeg` (Ubuntu).
  - **Windows:** Baixe o `.exe` e coloque na pasta do bot ou adicione ao PATH.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/marcojunior-spl/bot-discord-sap-o-with-IA-integration
   cd bot-discord-sap-o-with-IA-integration

### Instale asdependências: Crie um ambiente virtual (recomendado) e instale:

  ```bash
  pip install -r requirements.txt
  ```

## Conteúdo do requirements.txt

discord.py
groq
yt-dlp
PyNaCl
python-dotenv

### Configure as Variáveis de Ambiente: #Crie um arquivo chamado .env na raiz do projeto e adicione suas chaves (NUNCA suba este arquivo para o GitHub):Hub):CORD_TOKEN=seu_token_aqui

DISCORD_TOKEN=seu_token_aqui
GROQ_KEY=sua_chave_groq_aqui

### Configuração de IDs: No arquivo sapao_bot.py, ajuste os IDs dos canais e cargos do seu servidor:

ID_CANAL_BOAS_VINDAS = 123456789...
ID_CANAL_LOGS = 123456789...
ID_CANAL_SECRET = 123456789...


Como Rodar
No Terminal:

```bash
python3 sapao_bot.py
``` 
### No Linux (Systemd Service): Se configurado como serviço:

```bash
systemctl --user start sapao-bot.service
```

### 📝 Lista de Comandos

Comando,Descrição
/sapao [msg],Pergunta algo para a IA.
/imaginar [prompt],Gera uma imagem via IA.
/tocar [nome],Toca uma música do YouTube.
/parar,Para a música e desconecta.
/saldo,Mostra suas MoscaCoins.
/pix [user] [valor],Transfere moedas.
/limpar [qtd],Apaga mensagens (Admin).
/painel_cargos,Cria o menu de cargos (Admin).
!sinc,Sincroniza os comandos Slash (Manual).

# Desenvolvido com 💚 e 🦟.

ENGLISH
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# 🐸 Sapão Bot V9

A multifunctional Discord bot developed in Python, featuring Artificial Intelligence interactivity, high-quality Music playback, and a fun local Economy system.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Discord.py](https://img.shields.io/badge/Discord.py-2.0%2B-5865F2)
![AI Model](https://img.shields.io/badge/AI-Llama%203.3-orange)

## ✨ Features

### 🧠 Artificial Intelligence (Groq API)
- **Smart Chat:** Talk to Sapão using the `llama-3.3-70b-versatile` model (Llama 3). It is configured to reply with short, funny responses in **PT-BR**.
- **Command:** `/sapao [question]` or just mention `@Sapão` in the chat.
- **Image Generation:** Generates text-to-image content using Pollinations AI via the `/imaginar` command.

### 🎵 Music (DJ Sapão)
- High-quality audio playback from YouTube.
- Commands: `/tocar [search/link]` and `/parar`.
- *Requires FFmpeg installed on the system.*

### 💰 Economy (MoscaCoins)
- **Passive Income:** Earn coins automatically by sending messages in the chat.
- **Database:** Local JSON system (`banco.json`).
- **Transfers:** Send money to friends using `/pix`.
- **Balance:** Check your fortune with `/saldo`.

### 🛡️ Moderation & Utilities
- **Audit Logs:**
  - Deleted messages are sent to a secret channel (Anti-snipe).
  - Edited messages are logged in a public log channel.
- **Auto-Mod:** Automatic filter for forbidden words with temporary warnings.
- **Role Panel:** Interactive Dropdown menu for self-assignable roles.
- **Cleanup:** Bulk delete messages with `/limpar`.

---

## 🛠️ Installation and Configuration

### Prerequisites
- Python 3.8 or higher.
- [FFmpeg](https://ffmpeg.org/download.html) (Required for music).
  - **Linux:** `sudo pacman -S ffmpeg` (Arch) or `sudo apt install ffmpeg` (Ubuntu).
  - **Windows:** Download the `.exe` and place it in the bot's folder or add it to PATH.

### Step-by-Step

1. **Clone the repository:**
   ```bash
   git clone https://github.com/marcojunior-spl/bot-discord-sap-o-with-IA-integration
   cd bot-discord-sap-o-with-IA-integration
   
### install dependencies: Create a virtual environment (recommended) and install:

```bash
pip install -r requirements.txt
```

### Content of requirements.txt:

discord.py
groq
yt-dlp
PyNaCl
python-dotenv


### Configure Environment Variables: Create a file named .env in the project root and add your keys (NEVER upload this file to GitHub):


DISCORD_TOKEN=your_token_here
GROQ_KEY=your_groq_key_here

### ID Configuration: In the sapao_bot.py file, adjust the Channel and Role IDs to match your server:

ID_CANAL_BOAS_VINDAS = 123456789...
ID_CANAL_LOGS = 123456789...
ID_CANAL_SECRET = 123456789...

## How to Run
Terminal:
```bash
python3 sapao_bot.py
```
## Linux (Systemd Service): If configured as a service:

```bash
systemctl --user start sapao-bot.service
```

## 📝 Command List

Command,Description
/sapao [msg],Ask the AI something.
/imaginar [prompt],Generate an AI image.
/tocar [name],Play music from YouTube.
/parar,Stop music and disconnect.
/saldo,Check your MoscaCoins balance.
/pix [user] [value],Transfer coins to another user.
/limpar [qty],Bulk delete messages (Admin).
/painel_cargos,Create the role menu (Admin).
!sinc,Sync Slash commands manually.

# Developed with 💚 and 🦟.
