from Data import *
import matplotlib.pyplot as plt
import re

#sample of data class
class Sample:
    #attributs
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

    #return sample with only the willing name
    def get_by_name(self,name):
        #result list
        result = []
        #get all the datas with the name
        for data in self.datas:
            #if it's the good name we take the data
            if data.name == name:
                result.append(data)
        return Sample(result)

    #return sample with only the willing type
    def get_by_type(self,type):
        #result list
        result = []
        #get all the datas with the type
        for data in self.datas:
            #if it's the good type we take the data
            if data.type == type:
                result.append(data)
        return Sample(result)

    #return sample with only the willing topic
    def get_by_topic(self,topic):
        #result list
        result = []
        #get all the datas with the topic
        for data in self.datas:
            #if it's the good topic we take the data
            if data.topic == topic:
                result.append(data)
        return Sample(result)

    #return the average score
    def average_score(self):
        #short notes
        total = 0
        #sum
        for data in self.datas:
            total += data.score
        #average
        return total/len(self.datas)

    #return the average time
    def average_time(self):
        #short notes
        total_start = 0
        total_end = 0
        #sum
        for data in self.datas:
            total_start += data.start
            total_end += data.end
        #average
        return (total_end-total_start)/len(self.datas)

    #make a score average pie
    def score_average_pie(self):
        #name of each part
        name = ['right', 'wrong']
        #colors
        colors = ["#3bd70c","#fe2d2d"]
        #datas
        data = [self.average_score(),100-self.average_score()]
        #creation of the pie
        plt.pie(data, labels=name,colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)
        #make a perfect circle for the pie
        plt.axis('equal')
        #show up the pie
        plt.show()

    #make a time graph
    def time_plot(self):
        #list of time spend on each execise
        time_list = []
        for data in self.datas:
            time_list.append(data.end - data.start)
        #graph title
        plt.title("Time spend on each exercise")
        #show the grid
        plt.grid(True)
        #plot
        plt.plot(range(len(self.datas)), time_list, "b", linewidth=0.8, marker="+")
        #name of the x axe
        plt.xlabel("number of the exercise")
        #yaxe's name
        plt.ylabel("Time spend")
        #show the graph
        plt.show()

    #read a txt file and return a sample
    def read_data_sample(self,file_name):
        #opening the file
        with open(file_name,"r") as student_file:
            #list of data
            data_list = []
            #wrong data function
            wrong_data_function = Data()
            #regular expression
            expression = r"^([0-9]{1,3}[.]){3}[0-9]{1,3}(,[A-z]+){2},([A-z]+[ ]?)+,[0-9]{1,3}(,[0-9]{13}){2}$"
            #get all the line
            for line in student_file:
                #if data not empty
                if len(line)!=1:
                    try:
                        assert re.match(expression,line) is not None
                    #if line is not a correct data
                    except AssertionError:
                        #list of the two wrong datas
                        wrong_data_list = wrong_data_function.read_wrong_data(line)
                        #add each data in the data list
                        data_list.append(wrong_data_list[0])
                        data_list.append(wrong_data_list[1])
                    #if data is correct
                    else:
                        #data object
                        data_object = Data()
                        data_object.read_data(line)
                        data_list.append(data_object)
                #if data is empty skip it
                else:
                    continue
            #add the datas to the sample
            self.datas = data_list

#87.36.153.54,karl,match,chip chin chest,33,1370513116947,1370513137415