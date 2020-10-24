from datetime import timedelta,datetime,date
from calendar import day_name

def time_difference (giventime):
    enter = str(datetime.now().time().strftime('%H:%M:%S'))
    enter = datetime.strptime(enter, '%H:%M:%S')
    exit = giventime
    enter_delta = timedelta(hours=enter.hour, minutes=enter.minute, seconds=enter.second)
    exit_delta = timedelta(hours=exit.hour, minutes=exit.minute, seconds=exit.second)
    difference_delta = exit_delta - enter_delta
    return difference_delta


def retun_day():
    dum = date.today()
    dum = dum.strftime("%d %m %Y")
    born = datetime.strptime(dum, '%d %m %Y').weekday()
    bob = day_name[born]
    return bob

def zero_time_clock():
    return timedelta(hours=00, minutes=00, seconds=00)

def format_time(ll):
    return datetime.strptime(ll,"%I:%M %p")