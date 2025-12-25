import discord
from discord import app_commands
from discord.ext import commands
import json
import os
import asyncio
from dotenv import load_dotenv # <--- NOVO: Importa a biblioteca
# <--- NEW: Imports the library
try:
    from groq import AsyncGroq
    import yt_dlp
    import urllib.parse
except ImportError:
    print("❌ ERRO: Faltam bibliotecas! Rode: pip install groq yt-dlp PyNaCl")
    exit()

# Carrega as chaves do arquivo .env
# Loads keys from the .env file
load_dotenv() 

# --- ⚙️ CONFIGURAÇÃO ---
# --- ⚙️ CONFIGURATION ---
# O código agora busca a chave no ambiente, não mais no texto
# The code now fetches the key from the environment, no longer from the text
TOKEN_DISCORD = os.getenv("DISCORD_TOKEN")
KEY_GROQ = os.getenv("GROQ_KEY")

# IDs (Configure se mudou algo)
# IDs (Configure if something changed)

#aqui coloque os IDs dos canais escolhidos
# put the IDs of the chosen channels here

ID_CANAL_BOAS_VINDAS = 1452707742266560623 
ID_CANAL_LOGS = 1409592510753538068
ID_CANAL_SECRET = 1453552233000992850

# Cargos
# Roles
CARGOS_CONFIG = {
    "ET 👽": 1452788860219031572,
    "Gaad": 1452789103530610790,
}

# Palavras proibidas
# Forbidden words
PALAVRAS_PROIBIDAS = ["batata", "bug", "salpicão"]

MODELO_GROQ = "llama-3.3-70b-versatile"

# --- INICIALIZAÇÃO ---
# --- INITIALIZATION ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
try:
    client_groq = AsyncGroq(api_key=KEY_GROQ)
except:
    print("⚠️ Erro na chave Groq")

# --- 💰 ECONOMIA ---
# --- 💰 ECONOMY ---
ARQUIVO_BANCO = "banco.json"

def carregar_banco():
    if not os.path.exists(ARQUIVO_BANCO): return {}
    with open(ARQUIVO_BANCO, "r") as f: return json.load(f)

def salvar_banco(dados):
    with open(ARQUIVO_BANCO, "w") as f: json.dump(dados, f, indent=4)

def adicionar_moedas(user_id, quantidade):
    banco = carregar_banco()
    uid = str(user_id)
    if uid not in banco: banco[uid] = {"saldo": 0, "xp": 0}
    banco[uid]["saldo"] += quantidade
    banco[uid]["xp"] += 1
    salvar_banco(banco)

# --- ⚡ COMANDOS GERAIS ---
# --- ⚡ GENERAL COMMANDS ---
@bot.command()
async def sinc(ctx):
    await bot.tree.sync()
    await ctx.send("⚡ **Sincronizado com sucesso!**")

@bot.tree.command(name="limpar", description="Apaga mensagens do chat")
@app_commands.checks.has_permissions(manage_messages=True)
async def limpar(interaction: discord.Interaction, quantidade: int):
    if quantidade > 100: quantidade = 100
    await interaction.response.defer(ephemeral=True)
    deleted = await interaction.channel.purge(limit=quantidade)
    await interaction.followup.send(f"🧹 **Faxina feita!** Apaguei {len(deleted)} mensagens.", ephemeral=True)

# --- 🧠 IA & IMAGEM ---
# --- 🧠 AI & IMAGE ---
@bot.tree.command(name="sapao", description="Fala com o Sapão Inteligente")
async def sapao_slash(interaction: discord.Interaction, pergunta: str):
    await interaction.response.defer()
    try:
        resp = await client_groq.chat.completions.create(
            messages=[
                {"role": "system", "content": "Você é o Sapão. Responda curto, engraçado e em PT-BR."},
                {"role": "user", "content": pergunta}
            ],
            model=MODELO_GROQ,
        )
        await interaction.followup.send(f"🐸 **Você:** {pergunta}\n💬 **Eu:** {resp.choices[0].message.content}")
    except Exception as e:
        await interaction.followup.send(f"Deu ruim no cérebro: {e}")

