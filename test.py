import random 
import time
greetings = ['Здравствуйте господин',
                'Приветствую босс',
                ]
local_time = time.strftime('%H:%M')
local_time_hours = time.strftime('%H')

if local_time_hours == '07':
    print ('Доброе утро')


print(local_time)
print(local_time_hours)
print(random.choice(greetings))
