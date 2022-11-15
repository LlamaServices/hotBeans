def reptime(seconds):
    if seconds < 0: neg = -1
    else: neg = 1
    seconds = abs(seconds)
    hours = seconds//3600
    minutes = (seconds%3600)//60
    remseconds = (seconds%3600)%60
    return '{:d}:{:02d}:{:02d}'.format(neg*hours, minutes, remseconds)

print(reptime(100001))