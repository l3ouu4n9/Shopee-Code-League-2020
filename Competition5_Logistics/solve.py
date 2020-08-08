import csv
import datetime
import pandas as pd

mapp={'manila':0, 'luzon':1, 'visayas':2, 'mindanao':3}
need_date=[[3,5,7,7], [5,5,7,7], [7,7,7,7], [7,7,7,7]]

def read_csv():
    with open('delivery_orders_march.csv', newline='') as csvfile:
        data=[]
        rows = csv.reader(csvfile)
        for idx, row in enumerate(rows):
            data.append(row)
            #if idx>100:
            #    break
    return data[1:]

def check_cross_sunday(_1stdelivery,pickup_time):
    if (_1stdelivery-pickup_time).days >=7:
        return 1
    res = _1stdelivery.weekday() -  pickup_time.weekday()
    return res > 0

def analysis_data(datas):
    ID=[]
    time=[]
    diff_time=[]
    need=[]
    for data in datas:
        ID.append(data[0])
        pick_up_time=datetime.datetime.fromtimestamp(int(data[1]))
        first_time=datetime.datetime.fromtimestamp(int(float(data[2])))
        second_time=0 if data[3]=='' else datetime.datetime.fromtimestamp(int(float(data[3])))
        diff_time_1=(first_time-pick_up_time).days
        diff_time_2=0 if second_time==0 else (second_time-first_time).days
        time.append([pick_up_time, first_time, second_time])
        diff_time.append([diff_time_1, diff_time_2])
        src_address=data[4].split(' ')[-1]
        dst_address=data[5].split(' ')[-1]
        need.append(need_date[mapp[src_address.lower()]][mapp[dst_address.lower()]])
    return ID, time, diff_time, need

output_file = open('ans.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['orderid','is_late'])
datas=read_csv()
ID, time, diff_time, need=analysis_data(datas)
for i, t, d, n in zip(ID, time, diff_time, need):
    late=0
    if d[0]>n:
        if check_cross_sunday(t[1], t[0]):
            late+=1 if d[0]>n+1 else 0
    else:
        pass
    if d[1]>3:
        if check_cross_sunday(t[2], t[1]):
            late+=1 if d[0]>4 else 0
    else:
        pass
    late = 0 if late==0 else 1
    writer.writerow([i,late])
    #print(i, late)
output_file.close()