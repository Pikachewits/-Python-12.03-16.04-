duration = int(input('Введите промежуток времени в секундах: '))

if duration >= 0 and duration < 60:
    print(str(duration) + ' сек')
elif duration >= 60 and duration < 3600:
    minutes = duration // 60
    seconds = duration % 60
    print(str(minutes) + ' мин ' + str(seconds) + ' сек')
elif duration >= 3600 and duration < 86400:
    hours = duration // 3600
    minutes = duration % 3600 / 60
    minutes_result = int(minutes)
    seconds = minutes % 1 * 60
    seconds_result = int(seconds)
    print(str(hours) + ' час ' + str(minutes_result) + ' мин ' + str(seconds_result) + ' сек ')
elif duration >= 86400 and duration < 604800:
    days = duration // 86400
    hours = duration % 86400 / 3600
    hours_result = int(hours)
    minutes = hours % 1 * 60
    minutes_result = int(minutes)
    seconds = minutes % 1 * 60
    seconds_result = int(seconds)
    print(str(days) + ' дн ' + str(hours_result) + ' час ' + str(minutes_result) + ' мин ' + str(seconds_result) + ' сек ')