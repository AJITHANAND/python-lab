start = (6*60+52)*60
easy = (8*60+15)*2
tempo = (7*60+12)*3

finished_time_sec = start+easy+tempo
finished_hr = finished_time_sec/(60*60.0)
finished_floor = finished_time_sec//(60*60)
finished_min = (finished_hr - finished_floor)*60
print("Finish time was : %d:%d"%(finished_hr,finished_min))