import pandas as pd
import matplotlib.pyplot as plt
import sys


def readInputDate():
    year = int(input("Enter a year after 2015: "))
    if year < 2015:
        print("Try Again")
        sys.exit(1)
    day = int(input("Enter a day between 1-365: "))
    if day < 1 or day > 365:
        print("Try Again")
        sys.exit(1)
    return (year - 2015) * 365 + day


def calculateCovariance():
    summation = 0
    for index, row in data.iterrows():
        currX = row['CRASH_DATE']
        currY = row['count']
        summation += (currX-independentMean) * (currY-dependentMean)
    return summation/(numRows-1)


def calculateVarianceOfIndependentVar():
    summation = 0
    for index, row in data.iterrows():
        currX = row['CRASH_DATE']
        summation += (currX-independentMean) * (currX-independentMean)
    return summation/(numRows-1)


def plotValues(m, b):
    x = data['CRASH_DATE']
    y = data['count']
    plt.figure(figsize=(20, 10))
    plt.scatter(x, y)
    yVals = [(m*j + b) for j in x]
    rootMse = meanSquaredError(yVals) ** .5
    print(f"Root Mean Squared Error: {rootMse}")
    plt.plot(x, yVals, linewidth=3, color='red')
    plt.xlabel("CRASH DATE")
    plt.ylabel("CRASH COUNT")
    plt.title("Linear Regression on Car Crash Dataset")
    plt.show()


def meanSquaredError(predictedYVals):
    summation = 0
    for i in range(len(predictedYVals)):
        error = data['count'][i] - predictedYVals[i]
        summation += (error * error)
    return summation/numRows


data = pd.read_csv('dateCount.csv')

independentMean = data['CRASH_DATE'].mean()
dependentMean = data['count'].mean()
numRows = len(data)
# print(f"I: {independentMean}\nD: {dependentMean}\nN: {numRows}")
covariance = calculateCovariance()
varianceOfIndependent = calculateVarianceOfIndependentVar()
# print(covariance)
# print(varianceOfIndependent)
m = covariance/varianceOfIndependent
b = dependentMean - (m * independentMean)
print(f"LINE OF BEST FIT IS: y = {m}x + {b}")
inputDate = readInputDate()
print(f"Predicted Number of Car Accidents on day {inputDate} is {round(m * inputDate + b)}")


plotValues(m=m, b=b)



