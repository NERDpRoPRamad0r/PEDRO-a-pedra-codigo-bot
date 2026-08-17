import discord
import random

templo = 0
moeda = 0
bye = 0
ola_count = 0 
senha1 = 0 
templo1 = 0

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def flip_coin():
    return random.choice(["cara", "coroa"])

def gen_pass(pass_length):
    elements = "1234567890qwertyuiopasdfghjklçzxcvbnm`{^}:´[~],.;/?+-/*!&$#?=@<>"
    return "".join(random.choice(elements) for _ in range(pass_length))



@client.event
async def on_ready():
    print(f'Pedro a Pedra está online como {client.user}')



@client.event
async def on_message(message):
    global bye, ola_count, moeda, senha1, templo
    if message.author == client.user:
        return

    msg_lower = message.content.lower()
    if "derrepende, você ouve uma voz" in msg_lower:
        await message.channel.send("olá tudo bem! sou PEDRO a pedra, sim, sou uma pedra falante, mas olha, eu posso fazer varias coisas, claro que a maioria delas nao é inutel, claro que não! mas vamos o que importa, como vai a vida? o que você quer que eu faça?") 
        templo = 1
        if "e você ouve uma voz denovo, mas já sabendo de quem é:" in msg_lower:
            await message.channel.send("olá denovo! como vai a vida? o que você quer que eu faça?") 
            return
    elif message.content.lower().startswith('/sair do templo'):
        templo = 0
        bye = 0
        senha1 = 0
        ola_count = 0
        moeda = 0  

    msg_lower = message.content.lower()
    if templo == 1:
            opcoes_senha = ["senha", "uma senha", "quero uma senha", "me dá uma senha"]
            if any(msg_lower.startswith(msg) for msg in opcoes_senha) and templo == 1:
                if senha1 == 0:
                    await message.channel.send(f"Aqui está sua senha: {gen_pass(10)}")
                elif senha1 == 1:
                    await message.channel.send(f"Outra senha? Tá: {gen_pass(10)}")
                elif senha1 == 2:
                    await message.channel.send(f"Mais uma? Tome: {gen_pass(10)}")
                elif senha1 == 3:
                    await message.channel.send(f"JÁ TÔ CANSADO: {gen_pass(10)}")
                elif senha1 == 4:
                    await message.channel.send("CHEGA!!!")
                else:
                    await message.channel.send("JÁ FALEI CHEGA!!!")
                senha1 += 1
                return

            if "pedro a pedra" in msg_lower and ("cara ou coroa" in msg_lower or "gire a moeda" in msg_lower):
                if templo == 1:    
                    resultado = flip_coin()
                if moeda == 0:
                    await message.channel.send(f"Girando... deu **{resultado}**!")
                elif moeda == 3:
                    await message.channel.send(f"Denovoo? Tá, deu **{resultado}**.")
                elif moeda == 4:
                    await message.channel.send(f"Já tá bom, né? Girando... deu **{resultado}**.")
                elif moeda == 5:
                    await message.channel.send("Pelo amor de Deus, PARA!")
                elif moeda == 6:
                    await message.channel.send(f"SE QUER, ENTÃO TOMA! **{resultado}**!")
                elif moeda == 7:
                    await message.channel.send(f"PARAAAAAAAAAA..... **{resultado}**.....")
                moeda += 1
                return

            if msg_lower.startswith('voce quebrou o meu ovo')  or msg_lower.startswith('você quebrou o meu ovo') or msg_lower.startswith('VOCÊ QUEBROU O MEU OVO') or msg_lower.startswith('VOCE QUEBROU O MEU OVO'):
                if templo == 1:  
                    await message.channel.send("lá ele")
                    return

            if msg_lower.startswith('olá') or msg_lower.startswith('ola'):

                if templo == 1:  

                    if ola_count == 0:

                        await message.channel.send("olá!")

                    elif ola_count == 1:

                        await message.channel.send("olá denovo?")

                    elif ola_count == 2:

                        await message.channel.send("vc ja falou olá cara")

                    elif ola_count == 3:

                        await message.channel.send("PARA DE FALAR OLÁ!!")

                    elif ola_count == 4:

                        await message.channel.send("se vc continuar com esse olá, eu vou sair daqui!! há.. eu nao sei sair daqui")

                    elif ola_count == 5:

                        await message.channel.send("quer, saber vou ignorar seu idioma oláles e vou responder de forma respeitosa seu idioma oláles")

                    else:

                        await message.channel.send("olá!")

            

                ola_count += 1

                return



            elif msg_lower.startswith('tchau'):

                if templo == 1:  

                    if bye == 0:

                        await message.channel.send("\U0001f642")

                    elif bye == 1:

                        await message.channel.send("tchau denovo?")

                    elif bye == 2:

                        await message.channel.send("voce ja falou tchau, porque nao vai embora")

                    elif bye == 3:

                        await message.channel.send("PARA DE FALAR TCHAU!!")

                    elif bye == 4:

                        await message.channel.send("para de falar tchau, se nao eu ir embora!! há.. eu nao sei como ir embora")

                    elif bye == 5:

                        await message.channel.send("vou ignorar essa porcaria de idioma e vou responder de forma respeitosa")

                

                    elif ola_count >= 4:

                        await message.channel.send('lalelula!!')
                else:
                    await message.channel.send("\U0001f642")
                bye += 1
                return



            client.run("TOKEN")
