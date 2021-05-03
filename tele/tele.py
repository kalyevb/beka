import os
import sys
import json
import youtube_dl
import telepotpro
from random import randint
from multiprocessing import Process
from youtubesearchpython import SearchVideos
from datetime import datetime


bot = telepotpro.Bot("1544498260:AAGg6Chm_35MatLh1tM3qu7N6jpuYaUTwxQ")



def startMsg(chat_id, first_name, message):
    bot.sendMessage(chat_id, 'Привет, ' + first_name + '!\n\n'
     'Напиши:\n\n'
     '"*/m* Название песни"  or\n'
     '"*/m* Название автора,название песни"\n\n'
     'И я скачаю тебе ее. 🎶', parse_mode='Markdown')
    save_info_mp4(message)





def errorMsg(chat_id, error_type):
    if error_type == 'too_long':
        bot.sendMessage(chat_id, '‼️ *Ой! Слишком длинное видео для скачивания!*\n'
                                 'Закажи что-нибудь не более 30 минут.', parse_mode='Markdown')

    if error_type == 'spotify_command':
        bot.sendMessage(chat_id, "‼️ *Ой! Бот не поддерживает ссылки Spotify!*\n"
                                 'Try: "*/m* Название песни"\n'
                                 'or: "*/m* Название песни"', parse_mode='Markdown')

    if error_type == 'invalid_command':
        bot.sendMessage(chat_id, '‼️ *Ой! Вы ввели неправильную команду!*\n'
                                 'Try: "*/m* Название пенси"\n'
                                 'or: "*/m* Название автора, название песни"', parse_mode='Markdown')


def downloadMusic(file_name, link):
    ydl_opts = {
        'outtmpl': './' + file_name,
        'format': 'bestaudio/best',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'prefer_ffmpeg': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=True)


def validMusicInput(userInput, chat_id, chat_type):
    # Search music on youtube
    search = SearchVideos(userInput[6:], mode="json", max_results=9)
    resultados = json.loads(search.result())

    # Get video duration
    duration = resultados['search_result'][0]['duration'].split(':')
    splitCount = len(duration)

    if int(duration[0]) < 30 and splitCount < 10:
        title = resultados['search_result'][0]['title']
        link = resultados['search_result'][0]['link']
        file_name = title + ' - ' + str(randint(0, 999999)) + '.mp3'

        bot.sendMessage(chat_id, '🎵 ' + title + '\n' + '🔗 ' + link)
        DownloadingMsg = bot.sendMessage(chat_id, '⬇️ Downloading... '
                                                  '\n_(this may take a while.)_', parse_mode='Markdown')

        # Download the music
        downloadMusic(file_name, link)

        bot.sendAudio(chat_id, audio=open(file_name, 'rb'))
        bot.deleteMessage((chat_id, DownloadingMsg['message_id']))
        bot.sendMessage(chat_id, '✅ Готова! Не забудь поблагодорить Бектура')

        print("Готова! Не забудь поблагодорить Бектура")
        os.remove(file_name)

    else:
        errorMsg(chat_id, 'too_long')

    pass


def recebendoMsg(msg,):
    userInput = msg['text']
    chat_id = msg['chat']['id']
    first_name = msg['from']['first_name']
    chat_type = msg['chat']['type']

    if chat_type == 'group':
        if '@ForZymaBot' in userInput:
            userInput = userInput.replace('@ForZymaBot', '')

    if userInput.startswith('/start'):
        # Shows start dialog
        startMsg(chat_id, first_name)

    elif userInput.startswith('/m') and userInput[6:] != '':
        if 'open.jango.com' in userInput[6:]:
            errorMsg(chat_id, 'jango_command')

        else:
            # Process the music
            validMusicInput(userInput, chat_id, chat_type)

    else:
        # Invalid command
        errorMsg(chat_id, 'invalid_command')

    pass


def save_info_mp4(message):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    data_file = open('data_mp4.txt', 'a+')
    data_file.write(f'{date}\t{message.from_user.first_name} {message.from_user.last_name}\t{message.text}\n')
    data_file.close()

def main(msg):
    main_process = Process(target=recebendoMsg, args=(msg,))
    main_process.start()


bot.message_loop(main, run_forever=True)