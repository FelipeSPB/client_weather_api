from datetime import datetime
from datetime import timedelta


def differenceDate(dateStart, dateEnd):
    dateParam2 = datetime.strptime(dateEnd,'%Y-%m-%d')        
    dateParam1 = datetime.strptime(dateStart,'%Y-%m-%d')
    days = abs((dateParam2 - dateParam1).days)
    return int(days)

def analisingDateEnd(dateInitial,dateEnd):
    dateParam2 = datetime.strptime(dateEnd,'%Y-%m-%d')        
    dateParam1 = datetime.strptime(dateInitial,'%Y-%m-%d')
        
    while  dateParam1  <= dateParam2:
        #checking_dateEnd = dataTable.query.filter_by(sampleDate = dateEnd)
        #if True:
            #return differenceDate(dateStart,dateEnd)
        dateParam2 = dateParam2 - timedelta(days=1)
        print(dateParam2)


def discoveringIndex(data, date):
    indexRaw = []
    for i in range(0,len(data):
        indexRaw.append(data[i]['sampleDate'])
    for j in data:
        if j == date:
            return date.index(i)

print(discoveringIndex(['14/12/1993','13/06/2019'], '14/12/1993'))



