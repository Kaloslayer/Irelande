from Data import *
import matplotlib.pyplot as plt
import re
import pymysql.cursors
import numpy as np


#Sample is a class which have many method to work on learning
#datas
class Sample:
    #attributs are just a list of the datas
    def __init__(self,data_list = []):
        self.datas = data_list

    #display
    def __repr__(self):
        #result string
        string = "["+str(self.datas[0])
        for i in range(len(self.datas)-1):
            string += ","+str(self.datas[i+1])
        string += "]"
        return string

    #take a string as parameter and return a Sample object which
    #have the string as student's name
    def sampleGetName(self, name):
        #result list
        result = []
        #get all the datas with the name
        for data in self.datas:
            #if it's the good name we take the data
            if data.name == name:
                result.append(data)
        return Sample(result)

    #take a string as parameter and return a Sample object which
    #have the string as type
    def sampleGetType(self, type):
        #result list
        result = []
        #get all the datas with the type
        for data in self.datas:
            #if it's the good type we take the data
            if data.type == type:
                result.append(data)
        return Sample(result)

    #take a string as parameter and return a Sample object which
    #have the string as topic
    def sampleGetTopic(self, topic):
        #result list
        result = []
        #get all the datas with the topic
        for data in self.datas:
            #if it's the good topic we take the data
            if data.topic == topic:
                result.append(data)
        return Sample(result)

    #return the average score of all the sample
    def sampleAverageScore(self):
        #short notes
        total = 0
        #sum
        for data in self.datas:
            total += data.score
        #average
        return total/len(self.datas)

    #return the average time spend on all the sample
    def sampleAverageTime(self):
        #short notes
        total_start = 0
        total_end = 0
        #sum
        for data in self.datas:
            total_start += data.start
            total_end += data.end
        #average
        return (total_end-total_start)/len(self.datas)

    #take as parameter a string for the name of the figure
    #an integer for the number of the figure( for multithreading)
    #an other string for the title in the figure
    #make a pie of the average score of the sample
    def samplePie(self,piename = 'pie.png',figurenumber = 1,title = 'Average Score'):
        #name of each part
        name = ['right', 'wrong']
        #colors
        colors = ["#3bd70c","#fe2d2d"]
        #datas
        data = [self.sampleAverageScore(), 100 - self.sampleAverageScore()]
        #create a figure
        plt.figure(figurenumber)
        if title != None:
            #title of the figure
            plt.title(title)
        #creation of the pie
        plt.pie(data, labels=name,colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)
        #make a perfect circle for the pie
        plt.axis('equal')
        #save the pie
        plt.savefig(piename)
        #clear the figure
        plt.clf()

    #take as parameter a string for the name of the figure
    #an integer for the number of the figure( for multithreading)
    #an other string for the title in the figure
    #make a plot of the time spend on each exercise
    def sampleTimePlot(self,plotname = 'plot.png',figurenumber = 1,title = 'Time Spend on Each Exercise'):
        #list of time spend on each execise
        time_list = []
        for data in self.datas:
            time_list.append(data.end - data.start)
        #create a figure
        plt.figure(figurenumber)
        if title != None:
            #graph title
            plt.title(title)
        #show the grid
        plt.grid(True)
        #plot
        plt.plot(range(len(self.datas)), time_list, "b", linewidth=0.8, marker="+")
        #name of the x axe
        plt.xlabel("number of the exercise")
        #yaxe's name
        plt.ylabel("Time spend")
        #save the plot
        plt.savefig(plotname)
        #clear the figure
        plt.clf()

    #take a path as parameter
    #it must be a txt file with a precise structure
    #fill the sample with the reading datas
    def sampleReadTxtSample(self, file_name):
        #opening the file
        with open(file_name,"r") as student_file:
            #count
            i = 0
            #list of data
            data_list = []
            #wrong data function
            wrong_data_function = Data()
            #regular expression
            expression = r"^([0-9]{1,3}[.]){3}[0-9]{1,3}(,[A-z]*[0-9]*){2},([A-z]+[ ]?)+,[0-9]{1,3}(,[0-9]{10,13}){2}$"
            #get all the line
            for line in student_file:
                #if data not empty
                if len(line)!=1:
                    try:
                        assert re.match(expression,line) is not None
                    #if line is not a correct data
                    except AssertionError:
                        if i == 0:
                            break
                        continue
                        i += 1
                    #if data is correct
                    else:
                        #data object
                        data_object = Data()
                        data_object.dataReadTxtData(line)
                        data_list.append(data_object)
                        i += 1
                #if data is empty skip it
                else:
                    i += 1
                    continue
            #add the datas to the sample
            self.datas = data_list

    #take a cursor as a parameter
    #the name of the table you want to work on
    #and a SQL WHERE and SELECT for more precise research on the database
    #fill the sample object with corresponding datas
    def sampleReadDBSample(self,cursor,from_table,where = None,select = None):

        #list of the datas
        data_list = []

        #if there is no select
        if select == None:

            #if there is no where
            if where == None:
                #read the records
                sql = "SELECT * FROM `{}`".format(from_table)
                cursor.execute(sql)
                result = cursor.fetchall()

            else:
                sql = "SELECT * FROM `{}` WHERE `{}`".format(from_table,where)
                cursor.execute(sql)
                result = cursor.fetchall()

        else:

            #if there is no where
            if where == None:
               #read the records
               sql = "SELECT `{}` FROM `{}`".format(select,from_table)
               cursor.execute(sql)
               result = cursor.fetchall()

            else:
                sql = "SELECT `{}` FROM `{}` WHERE `{}`".format(select,from_table,where)
                cursor.execute(sql)
                result = cursor.fetchall()

        #browse all the result
        for data in result:

            #data object
            data_object = Data(data)

            #append the data to the data list
            data_list.append(data_object)

        self.datas = data_list


    #take two string
    #first is the current name you want to change
    #second is the rename
    #the function will change all the corresponding datas
    #with the corresponding rename
    def sampleRename(self, student_name, rename):
        #browse all the datas of the sample
        for data in self.datas:
            #for each data change the name
            data.dataRename(student_name, rename)

    #take a path as parameter
    #create a new txt file or erase the precedent one
    #write a txt file with a precise structure
    def sampleWrite(self, filename):
        #open the file
        with open(filename,'w') as file:
            #browse all the datas
            for data in self.datas:
                #write a data
                data.dataWriteData(file)


    #take the path as parameter
    #add content to a txt file
    #or create it if not exist
    #write a txt file with a precise structure
    def sampleAddWrite(self, filename):
        #open the file
        with open(filename,'a') as file:
            #browse all the datas
            for data in self.datas:
                #write a data
                data.dataWriteData(file)

    #take the path as parameter
    #create a csv file or rewrite on it if exist
    #create the file if not exist
    #write a csv file
    def sampleCsvWrite(self, filename):
        #open the file
        with open(filename,'w') as file:
            #browse all the datas
            for data in self.datas:
                #write a data
                data.dataCsvWriteData(file)

    #take the path as parameter
    #add content to a csv file
    #create the file if not exist
    #write a csv file
    def sampleCsvAddWrite(self, filename):
        #open the file
        with open(filename,'a') as file:
            #browse all the datas
            for data in self.datas:
                #write a data
                data.dataCsvWriteData(file)

    #take a list as parameter
    #fill the list with all the different name of the sample
    def sampleNameList(self, name_list):
        #browse the datas
        for data in self.datas:
            #True is name already in the list
            name_in_list = False
            #browse name list
            for name in name_list:
                #if name exist
                if name == data.name:
                    name_in_list = True
            #if name not in list
            if name_in_list == False:
                #put the name in the list
                name_list.append(data.name)

    #take a list as parameter
    #fill the list with all the different topic of the sample
    def sampleTopicList(self, topic_list):
        #browse the datas
        for data in self.datas:
            #True is topic already in the list
            topic_in_list = False
            #browse topic list
            for topic in topic_list:
                #if topic exist
                if topic == data.topic:
                    topic_in_list = True
            #if topic not in list
            if topic_in_list == False:
                #put the topic in the list
                topic_list.append(data.topic)

    #take a list as parameter
    #fill the list with all the different type of the sample
    def sampleTypeList(self, type_list):
        #browse the datas
        for data in self.datas:
            #True is type already in the list
            type_in_list = False
            #browse type list
            for type in type_list:
                #if type exist
                if type == data.type:
                    type_in_list = True
            #if type not in list
            if type_in_list == False:
                #put the type in the list
                type_list.append(data.type)

    #return the min of all the timestamp of the sample
    def minTimestamp(self):

        #if the time in timestamp
        if isinstance(self.datas[0].start,int):
            #minimum is the first timestamp
            minimum = self.datas[0].start
        #if the time in datetime
        else:
            #time to timestamp
            #minimum is the first timestamp
            minimum = DatetimeToTimestamp(self.datas[0].start)
        for data in self.datas:
            #if the time in timestamp
            if isinstance(data.start,int):
                #if minimum > at the new timestamp then minimum is the new timestamp
                if minimum > data.start:
                    minimum = data.start
            #if the time in datetime
            else:
                #time to timestamp
                data.start = DatetimeToTimestamp(data.start)
                #if minimum > at the new timestamp then minimum is the new timestamp
                if minimum > data.start:
                    minimum = data.start
        #return the minmum timestamp
        return minimum

    #return the max of all the timestamp of the sample
    def maxTimestamp(self):
        #if the time in timestamp
        if isinstance(self.datas[0].end,int):
            #maximum is the fisrt data's timestamp
            maximum = self.datas[0].end
        #if the time in datetime
        else:
            maximum = DatetimeToTimestamp(self.datas[0].end)
        #for all the datas
        for data in self.datas:
            #if the time in timestamp
            if isinstance(data.end,int):
                #if maximum < at the new timestamp then maximum is the new timestamp
                if maximum < data.end:
                    maximum = data.end
            #if the time in datetime
            else:
                #time in timestamp
                data.end = DatetimeToTimestamp(data.end)
                #if maximum < at the new timestamp then maximum is the new timestamp
                if maximum < data.end:
                    maximum = data.end
        #return the maximum timestamp
        return maximum

    #return the number of week between the first data and the last one
    def numberOfWeek(self):
        #get the number of second between the first data and the last one
        number = self.maxTimestamp() - self.minTimestamp()
        #get the number of week
        number = number / 604800
        #if the number is not an integer and 1 to the number of week
        if number % 1 > 0:
            number = int(number)+1
        return number

    #take two strings as parameter and one integer
    #first string is the name of the file
    #second is the title of the figure
    #the integer is the number of the figure(for multithreading)
    #save a plot of the progression of the sample during the weeks
    def sampleProgressionPlot(self,plotname = 'progression.png', title = 'Progression by week', figurenumber = 1):

        #get the minimum of the timestamp
        start_week = self.minTimestamp()
        #get the number of weeks
        number_of_week = self.numberOfWeek()
        #list of the average score in each week
        average_list = []

        #for each week
        for week in range(number_of_week):

            #create a sample object
            sample = Sample()

            #for all the datas
            for data in self.datas:

                #if the time in timestamp
                if isinstance(data.start,int):

                    #take the datas of the week
                    #604 800 is the number of second in a week
                    if data.start >= start_week and data.start < start_week + 604800:
                        sample.datas.append(data)
                #if the time in datetime
                else:
                    #change the time in timestamp
                    data.start = DatetimeToTimestamp(data.start)

                    #take the datas of the week
                    if data.start >= start_week and data.start < start_week + 604800:
                        sample.datas.append(data)

            #start of the new week
            start_week = start_week + 604800
            #fill the list with the average score of the sample
            average_list.append(int(sample.sampleAverageScore()))


        #create a figure
        plt.figure(figurenumber)
        #graph title
        plt.title(title)
        #show the grid
        plt.grid(True)
        #plot
        plt.plot(range(len(average_list)), average_list, "b", linewidth=0.8, marker="+")
        #name of the x axe
        plt.xlabel("Week")
        #yaxe's name
        plt.ylabel("Score")
        #save the plot
        plt.savefig(plotname)
        #clear the figure
        plt.clf()