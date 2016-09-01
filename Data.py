#regular expression
import re
import datetime
from time import gmtime, strftime
from datetime import *

#function to turn a timestamp into a date(timestamp must be in second)
#take a timestamp as parameter and string of the datetime pattern you want
#datePattern exemple("%Y-%m-%d %H:%M:%S")
def timestampToDate(timestamp, datePattern):

    #return a datetime object
    return strftime(datePattern, gmtime(float(timestamp)))

#function to turn a datetime into a timestamp
#take a datetime as parameter("%Y-%m-%d %H:%M:%S")
def DatetimeToTimestamp(dt):

    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    timestamp = int(timestamp)
    #return a timestamp
    return timestamp

#class that represent one exercise done by a student
class Data:
    #attributs
    def __init__(self,data_dict = {'StudentId':0,'Topic':"",'Start_Time':0,'End_Time':0,'Type':'','Score':0}):
        self.ip = None
        #name of the student
        self.name = data_dict['StudentId']
        #type of the exercise
        self.type = data_dict['Type']
        #topic of the exercise
        self.topic = data_dict['Topic']
        #score of the student on this exercise
        self.score = data_dict['Score']

        #if time is a timestamp
        if isinstance(data_dict['Start_Time'],int):
            #if timestamp is not in second
            if data_dict['Start_Time'] > 9999999999:
                #get the timestamp in second
                data_dict['Start_Time'] = data_dict['Start_Time']/1000
                #time where the student strated the exercise
                self.start = data_dict['Start_Time']
        #if time is a datetime
        else:
            #time where the student strated the exercise
            self.start = data_dict['Start_Time']

        #if time is a timestamp
        if isinstance(data_dict['End_Time'],int):
            #if timestamp is not in second
            if data_dict['End_Time'] > 9999999999:
                #get the timestamp in second
                data_dict['End_Time'] = data_dict['End_Time']/1000
                #time where the student strated the exercise
                self.end = data_dict['End_Time']
        #if time is a datetime
        else:
            #time where the student finished the exercise
            self.end = data_dict['End_Time']




    #change the display of the class
    def __repr__(self):
        list = []
        string = ""
        if self.ip != None:
            list += [str(self.ip),str(self.name),str(self.type),str(self.topic),str(self.score),str(self.start),str(self.end)]
            string = ",".join(list)
        else:
            list += [str(self.name),str(self.type),str(self.topic),str(self.score),str(self.start),str(self.end)]
            string = ",".join(list)
        return string

    #change the display when turned into string
    def __str__(self):
        list = []
        string = ""
        if self.ip != None:
            list += [str(self.ip),str(self.name),str(self.type),str(self.topic),str(self.score),str(self.start),str(self.end)]
            string = ",".join(list)
        else:
            list += [str(self.name),str(self.type),str(self.topic),str(self.score),str(self.start),str(self.end)]
            string = ",".join(list)
        return string

    #take the studnet's name you want to replace
    #and the new name and change the student's name
    def dataRename(self, student_name, rename):
        #if it's the student name
        if self.name == student_name:
            #rename
            self.name = str(rename)

    #take a file as paramter (the file must be open)
    #write one data in a txt file
    def dataWriteData(self, file):
        #string to write
        string = ''
        if isinstance(self.start,datetime):
            self.start = DatetimeToTimestamp(self.start)
            self.start = int(self.start)

        if isinstance(self.start,datetime):
            self.end = DatetimeToTimestamp(self.end)
            self.end = int(self.end)

        if self.ip != None:
            #write a data in txt
            string += str(self.ip) + ',' + str(self.name) + ',' + str(self.type) + ',' + str(self.topic) + ','
            string += str(self.score) + ',' + str(self.start) + ',' + str(self.end) + '\n'
            file.write(string)
        else:
            #write a data in txt
            string += '0.0.0.0'+ ',' + str(self.name) + ',' + str(self.type) + ',' + str(self.topic) + ','
            string += str(self.score) + ',' + str(self.start) + ',' + str(self.end) + '\n'
            file.write(string)

    #take a file as paramter (the file must be open)
    #write one data in a csv file
    def dataCsvWriteData(self, file):

        if isinstance(self.start,int):
            self.start = int(self.start)
            self.start = timestampToDate(self.start,"%Y-%m-%d %H:%M:%S")

        if isinstance(self.end,int):
            self.end = int(self.end)
            self.end = timestampToDate(self.end,"%Y-%m-%d %H:%M:%S")
        #string to write
        string = ''
        #write a data in txt
        string += 'NULL' + ';' + str(self.name) + ';' + str(self.type) + ';' + str(self.topic) + ';'
        string += str(self.score) + ';' + str(self.start) + ';' + str(self.end) + '\n'
        file.write(string)

    #take a line as parameter
    #read a txt line and fill the data object
    def dataReadTxtData(self, line):
        #get the data into list
        data = line.split(",")
        self.ip = str(data[0])
        self.name = str(data[1])
        self.type = str(data[2])
        self.topic = str(data[3])
        self.score = int(data[4])

        if int(data[5]) > 9999999999:
            data[5] = int(data[5]) / 1000

        if int(data[6]) > 9999999999:
            data[6] = int(data[6]) / 1000

        self.start = int(data[5])
        self.end = int(data[6])

    #take a line in parameter
    #if the line is wrong this function should repair some bug or skip them
    #read the txt file and fill the data object
    def dataReadWrongData(self, line):
        data_list = []
        #wrong data = line in list
        wrong_data = line.split(",")
        #correct data
        data1 = []
        data2 = []
        #course wrong_data list
        for each_wrong_data in wrong_data:
            #if each_wrong_data empty do nothing
            if each_wrong_data != "":
                #get the first part of the data
                part1 = each_wrong_data[0:len(each_wrong_data)//2]
                #get the second part of the data
                part2 = each_wrong_data[len(each_wrong_data)//2:len(each_wrong_data)]
                #insert each part in the correct data
                data1.append(part1)
                data2.append(part2)
            else:
                continue
        #turn datas into Data objects
        data1_object = Data(data1)
        data2_object = Data(data2)
        #add the datas to the data list
        data_list.append(data1_object)
        data_list.append(data2_object)
        return data_list