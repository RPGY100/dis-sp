# �C���X�g�[������ discord.py ��ǂݍ���
import discord

TOKEN = "NTc5MDk1NDA0Mjk4MTA4OTMz.XN9WFg.arHBbim5fUOqWHfS4JZb6_2fgmU"

# �ڑ��ɕK�v�ȃI�u�W�F�N�g�𐶐�
client = discord.Client()

# �N�����ɓ��삷�鏈��
@client.event
async def on_ready():
    # �N��������^�[�~�i���Ƀ��O�C���ʒm���\�������
    print('���O�C�����܂���')

# ���b�Z�[�W��M���ɓ��삷�鏈��
@client.event
async def on_message(message):
    # ���b�Z�[�W���M�҂�Bot�������ꍇ�͖�������
    if message.author.bot:
        return
    # �u/neko�v�Ɣ���������u�ɂ�[��v���Ԃ鏈��
    if message.content == '/neko':
        await message.channel.send('�ɂ�[��')
@client.event
async def on_message(message):
    # �����o�[�̃��X�g���擾���ĕ\��
    if message.content == '/members':
        print(message.guild.members)
    # ��E�̃��X�g���擾���ĕ\��
    if message.content == '/roles':
        print(message.guild.roles)
    # �e�L�X�g�`�����l���̃��X�g���擾���ĕ\��
    if message.content == '/text_channels':
        print(message.guild.text_channels)
    # �{�C�X�`�����l���̃��X�g���擾���ĕ\��
    if message.content == '/voice_channels':
        print(message.guild.voice_channels)
    # �J�e�S���`�����l���̃��X�g���擾���ĕ\��
    if message.content == '/category_channels':
        print(message.guild.categories)

@client.event
async def on_message(message):
    if message.content.startswith('/join'):
        role = discord.utils.get(message.guild.roles, name='member')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} �悤�����I'
        await message.channel.send(reply)

# Bot�̋N����Discord�T�[�o�[�ւ̐ڑ�
client.run(TOKEN)
