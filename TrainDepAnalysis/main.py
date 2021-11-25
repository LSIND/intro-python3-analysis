import datetime
from collections import Counter

def getdata():
    deps = []
    with open('depsalem.txt') as infile:
        for row in infile.readlines():
            departure = getdep(row)
            if departure:
                deps.append(departure)
    return deps

def getdep(row):
    if row[0] == '*':
        return None

    departure = row.strip().split('\t')
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


def main():
    print("-"*40)
    dep_lisoftup = getdata() # list of tuples

    empty = [d for d in dep_lisoftup if d[1] == None]
    print("Not operated trips: ", len(empty))
    countdays = []
    for i in empty:
        countdays.append(i[3])
    daysnotoper = Counter(countdays)
    print("Counting not departed trains by day of week:\n", daysnotoper.most_common())

    print("-"*40)

    dep_lisoftup = [d for d in dep_lisoftup if d[1]]
    ontime = [d for d in dep_lisoftup if d[1] == d[0]]
    late = [d for d in dep_lisoftup if d[1] > d[0]]
    nextday = [d for d in dep_lisoftup if d[0].day != d[1].day]
    print('''Departed trains: {} 
On time departure: {}
Late departure: {}
Next day departure: {}'''.format(len(dep_lisoftup),
                                   len(ontime),
                                   len(late),
                                   len(nextday)))


main()
