import pandas as pd

dataRaw = pd.read_csv('State_of_Utah_Crash_Data_2015-2019_20241013.csv')
columnsToKeep = ['CRASH_DATE']
data = dataRaw[columnsToKeep]

data['CRASH_DATE'] = pd.to_datetime(data['CRASH_DATE']).dt.date
data['count'] = data.groupby(['CRASH_DATE'])['CRASH_DATE'].transform('size')

monthDays = {
    '01': 0,
    '02': 31,
    '03': 59,
    '04': 90,
    '05': 120,
    '06': 151,
    '07': 181,
    '08': 212,
    '09': 243,
    '10': 273,
    '11': 304,
    '12': 334
}


def convertDateToNumber(year, month, day):
    yearsToDays = (year - 2015) * 365
    monthToDays = monthDays[month]
    return yearsToDays + monthToDays + day


for index, row in data.iterrows():
    currentDate = str(row['CRASH_DATE']).split("-")
    year = int(currentDate[0])
    month = currentDate[1]
    day = int(currentDate[2])

    dateInDays = convertDateToNumber(year, month, day)
    data.at[index, 'CRASH_DATE'] = dateInDays


data.sort_values(by='CRASH_DATE', ascending=True, inplace=True)
data.drop_duplicates(inplace=True)
data.to_csv("dateCount.csv", index=False)