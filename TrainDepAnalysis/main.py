import datetime
from collections import Counter

def getdata():
    deps = []
    with open('TrainDepAnalysis\depsalem.txt') as infile:
        for row in infile.readlines():
            departure = getdep(row)
            if departure:
                deps.append(departure)
    return deps

def getdep(row):
    if row[0] == '*':
        return None

    departure = row.strip().split('\t')  # ignore train number
    #print(departure)
    planned = datetime.datetime.strptime(departure[1][:-5], '%m/%d/%Y %I:%M %p')
    trainno = departure[0]
    dayofw = departure[1][-3:-1]

    if len(departure) <= 2:
        actual = None
        #return None
    else:
        actual = datetime.datetime.strptime(departure[1][:10] + departure[2], '%m/%d/%Y%I:%M%p')
        if actual < planned:
            actual = actual + datetime.timedelta(days=1)

    return (planned, actual, trainno, dayofw)

if __name__ == '__main__':
    print('-'*40)
    dep_listoftup = getdata() # list of tuples (datetime, datetime, Train No, Dofweek)

    empty = [d for d in dep_listoftup if d[1] == None]
    if empty:
        print(f'Not operated trips: {len(empty)}')
        dow = map(lambda k: k[3], empty)
        days_count = Counter(dow)
        print(f'Not departed trains by day of the week: {days_count.most_common()}')
    else:
        print('All trains were departed.')

    print('-'*40)

    dep_listoftup = [d for d in dep_listoftup if d[1] and d[2]]
    ontime_list = [d for d in dep_listoftup if d[1] == d[0]]
    late_list = [d for d in dep_listoftup if d[1] > d[0]]
    nextday_list = [d for d in dep_listoftup if d[0].day != d[1].day]

    departed = 0
    if dep_listoftup:
        departed = len(dep_listoftup)
    ontime = 0
    if ontime_list:
        ontime = len(ontime_list)
    late = 0
    if late_list:
        late = len(late_list)
    nextday = 0
    if nextday_list:
        nextday = len(nextday_list)

    print(f'''Departed trains: {departed} 
On time departure: {ontime}
Late departure: {late}
Next day departure: {nextday}''')