@bot.tree.command(name="imaginar", description="Cria uma imagem IA")
async def imaginar(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()
    prompt_url = urllib.parse.quote(prompt)
    url_imagem = f"https://image.pollinations.ai/prompt/{prompt_url}?width=1024&height=1024&nologo=true"
    embed = discord.Embed(title=f"🎨 {prompt}", color=0xFF00FF)
    embed.set_image(url=url_imagem)
    embed.set_footer(text=f"Pedido por {interaction.user.name}")
    await interaction.followup.send(embed=embed)

# --- 🎵 MÚSICA (CORRIGIDO) ---
# --- 🎵 MUSIC (FIXED) ---
yt_dlp_opts = {'format': 'bestaudio/best', 'noplaylist': True, 'quiet': True}
ffmpeg_opts = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

@bot.tree.command(name="tocar", description="Toca música do YouTube")
async def tocar(interaction: discord.Interaction, busca: str):
    if not interaction.user.voice:
        await interaction.response.send_message("❌ Entre na voz primeiro!", ephemeral=True)
        return
    await interaction.response.defer()
    
    canal_voz = interaction.user.voice.channel
    if not interaction.guild.voice_client: 
        await canal_voz.connect()
    
    vc = interaction.guild.voice_client
    
    with yt_dlp.YoutubeDL(yt_dlp_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{busca}", download=False)['entries'][0]
            url2 = info['url']
            titulo = info['title']
            
            if vc.is_playing(): vc.stop()
            vc.play(discord.FFmpegPCMAudio(url2, **ffmpeg_opts))
            await interaction.followup.send(f"🎵 **Tocando:** {titulo}")
        except Exception as e:
            await interaction.followup.send(f"❌ Erro ao tocar: {e}")

@bot.tree.command(name="parar", description="Para a música")
async def parar(interaction: discord.Interaction):
    if interaction.guild.voice_client:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("🛑 Parei!")
    else: 
        await interaction.response.send_message("Já tô quieto!", ephemeral=True)

# --- 💰 ECONOMIA & CARGOS ---
# --- 💰 ECONOMY & ROLES ---
@bot.tree.command(name="saldo", description="Vê suas moedas")
async def saldo(interaction: discord.Interaction):
    banco = carregar_banco()
    saldo = banco.get(str(interaction.user.id), {}).get("saldo", 0)
    await interaction.response.send_message(f"💰 Você tem **{saldo} MoscaCoins**!")

@bot.tree.command(name="pix", description="Transfere moedas")
async def pix(interaction: discord.Interaction, amigo: discord.User, valor: int):
    if valor <= 0:
        await interaction.response.send_message("Valor inválido!", ephemeral=True); return
    
    banco = carregar_banco()
    rem = str(interaction.user.id)
    if banco.get(rem, {}).get("saldo", 0) < valor:
        await interaction.response.send_message("🚫 Sem grana!", ephemeral=True); return
    
    adicionar_moedas(interaction.user.id, -valor)
    adicionar_moedas(amigo.id, valor)
    await interaction.response.send_message(f"💸 Pix de {valor} para {amigo.mention}!")

class MenuCargos(discord.ui.Select):
    def __init__(self):
        opcoes = [discord.SelectOption(label=n, value=str(i)) for n, i in CARGOS_CONFIG.items()]
        super().__init__(placeholder="Selecione...", options=opcoes)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        for n, i in CARGOS_CONFIG.items():
            r = interaction.guild.get_role(i)
            if r and str(i) in self.values and r not in interaction.user.roles:
                await interaction.user.add_roles(r)
        await interaction.followup.send("✅ Cargos dados!", ephemeral=True)

@bot.tree.command(name="painel_cargos", description="Cria painel")
@app_commands.checks.has_permissions(administrator=True)
async def painel_cargos(interaction: discord.Interaction):
    view = discord.ui.View(); view.add_item(MenuCargos())
    await interaction.response.send_message("Escolha:", view=view)

# --- EVENTOS ---
# --- EVENTS ---
@bot.event
async def on_ready():
    print(f'🐸 Sapão V9 (FULL) Logado como {bot.user}')
    try:
        await bot.tree.sync()
    except: pass

@bot.event
async def on_member_join(member):
    canal = bot.get_channel(ID_CANAL_BOAS_VINDAS)
    if canal:
        embed = discord.Embed(title="Bem-vindo(a)!", description=f"{member.mention} chegou no pântano!", color=0x00FF00)
        if member.avatar: embed.set_thumbnail(url=member.avatar.url)
        await canal.send(embed=embed)
    adicionar_moedas(member.id, 10)

@bot.event
async def on_message(message):
    if message.author.bot: return
    
    # Auto-Mod
    # Auto-Mod
    for palavra in PALAVRAS_PROIBIDAS:
        if palavra in message.content.lower():
            await message.delete()
            msg = await message.channel.send(f"😡 {message.author.mention} sem palavrão!")
            await asyncio.sleep(5)
            await msg.delete()
            return

    adicionar_moedas(message.author.id, 1)
    
    # IA Mention
    # AI Mention
    if bot.user.mentioned_in(message) and not message.content.startswith("!"):
        async with message.channel.typing():
            try:
                txt = message.content.replace(f"<@{bot.user.id}>", "").strip() or "Oi"
                resp = await client_groq.chat.completions.create(
                    messages=[{"role":"system","content":"Sapão aqui. Resposta curta."}, {"role":"user","content":txt}],
                    model=MODELO_GROQ
                )
                await message.reply(resp.choices[0].message.content)
            except: pass
            
    await bot.process_commands(message)


# --- 🛡️ SISTEMA DE LOGS DE MODERAÇÃO ---
# --- 🛡️ MODERATION LOG SYSTEM ---

@bot.event
async def on_message_delete(message):
    if message.author.bot: return
    canal_logs = bot.get_channel(ID_CANAL_SECRET)
    if canal_logs:
        embed = discord.Embed(title="🗑️ Mensagem Apagada", color=0xFF0000)
        embed.add_field(name="Autor:", value=message.author.mention, inline=True)
        embed.add_field(name="Canal:", value=message.channel.mention, inline=True)
        embed.add_field(name="Conteúdo:", value=message.content or "[Sem conteúdo/Imagem]", inline=False)
        embed.set_footer(text=f"ID do Usuário: {message.author.id}")
        await canal_logs.send(embed=embed)

@bot.event
async def on_message_edit(before, after):
    if before.author.bot or before.content == after.content: return
    canal_logs = bot.get_channel(ID_CANAL_LOGS)
    if canal_logs:
        embed = discord.Embed(title="📝 Mensagem Editada", color=0xFFFF00)
        embed.add_field(name="Autor:", value=before.author.mention, inline=True)
        embed.add_field(name="Canal:", value=before.channel.mention, inline=True)
        embed.add_field(name="Antes:", value=before.content, inline=False)
        embed.add_field(name="Depois:", value=after.content, inline=False)
        await canal_logs.send(embed=embed)

if __name__ == "__main__":
    bot.run(TOKEN_DISCORD)
