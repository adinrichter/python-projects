from datetime import datetime, timedelta
from pytz import timezone


def getGMT():
    return datetime.now(timezone('Etc/GMT'))

def getTime(location):
    PDX = getGMT() - timedelta(hours = 7)
    NYC = getGMT() - timedelta(hours = 4)
    LON = getGMT() + timedelta(hours = 1)

    return {'PDX': PDX, 'NYC': NYC, 'LON': LON}[location]

def isOpen(time):
    time = round(float(time.strftime('%H.%M')), 2)
    if (time >= 9 and time <= 17):
        return 'open'
    else:
        return 'closed'

def getBranchAvailability():
    print('The Portland branch is {}.'.format(isOpen(getTime('PDX'))))
    print('The New York City branch is {}.'.format(isOpen(getTime('NYC'))))
    print('The London branch is {}.'.format(isOpen(getTime('LON'))))
    

if __name__ == '__main__':
    getBranchAvailability()
