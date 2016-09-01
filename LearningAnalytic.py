import os
import time as tm
from Sample import *

start = tm.time()

#Here are some examples of what we can do with the tool

# Connect to the database
connection = pymysql.connect(host='student.computing.dcu.ie',
                             user='mwardintern',
                             password='mward2016',
                             db='la_dev',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    #make the connection
    with connection.cursor() as cursor:

        #sample object
        data_sample = Sample()
        # Read all the records
        data_sample.sampleReadDBSample(cursor,'Exercise')

finally:
    #close the connection
    connection.close()
#create and save a pie of the average score of the class
data_sample.samplePie(piename="AverageClassScore.png",title="Average Score of the Class")

#create and save a plot of the progression of the score
data_sample.sampleProgressionPlot(title="progression of the class")

#get the sample with student's name 0
#sample object
data_sample_name = Sample()
#fill the object with only the data of the student's name
data_sample_name = data_sample.sampleGetName(0)
#create a new text file and write a sample in
data_sample_name.sampleWrite("SampleName.txt")
#create a new csv file and write a sample in
data_sample_name.sampleCsvWrite("SampleName.csv")
#it works the same way for all the other function of this type
#sampleGetType
#sampleGetTopic

#create and save a plot of the time spend on each exercise by the student 0
data_sample_name.sampleTimePlot(plotname='timePlot.png',title="Time spend on each exercise by the student 0")

#rename one student name in the sample
data_sample.sampleRename(0,"Ramses")
#get the datas with Ramses as student's name
data_sample_Ramses = data_sample.sampleGetName("Ramses")
#create a new text file and write a sample in
data_sample_Ramses.sampleWrite("SampleRamses.txt")
#create a new csv file and write a sample in
data_sample_Ramses.sampleCsvWrite("SampleRamses.csv")
#data_sample_Ramses and data_sample_name are the same sample but the student'name changed

#list object
name_list = []
#get the list of all the different student's name
data_sample.sampleNameList(name_list)
print("data_sample's name_list: ",name_list)
#list object
other_name_list = []
#get the list of the other sample object
data_sample_name.sampleNameList(other_name_list)
print("data_sample_name's name list :",other_name_list)
#sampleTopicList and sampleTypeList are working the same way

#sample object
data_sample_read = Sample()
#read the new txt file
data_sample_read.sampleReadTxtSample("Sample.txt")
print("data_sample_read: ",data_sample_read)


#All the other comment are some sample of what I've done.
#Most of it works but not everything

"""
#-------Sample Treatement-------
directory_path = r"C:\Python\Ireland\LearningData"

#list of the different name
name_list = []

#if the text file exist
if os.path.exists(r"C:\Python\Ireland\LearningData\Data.txt") == True:
    #remove the text file
    os.remove(r"C:\Python\Ireland\LearningData\Data.txt")

#if the csv file exist
if os.path.exists(r"C:\Python\Ireland\LearningData\Data.csv") == True:
    #remove the csv file
    os.remove(r"C:\Python\Ireland\LearningData\Data.csv")

#create a learning repertory if not exist
if os.path.isdir(r"C:\Python\Ireland\LearningData") == False:
    os.mkdir(r"C:\Python\Ireland\LearningData")

#change working directory
os.chdir(directory_path)

#create a Topic repertory if not exist
if os.path.isdir(r"C:\Python\Ireland\LearningData\Topic") == False:
    os.mkdir(r"C:\Python\Ireland\LearningData\Topic")

#create a Type repertory if not exist
if os.path.isdir(r"C:\Python\Ireland\LearningData\Type") == False:
    os.mkdir(r"C:\Python\Ireland\LearningData\Type")

#browse all the datas
for data in data_sample.datas:

    #create a student repertory if not exist
    if os.path.isdir(str(data.name)) == False:
        #create the student repertory
        os.mkdir(str(data.name))

    #create a topic repertory if not exist
    if os.path.isdir("{0}\Topic".format(str(data.name))) == False:
        #create the topic repertory
        os.mkdir("{0}\Topic".format(str(data.name)))

    #create a type repertory if not exist
    if os.path.isdir("{0}\Type".format(str(data.name))) == False:
        #create the type repertory
        os.mkdir("{0}\Type".format(str(data.name)))

    #create a topic repertory
    if os.path.isdir("{0}\Topic\{1}".format(str(data.name),data.topic)) == False:
        #create the topic repertory
        os.mkdir("{0}\Topic\{1}".format(str(data.name),data.topic))

    #create a type repertory
    if os.path.isdir("{0}\Type\{1}".format(str(data.name),data.type)) == False:
        #create the type repertory
        os.mkdir("{0}\Type\{1}".format(str(data.name),data.type))

    #create a topic repertory if not exist
    if os.path.isdir("Topic\{0}".format(data.topic)) == False:
        #create the topic repertory
        os.mkdir("Topic\{0}".format(data.topic))

    #create a type repertory if not exist
    if os.path.isdir("Type\{0}".format(data.type)) == False:
       #create the type repertory
       os.mkdir("Type\{0}".format(data.type))

#get the list of the different student's name
data_sample.sampleNameList(name_list)

#browse all the different names
for name in name_list:

    #new sample with only one name
    data_sample_name = data_sample.sampleGetName(name)

    #if there are datas write them in a file
    if len(data_sample_name.datas) != 0:
        #write the new sample
        data_sample_name.sampleAddWrite("{0}\Data.txt".format(name))

    #if there are datas write them in a file
    if len(data_sample_name.datas) != 0:
        #write the new sample
        data_sample_name.sampleAddWrite("Test.txt")

    #if there are datas write them in a file
    if len(data_sample_name.datas) != 0:
        #write the new sample
        data_sample_name.sampleCsvAddWrite("Data.csv")

"""
"""

#------------------Sample treatment--------------


directory_path = 'C:\Python\Ireland\data\data'

#list of the different name
name_list = []

#if the text file exist
if os.path.exists(r"C:\Python\Ireland\LearningData\Data.txt") == True:
    #remove the text file
    os.remove(r"C:\Python\Ireland\LearningData\Data.txt")

#if the csv file exist
if os.path.exists(r"C:\Python\Ireland\LearningData\Data.csv") == True:
    #remove the csv file
    os.remove(r"C:\Python\Ireland\LearningData\Data.csv")

#create a learning repertory if not exist
if os.path.isdir(r"C:\Python\Ireland\LearningData") == False:
    os.mkdir(r"C:\Python\Ireland\LearningData")

#create a Topic repertory if not exist
if os.path.isdir(r"C:\Python\Ireland\LearningData\Topic") == False:
    os.mkdir(r"C:\Python\Ireland\LearningData\Topic")

#create a Type repertory if not exist
if os.path.isdir(r"C:\Python\Ireland\LearningData\Type") == False:
    os.mkdir(r"C:\Python\Ireland\LearningData\Type")

#browse all the elements of the directory
for path, dirs, files in os.walk(directory_path):
    #browse all the files
    for filename in files:
        #if file is not a text file skip it
        if filename.find("txt") != -1:

            #change the working directory
            os.chdir(path)

            #object Sample
            data_sample = Sample()
            #read each file
            data_sample.sampleReadSample(filename)

            #change the working directory
            os.chdir(r"C:\Python\Ireland\LearningData")

            #browse all the datas
            for data in data_sample.datas:

                #create a student repertory if not exist
                if os.path.isdir(data.name) == False:
                    #create the student repertory
                    os.mkdir(data.name)

                #create a topic repertory if not exist
                if os.path.isdir("{0}\Topic".format(data.name)) == False:
                    #create the topic repertory
                    os.mkdir("{0}\Topic".format(data.name))

                #create a type repertory if not exist
                if os.path.isdir("{0}\Type".format(data.name)) == False:
                    #create the type repertory
                    os.mkdir("{0}\Type".format(data.name))

                #create a topic repertory
                if os.path.isdir("{0}\Topic\{1}".format(data.name,data.topic)) == False:
                    #create the topic repertory
                    os.mkdir("{0}\Topic\{1}".format(data.name,data.topic))

                #create a type repertory
                if os.path.isdir("{0}\Type\{1}".format(data.name,data.type)) == False:
                    #create the type repertory
                    os.mkdir("{0}\Type\{1}".format(data.name,data.type))

                #create a topic repertory if not exist
                if os.path.isdir("Topic\{0}".format(data.topic)) == False:
                    #create the topic repertory
                    os.mkdir("Topic\{0}".format(data.topic))

                #create a type repertory if not exist
                if os.path.isdir("Type\{0}".format(data.type)) == False:
                    #create the type repertory
                    os.mkdir("Type\{0}".format(data.type))

            #get the list of the different student's name
            data_sample.sampleNameList(name_list)

            #browse all the different names
            for name in name_list:

                #new sample with only one name
                data_sample_name = data_sample.sampleGetName(name)

                #if there are datas write them in a file
                if len(data_sample_name.datas) != 0:
                    #write the new sample
                    data_sample_name.sampleAddWrite("{0}\Data.txt".format(name))

            #if there are datas write them in a file
            if len(data_sample.datas) != 0:
                #write the new sample
                data_sample.sampleAddWrite("Data.txt")

            #if there are datas write them in a file
            if len(data_sample.datas) != 0:
                #write the new sample
                data_sample.sampleCsvAddWrite("Data.csv")
"""


"""
path = "C:\Python\Ireland\LearningData"

class_graph_thread = ClassGraphs(path)

student_graph_thread = StudentGraphs(name_list,path)

class_graph_thread.start()
student_graph_thread.start()

class_graph_thread.join()
student_graph_thread.join()

"""
"""
#sample object
data_sample_class = Sample()

#read a sample
data_sample_class.sampleReadSample("Data.txt")

#get the average score of the class
data_sample_class.samplePie("AverageClassScore.png")

#list of different topic
topic_list_class = []
#get the list of the different topic
data_sample_class.sampleTopicList(topic_list_class)

#list of different type
type_list_class = []
#get the list of the different type
data_sample_class.sampleTypeList(type_list_class)

#browse all the topic
for topic in topic_list_class:

    #get all the data of one topic
    data_sample_topic_class = data_sample_class.sampleGetTopic(topic)

    #pie of the class's topic score
    data_sample_topic_class.samplePie("Topic\{0}\Average{1}Score.png".format(topic,topic))
    #graph of the class's topic time
    data_sample_topic_class.sampleTimePlot("Topic\{0}\AverageTimeSpend.png".format(topic))

#browse all the type
for type in type_list_class:

    #get all the data of one type
    data_sample_type_class = data_sample_class.sampleGetType(type)

    #pie of the class's type score
    data_sample_type_class.samplePie("Type\{0}\Average{1}Score.png".format(type,type))
    #graph of the class's type time
    data_sample_type_class.sampleTimePlot("Type\{0}\AverageTimeSpend.png".format(type))


#brose all the different name
for name in name_list:

    #sample object
    data_sample = Sample()
    #read a sample
    data_sample.sampleReadSample("{0}\Data.txt".format(name))

    #list of the different topic
    topic_list = []
    #list of the different type
    type_list = []

    #get the list of the different topic
    data_sample.sampleTopicList(topic_list)
    #get the list of the different type
    data_sample.sampleTypeList(type_list)

    #pie of the student's score
    data_sample.samplePie('{0}\AverageScore.png'.format(name))
    #plot of the average time spend
    data_sample.sampleTimePlot('{0}\AverageTimeSpend.png'.format(name))

    for topic in topic_list:
        #new sample with only one topic
        data_sample_topic = data_sample.sampleGetTopic(topic)
        #pie of the student's topic score
        data_sample_topic.samplePie('{0}\Topic\{1}\Average{2}Score.png'.format(name,topic,topic))
        #graph of the student's type topic
        data_sample_topic.sampleTimePlot("{0}\Topic\{1}\AverageTimeSpend.png".format(name,topic))


    for type in type_list:
        #new sample with only one type
        data_sample_type = data_sample.sampleGetType(type)
        #pie of the student's type score
        data_sample_type.samplePie('{0}\Type\{1}\Average{2}Score.png'.format(name,type,type))
        #graph of the student's type time
        data_sample_type.sampleTimePlot("{0}\Type\{1}\AverageTimeSpend.png".format(name,type))



"""
"""
for data in data_list:
#sample with Daire as name
sample_name = data_sample.sampleGetName("Ramses")
#sample with pattern as topic
sample_topic = data_sample.sampleGetTopic("ordinal")
#sample with mix as type
sample_type = data_sample.sampleGetType("match")
#average score of Daire
print("Average score:{}".format(sample_name.sampleAverageScore()))
#average time of pattern topic
print("Avereage time:{}".format(sample_topic.sampleAverageTime()))
#average score pie
data_sample.samplePie()
#time spend graph
data_sample.sampleTimePlot()
"""


"""
#------------------------Rename Part---------------
#directory_path = r'C:\Python\Ireland\data\data'

#list of the name
name_list = []

#browse all the elements of the directory
for path, dirs, files in os.walk(directory_path):
    #browse all the files
    for filename in files:
        print(filename)
 #       if filename.find("txt") != -1:
  #          print('passe dans le if')
            os.chdir(path)
            #object Sample
            data_sample = Sample()
            #read each file
            data_sample.sampleReadSample(filename)
            #list of the name
            data_sample.sampleNameList(name_list)
            for name in name_list:
                #rename
                data_sample.sampleRename(name,name_list.index(name))
            if len(data_sample.datas) != 0:
                #write the new sample
                data_sample.sampleWrite(filename)
"""


"""
#-------------------Learning Part---------
#directory_path = r'C:\Python\Ireland\data\data'

#list of the name
name_list = []

#browse all the elements of the directory
for path, dirs, files in os.walk(directory_path):
    #browse all the files
    for filename in files:
 #       if filename.find("txt") != -1:
            os.chdir(path)
            #object Sample
            data_sample = Sample()
            #read each file
            data_sample.sampleReadSample(filename)
            #list of the name
            data_sample.sampleNameList(name_list)
            for name in name_list:
                #rename
                data_sample.sampleRename(name,name_list.index(name))
            if len(data_sample.datas) != 0:
                #write the new sample
                data_sample.sampleWrite(filename)
"""

end = tm.time()

print("execution time : ",end-start,"s")