def to_min(t):
    set_t = set_time(t, time)
    if time == 'sec':
        return set_t / 60
    elif time == 'min':
        return t
    elif time == 'hours':
        return t * 60
    elif time == 'days':
        return t * 1440

def convert_to_day(not_day, time):
    if time == 'sec':
        return not_day / 86400.
    elif time == 'min':
        return not_day / 1440.
    elif time == 'hours':
        return not_day / 24.
    elif time == 'days':
        return not_day / 1.


def set_time(t, time, timeout):
    tlist = []
    for i in t:
        if timeout == 'days':
            if time == 'sec':
                i = i * 86400
            elif time == 'min':
                i = i * 1440
            elif time == 'hours':
                i = i * 24
            elif time == 'days':
                i = i * 1
        elif timeout ==  'hours':
            i = i / 60
        tlist.append(i)
    return tlist