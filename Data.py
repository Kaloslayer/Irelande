#regular expression
import re

#data class
class Data:
    #attributs
    def __init__(self,data = ["","","","",0,0,0]):
        self.ip = str(data[0])
        self.name = str(data[1])
        self.type = str(data[2])
        self.topic = str(data[3])
        self.score = int(data[4])
        self.start = int(data[5])
        self.end = int(data[6])

    #change the display of the class
    def __repr__(self):
        string = ""
        string += "Ip:"+self.ip+"\n"+"Name:"+self.name+"\n"+"Type:"+self.type+"\n"+\
                  "Topic:"+self.topic+"\n"+"Score:"+str(self.score)+"\n"+\
                  "Start:"+str(self.start)+"\n"+"End:"+str(self.end)+"\n"
        return string

    #change the display when turned into string
    def __str__(self):
        string = ""
        string += "Ip:"+self.ip+"\n"+"Name:"+self.name+"\n"+"Type:"+self.type+"\n"+\
                  "Topic:"+self.topic+"\n"+"Score:"+str(self.score)+"\n"+\
                  "Start:"+str(self.start)+"\n"+"End:"+str(self.end)+"\n"
        return string

    #read a data
    def read_data(self,line):
        #get the data into list
        data = line.split(",")
        self.ip = str(data[0])
        self.name = str(data[1])
        self.type = str(data[2])
        self.topic = str(data[3])
        self.score = int(data[4])
        self.start = int(data[5])
        self.end = int(data[6])

    #read a wrong_data and return a list with two datas
    def read_wrong_data(self,line):
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



#87.36.153.54,karl,match,chip chin chest,33,1370513116947,1370513137415