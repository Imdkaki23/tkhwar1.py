names=['morocco','japan','brazil','italy','australia']
cities=['rabat','tokyo','brazil','roma','sidney']
pop=[40,90,200,70,30]
my_dict={'country':names, 'capitals':cities,'population':pop}
print(my_dict)
import pandas as pd
dict=pd.DataFrame(my_dict)
print(dict)
raw_labels=['MA','JPN','BR','IT','AUS']
dict.index=raw_labels
print(dict)
print(dict['country'])
print(dict[0:3])
print(dict.loc[['JPN']])