from numpy import *
import operator
import csv


if __name__=="__main__":

    with open('result.csv', 'wb') as myFile:
        myWriter = csv.writer(myFile)
        firstRow = ["ImageId", "Label"]
        myWriter.writerow(firstRow)

        for i in range (100):
            with open('result.csv', 'wb') as myFile:
                myWriter = csv.writer(myFile)

                mylist=[i,i+1]
                print(mylist)
                myWriter.writerow(mylist)
