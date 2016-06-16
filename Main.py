import pickle
from Data import *
from Sample import *


data_sample = Sample()
data_sample.read_data_sample("karl.txt")
#sample with Daire as name
sample_name = data_sample.get_by_name("karl")
#sample with pattern as topic
sample_topic = data_sample.get_by_topic("pattern")
#sample with mix as type
sample_type = data_sample.get_by_type("mix")
#average score of Daire
print("Average score:{}".format(sample_name.average_score()))
#average time of pattern topic
print("Avereage time:{}".format(sample_topic.average_time()))
#average score pie
data_sample.score_average_pie()
#time spend graph
data_sample.time_plot()
