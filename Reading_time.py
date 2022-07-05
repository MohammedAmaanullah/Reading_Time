from google.colab import files
a=files.upload()
import plotly.figure_factory as ff
import statistics 
import random
import csv
import pandas as pd
import plotly.graph_objects as go


def random_set_of_mean(counter):
  dataset = []
  for i in range(0, counter):
    random_index= random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)
  mean = statistics.mean(dataset)
  return mean
  mean_list=[]
for i in range(0,1000):
  set_of_mean = random_set_of_mean(100)
  mean_list.append(set_of_mean)
std_deviation = statistics.stdev(mean_list)
mean=statistics.mean(mean_list)
print(std_deviation, mean)  
df = pd.read_csv("sample_2.csv")
data = df["Reading_time"].tolist()
f_std_s, f_std_e = mean-std_deviation, mean+std_deviation
s_std_s, s_std_e = mean-(2*std_deviation), mean+(2*std_deviation)
t_std_s, t_std_e = mean-(3*std_deviation), mean+(3*std_deviation)
mean_of_sample1 = statistics.mean(data)
print(mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="Mean of student reading time"))
fig.add_trace(go.Scatter(x=[f_std_s, f_std_e], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[s_std_s, s_std_e], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[t_std_s, t_std_e], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
print(f_std_s, f_std_e)
print(s_std_s, s_std_e)
print(t_std_s, t_std_e)
z_score = (mean_of_sample1-mean)/std_deviation
print(z_score)