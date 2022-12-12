import time
import random
import speech_recognition

sr = speech_recognition.Recognizer()

sr.pause_threshold = 0.5

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language= 'ru-RU' )
        return query

    except speech_recognition.UnknownValueError:
        return "Sorry i don't know this command"


def greeting():
    greetings = {'Здравствуйте',
                'Приветствую',
                'Добрый день',
                'Доброе утро',
                'Добрый вечер'}
    print(random.choice(greetings))

    
    # Рандомное приветсвие и определением времени утро,вечер,вечер
    # greetings = ['Здравствуйте господин',
    #             'Приветствую босс',
    #             ]
    # local_time = time.strftime('%H:%M')
    # local_time_hours = time.strftime('%H')

    # if local_time_hours == '07':
    #     print ('Доброе утро')
    
    #print(random.choice(greetings))

# def task_on_txt():
#     print('что добавим В список дел?')

#     query = listen_command()
    
#     with open('todo-list.txt', 'a') as file:
#         file.write(f'{query}\n')
#     return f'Задача {query} добавлена в todo-list!'

query = listen_command()

if query == 'Привет друг':
    print(greeting())
# elif query == 'Добавить задачу':
#     print(task_on_txt)


