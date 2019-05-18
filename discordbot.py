# インストールした discord.py を読み込む
import discord

TOKEN = "NTc5MDk1NDA0Mjk4MTA4OTMz.XN9WFg.arHBbim5fUOqWHfS4JZb6_2fgmU"

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
@client.event
async def on_message(message):
    # メンバーのリストを取得して表示
    if message.content == '/members':
        print(message.guild.members)
    # 役職のリストを取得して表示
    if message.content == '/roles':
        print(message.guild.roles)
    # テキストチャンネルのリストを取得して表示
    if message.content == '/text_channels':
        print(message.guild.text_channels)
    # ボイスチャンネルのリストを取得して表示
    if message.content == '/voice_channels':
        print(message.guild.voice_channels)
    # カテゴリチャンネルのリストを取得して表示
    if message.content == '/category_channels':
        print(message.guild.categories)

@client.event
async def on_message(message):
    if message.content.startswith('/join'):
        role = discord.utils.get(message.guild.roles, name='member')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} ようこそ！'
        await message.channel.send(reply)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
