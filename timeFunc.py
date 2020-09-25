import datetime
import tts2

print('')

def welcome():
    currentTime =  datetime.datetime.now()

    if(currentTime.hour < 12):
        tts2.speak('Good Morning sir!')
    elif(currentTime.hour < 18):
        tts2.speak('Good afternoon sir!')
    else:
        tts2.speak('good evening sir!')

def exec(param):
    currentTime =  datetime.datetime.now()

    if(param == 'day'):
        return currentTime.day
    elif(param == 'month'):
        return currentTime.month
    elif(param == 'year'):
        return currentTime.year
    elif(param == 'hour'):
        return currentTime.hour
    elif(param == 'minute'):
        return currentTime.minute
    elif(param == 'time'):
        return (str(currentTime.hour) + ' hours and ' + str(currentTime.minute) + ' minutes')
    elif(param == 'date'):
        return (str(currentTime.day) + str(currentTime.month) + str(currentTime.year))
    else:
        return 'invalid'

