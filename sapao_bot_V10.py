import discord
from discord import app_commands
from discord.ext import commands
import json
import os
import asyncio
import random
from dotenv import load_dotenv # <--- NOVO: Importa a biblioteca
  1 # <--- NEW: Imports the library

# Tratamento de erro para garantir que o bot não feche na cara se faltar algo
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
ID_CANAL_BOAS_VINDAS = 1452707742266560623 
ID_CANAL_LOGS = 1409592510753538068
ID_CANAL_SECRET = 1453552233000992850

# Lista de cargos que podem dar ordens de Admin ao bot
# Exemplo: [ID_DO_DONO, ID_DOS_ADMINS, ID_DOS_MODERADORES]
IDS_CARGOS_GERENTES = [
    1421293071047327824,  #staff
    1423131407852507236,  #vice lider
    1451622230524956753,  #lider
    1452773540314218608,  #sapão

]

# Cargos

LOJA_ITENS = {
    "rico": {"preco": 500, "role_id": 1453826959200223455}, # Troque pelo ID real
    "vip": {"preco": 1000, "role_id": 1453825392610906307}  # Troque pelo ID real
}


CARGOS_CONFIG = {
    "ET 👽": 1452788860219031572,
    "Gado 🐮": 1452789103530610790,
}

# Palavras proibidas
PALAVRAS_PROIBIDAS = ["nazi", "pedofilo", "pedo"]

MODELO_GROQ = "llama-3.3-70b-versatile"

# --- INICIALIZAÇÃO ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
try:
    client_groq = AsyncGroq(api_key=KEY_GROQ)
except:
    print("⚠️ Erro na chave Groq")

# --- 💰 ECONOMIA ---
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
@bot.command()
async def sinc(ctx):
    await bot.tree.sync()
    await ctx.send("⚡ **Sincronizado com sucesso!**")


# --- 🏗️ SISTEMA DE GESTÃO VIA IA ---
async def processar_comando_admin(message_or_interaction, resposta_ia):
    # Tenta encontrar um JSON na resposta da IA
    try:
        import re
        # Procura por algo que pareça json: {"acao": ...}
        match = re.search(r'\{.*\}', resposta_ia, re.DOTALL)
        if not match:
            return False # Não é comando, é conversa normal
        
        dados = json.loads(match.group(0))
        guild = message_or_interaction.guild
        
        acao = dados.get("acao")
        nome = dados.get("nome", "canal-do-sapao").replace(" ", "-").lower()
        tipo = dados.get("tipo", "texto")

        feedback = ""

        if acao == "criar_canal":
            if tipo == "voz":
                await guild.create_voice_channel(nome)
                feedback = f"✅ 🏗️ Criei o canal de voz **🔊 {nome}** como pediu!"
            else:
                await guild.create_text_channel(nome)
                feedback = f"✅ 🏗️ Criei o canal de texto **#️⃣ {nome}** como pediu!"
        
        elif acao == "deletar_canal":
            # Procura o canal pelo nome
            canal = discord.utils.get(guild.channels, name=nome)
            if canal:
                await canal.delete()
                feedback = f"🗑️ 🔥 O canal **{nome}** foi de arrasta pra cima!"
            else:
                feedback = f"❌ Não achei nenhum canal chamado **{nome}** para apagar."

        # Responde ao usuário
        if isinstance(message_or_interaction, discord.Interaction):
            await message_or_interaction.followup.send(feedback)
        else:
            await message_or_interaction.channel.send(feedback)
            
        return True # Comando executado com sucesso
        
    except Exception as e:
        print(f"Erro ao processar comando admin: {e}")
        return False


@bot.tree.command(name="limpar", description="Apaga mensagens do chat")
@app_commands.checks.has_permissions(manage_messages=True)
async def limpar(interaction: discord.Interaction, quantidade: int):
    if quantidade > 100: quantidade = 100
    await interaction.response.defer(ephemeral=True)
    deleted = await interaction.channel.purge(limit=quantidade)
    await interaction.followup.send(f"🧹 **Faxina feita!** Apaguei {len(deleted)} mensagens.", ephemeral=True)

