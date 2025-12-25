# bot-discord-sap-o-with-IA-integration
A Discord bot with Groq integration, coin system, and log reporting.

# 🐸 Sapão Bot V9

Um bot de Discord multifuncional desenvolvido em Python, focado em interatividade com Inteligência Artificial, Música de alta qualidade e um sistema de Economia divertido.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Discord.py](https://img.shields.io/badge/Discord.py-2.0%2B-5865F2)
![AI Model](https://img.shields.io/badge/AI-Llama%203.3-orange)

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
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPO.git](https://github.com/SEU_USUARIO/NOME_DO_REPO.git)
   cd NOME_DO_REPO

ENGLISH
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
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
   git clone [https://github.com/YOUR_USERNAME/REPO_NAME.git](https://github.com/YOUR_USERNAME/REPO_NAME.git)
   cd REPO_NAME

   
