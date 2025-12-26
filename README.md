# bot-discord-sap-o-with-IA-integration
A Discord bot with Groq integration, coin system, and log reporting.

# 🐸 Sapão Bot V10 (Ultimate Edition)

Um bot de Discord multifuncional desenvolvido em Python, focado em interatividade com Inteligência Artificial, Música de alta qualidade e um sistema de Economia completo.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Discord.py](https://img.shields.io/badge/Discord.py-2.0%2B-5865F2)
![AI Model](https://img.shields.io/badge/AI-Llama%203.3-orange)
![JSON](https://img.shields.io/badge/Data-JSON-lightgrey?style=flat&logo=json&logoColor=000000)

## ✨ Funcionalidades

### 🧠 Inteligência Artificial & Gestão (Groq API)
- **Chat Inteligente:** Converse com o Sapão usando o modelo `llama-3.3-70b-versatile`. Ele responde de forma curta, engraçada e **jamais admite ser da Meta**.
- **Gestor de Canais (Function Calling):** Cargos de liderança podem pedir para a IA criar ou deletar canais usando linguagem natural (Ex: *"Cria uma sala de voz chamada Reunião"*).
- **Fofoca:** O comando `/fofoca` lê as últimas mensagens do chat e cria um resumo engraçado do que está rolando.
- **Geração de Imagens:** Cria imagens via Pollinations AI com `/imaginar`.

### 🎵 Música (DJ Sapão)
- Reprodução de áudio do YouTube com alta qualidade.
- Comandos: `/tocar [busca/link]` e `/parar`.
- *Requer FFmpeg instalado no sistema.*

### 💰 Economia (MoscaCoins)
- **Ganho Automático:** Ganhe moedas interagindo no chat.
- **Cassino:** Aposte suas moedas na rinha com `/apostar`.
- **Loja de Cargos:** Compre cargos exclusivos com `/loja`.
- **Banco de Dados:** Sistema local em JSON (`banco.json`).
- **Pix:** Transferências entre usuários.

### 🛡️ Moderação & Utilitários
- **Logs de Auditoria:**
  - Mensagens apagadas vão para um canal secreto.
  - Mensagens editadas são registradas no canal de logs.
- **Auto-Mod:** Filtro automático de palavras proibidas.
- **Painel de Cargos:** Menu interativo para auto-atribuição.
- **Limpeza:** Comando `/limpar` para apagar mensagens em massa.

---

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior.
- [FFmpeg](https://ffmpeg.org/download.html) (Necessário para música).
  - **Linux (Arch/CachyOS):** `sudo pacman -S ffmpeg`
  - **Ubuntu/Debian:** `sudo apt install ffmpeg`
  - **Windows:** Adicione o `.exe` ao PATH.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/marcojunior-spl/bot-discord-sap-o-with-IA-integration](https://github.com/marcojunior-spl/bot-discord-sap-o-with-IA-integration)
   cd bot-discord-sap-o-with-IA-integration

```

2. **Instale as dependências:**
Crie um ambiente virtual (recomendado) e instale:
```bash
python -m venv venv
source venv/bin/activate  # Linux
# .\venv\Scripts\activate # Windows
pip install -r requirements.txt

```


3. **Configure as Variáveis de Ambiente:**
Crie um arquivo chamado `.env` na raiz e adicione suas chaves:
```env
DISCORD_TOKEN=seu_token_aqui
GROQ_KEY=sua_chave_groq_aqui

```


4. **Configuração de IDs:**
No arquivo `sapao_bot.py`, ajuste:
* `ID_CANAL_...`: IDs dos canais de logs e boas-vindas.
* `IDS_CARGOS_GERENTES`: Lista de IDs de cargos que podem mandar a IA criar canais.
* `CARGOS_CONFIG` e `LOJA_ITENS`: Configure os preços e cargos da loja.



## Como Rodar

**No Terminal:**

```bash
python sapao_bot_V10.py

```

**No Linux (Systemd Service):**

```bash
systemctl --user start sapao-bot-V10.service

```

---

## 📝 Lista de Comandos

| Comando | Descrição |
| --- | --- |
| `/sapao [msg]` | Pergunta algo para a IA (Admins podem gerenciar canais). |
| `/fofoca` | A IA resume as últimas 30 mensagens do chat. |
| `/imaginar [prompt]` | Gera uma imagem via IA. |
| `/tocar [nome]` | Toca uma música do YouTube. |
| `/apostar [valor]` | Tenta a sorte no cassino (50% de chance). |
| `/loja [item]` | Compra cargos com MoscaCoins. |
| `/saldo` | Mostra suas moedas. |
| `/pix [user] [valor]` | Transfere moedas. |
| `/painel_cargos` | Cria o menu de cargos (Admin). |
| `!sinc` | Sincroniza os comandos Slash (Manual). |

# Desenvolvido com 💚 e 🦟.

ENGLISH
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

# 🐸 Sapão Bot V10

A multifunctional Discord bot developed in Python, featuring AI interactivity, Channel Management via LLM, Music, and a complete Economy system.

## ✨ Features

### 🧠 AI & Management (Groq API)

* **Smart Chat:** Chat with Sapão using Llama 3. It replies with a distinct personality.
* **AI Channel Manager:** Authorized roles can ask the AI to create or delete channels using natural language (e.g., *"Create a voice channel named Gaming"*).
* **Gossip (Fofoca):** Summarizes recent chat history with humor.
* **Image Gen:** Text-to-image via Pollinations AI.

### 🎵 Music

* High-quality YouTube audio playback using `yt-dlp` and `ffmpeg`.

### 💰 Economy (MoscaCoins)

* **Passive Income:** Earn coins by chatting.
* **Casino:** Gamble your coins with `/apostar`.
* **Shop:** Buy roles with `/loja`.
* **Banking:** Local JSON database with transfers via `/pix`.

---

## 📝 Command List

| Command | Description |
| --- | --- |
| `/sapao [msg]` | Chat with AI (Managers can create channels). |
| `/fofoca` | Summarizes recent chat messages. |
| `/imaginar [prompt]` | Generates an AI image. |
| `/apostar [val]` | Bet coins in the casino. |
| `/loja [item]` | Buy roles from the shop. |
| `/saldo` | Check balance. |
| `/pix` | Transfer coins. |

# Developed with 💚 and 🦟