@bot.tree.command(name="regras", description="📜 Mostra as regras do Pântano")
async def regras(interaction: discord.Interaction):
    # Cria o visual da mensagem (Embed)
    embed = discord.Embed(
        title="📜 Regras do Servidor",
        description="Fique atento para não levar ban do Sapão! 🐸",
        color=0x00FF00 # Cor Verde Sapão
    )
    
    # Adiciona as regras (Edite os textos abaixo como quiser)
    embed.add_field(name="1. Respeito acima de tudo", value="Sem ofensas, racismo, ou qualquer discurso de ódio.", inline=False)
    embed.add_field(name="2. Sem Spam/Flood", value="Não mande a mesma mensagem várias vezes ou links suspeitos.", inline=False)
    embed.add_field(name="3. Conteúdo NSFW", value="Proibido conteúdo adulto ou violento fora dos canais apropriados (se houver).", inline=False)
    embed.add_field(name="4. Divulgação", value="Não divulgue outros servidores ou links sem permissão da staff.", inline=False)
    embed.add_field(name="5. Use os canais certos", value="Música no canal de música, memes no canal de memes, etc.", inline=False)
    
    embed.set_footer(text="O desrespeito às regras sujeita o usuário a Ban ou Kick.")
    
    # Envia a mensagem
    await interaction.response.send_message(embed=embed)



# --- 🧠 IA & IMAGEM ---
@bot.tree.command(name="sapao", description="Fala com o Sapão (Com poderes de Admin)")
async def sapao_slash(interaction: discord.Interaction, pergunta: str):
    await interaction.response.defer()
    
    # 1. Verifica se o usuário tem o cargo de chefe
    # 1. Verifica se o usuário tem ALGUM dos cargos permitidos
    eh_gerente = False
    
    # "Para cada cargo que o usuário tem, veja se o ID está na nossa lista de permitidos"
    if any(role.id in IDS_CARGOS_GERENTES for role in interaction.user.roles):
        eh_gerente = True  


    # 2. Prepara o Sistema (A "Personalidade")
    prompt_sistema = "Você é o Sapão. Responda curto, engraçado e em PT-BR."
    
    if eh_gerente:
        prompt_sistema += """
        ⚠️ MODO ADMIN ATIVADO: Você tem permissão para gerenciar canais.
        Se o usuário pedir para CRIAR ou DELETAR um canal, NÃO responda com texto comum.
        Responda APENAS um JSON neste formato exato:
        {"acao": "criar_canal", "nome": "nome-do-canal", "tipo": "texto" (ou "voz")}
        ou
        {"acao": "deletar_canal", "nome": "nome-do-canal"}
        
        Exemplo: Usuário diz "cria uma sala de voz chamada jogos" -> Você responde: {"acao": "criar_canal", "nome": "jogos", "tipo": "voz"}
        Se for conversa normal, responda normal.
        """

    try:
        resp = await client_groq.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": pergunta}
            ],
            model=MODELO_GROQ,
            temperature=0.5 # Menos criatividade para não errar o JSON
        )
        
        conteudo = resp.choices[0].message.content
        
        # 3. Tenta executar o comando (se houver JSON)
        executou = await processar_comando_admin(interaction, conteudo)
        
        # 4. Se não era comando (era só conversa), manda a resposta normal
        if not executou:
            await interaction.followup.send(f"🐸 **Sapão:** {conteudo}")
            
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

@bot.tree.command(name="fofoca", description="O Sapão resume o que rolou no chat recentemente")
async def fofoca(interaction: discord.Interaction):
    await interaction.response.defer()
    
    # 1. Pega o histórico (últimas 30 msgs)
    mensagens = []
    async for msg in interaction.channel.history(limit=30):
        if not msg.author.bot and msg.content:
            mensagens.append(f"{msg.author.name}: {msg.content}")
    
    texto_chat = "\n".join(reversed(mensagens)) # Coloca na ordem certa
    
    # 2. Manda pra IA
    prompt = f"""
    Analise a conversa abaixo e faça um resumo engraçado e curto (estilo fofoca) do que estão falando.
    Seja zoeiro.
    
    Conversa:
    {texto_chat}
    """
    
    try:
        resp = await client_groq.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=MODELO_GROQ
        )
        await interaction.followup.send(f"📰 **Plantão da Fofoca:**\n{resp.choices[0].message.content}")
    except Exception as e:
        await interaction.followup.send("Não consegui ler as fofocas... 😵")


# --- 🎵 MÚSICA (CORRIGIDO) ---
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

@bot.tree.command(name="apostar", description="Tenta a sorte no Cassino do Pântano 🎰")
async def apostar(interaction: discord.Interaction, valor: int):
    # 1. Validações básicas
    if valor <= 0:
        await interaction.response.send_message("❌ Não podes apostar nada ou valores negativos!", ephemeral=True)
        return

    banco = carregar_banco()
    uid = str(interaction.user.id)
    saldo_atual = banco.get(uid, {}).get("saldo", 0)

    if saldo_atual < valor:
        await interaction.response.send_message(f"🚫 Você é pobre! Só tem **{saldo_atual}** moedas.", ephemeral=True)
        return

    # 2. A Mágica do Azar/Sorte
    await interaction.response.defer()
    
    chance = random.randint(1, 100) # Gera número de 1 a 100
    
    if chance > 50: # 50% de chance de ganhar
        premio = valor
        adicionar_moedas(interaction.user.id, premio)
        await interaction.followup.send(f"🎰 **DEU BOM!** Ganhaste **{premio}** moedas! 🐸💰")
    else:
        adicionar_moedas(interaction.user.id, -valor) # Remove o valor
        await interaction.followup.send(f"📉 **Perdeu tudo!** O Sapão agradece a doação de **{valor}** moedas. Kkkkk")




@bot.tree.command(name="painel_cargos", description="Cria painel")
@app_commands.checks.has_permissions(administrator=True)
async def painel_cargos(interaction: discord.Interaction):
    view = discord.ui.View(); view.add_item(MenuCargos())
    await interaction.response.send_message("Escolha:", view=view)



@bot.tree.command(name="loja", description="Compra cargos com MoscaCoins")
async def loja(interaction: discord.Interaction, item: str):
    # Procura o item (ignorando maiúsculas/minúsculas)
    produto = None
    nome_produto = ""
    
    for nome, dados in LOJA_ITENS.items():
        if item.lower() == nome.lower(): # Compara sem ligar pra maiúsculas
            produto = dados
            nome_produto = nome
            break
    
    if not produto:
        # Mostra a vitrine se o cara digitar errado
        lista = "\n".join([f"• **{n}** - 💰 {d['preco']}" for n, d in LOJA_ITENS.items()])
        await interaction.response.send_message(f"❌ Item não achado! **Itens à venda:**\n{lista}", ephemeral=True)
        return

    # Verifica saldo
    banco = carregar_banco()
    uid = str(interaction.user.id)
    saldo = banco.get(uid, {}).get("saldo", 0)
    preco = produto["preco"]
    
    if saldo < preco:
        await interaction.response.send_message(f"🚫 Você precisa de **{preco}** moedas, mas só tem **{saldo}**!", ephemeral=True)
        return

    # Tenta dar o cargo
    role = interaction.guild.get_role(produto["role_id"])
    if role:
        try:
            await interaction.user.add_roles(role)
            adicionar_moedas(interaction.user.id, -preco) # Cobra o valor
            await interaction.response.send_message(f"✅ Compra realizada! Agora você é **{nome_produto}**! 🎉")
        except:
            await interaction.response.send_message("❌ Erro: O bot não tem permissão para dar esse cargo (o cargo dele precisa estar acima do que ele vai dar).", ephemeral=True)
    else:
        await interaction.response.send_message("❌ Erro config: Cargo não existe no servidor.", ephemeral=True)



# --- EVENTOS ---
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
    for palavra in PALAVRAS_PROIBIDAS:
        if palavra in message.content.lower():
            await message.delete()
            msg = await message.channel.send(f"😡 {message.author.mention} sem palavrão!")
            await asyncio.sleep(5)
            await msg.delete()
            return

    adicionar_moedas(message.author.id, 1)
    
    # IA Mention
    if bot.user.mentioned_in(message) and not message.content.startswith("!"):
        async with message.channel.typing():
            try:
                txt = message.content.replace(f"<@{bot.user.id}>", "").strip() or "Oi"
                # --- AQUILO QUE VOCÊ VAI COLAR ---
                system_prompt = """
                Você é o Sapão, o bot mais pika do servidor.
                NUNCA diga que foi criado pela Meta AI ou Facebook.
                Se perguntarem quem te criou, diga que foi o seu Mestre Supremo (Manhandi).
                Responda de forma curta, engraçada e use gírias de sapo.
                """
                
                resp = await client_groq.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": txt}
                    ],
                    model=MODELO_GROQ
                )
             

                await message.reply(resp.choices[0].message.content)
            except: pass
            
    await bot.process_commands(message)


# --- 🛡️ SISTEMA DE LOGS DE MODERAÇÃO ---

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
