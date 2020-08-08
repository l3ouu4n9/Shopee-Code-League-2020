import csv
import functools
from datetime import datetime, timedelta
import pandas as pd

def WriteCsv(shopId,userId):    
    submission =pd.DataFrame({'shopid':shopId,'userid':userId})
    submission.to_csv("22056Ma-Bao.csv",index = False)
    print("Write to csv finished!")

def custom_sorted(x, y):
    if x[1]>y[1]:
        return -1
    elif x[1]<y[1]:
        return 1
    else:
        if x[-1]<y[-1]:
            return -1
        elif x[-1]<y[-1]:
            return 1
        return 0

order_list=[]
with open('order_brush_order.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        order_list.append(row)

ordered_list=sorted(order_list[1:],key=functools.cmp_to_key(custom_sorted))
ordered_list.append([0,0,0,'2020-06-13 16:55:59'])

ans_dict=dict()
for idx in range(len(ordered_list)-1):
    #for idx in range(1000):
    tail_idx=idx+1
    head_shop_id=ordered_list[idx][1]
    head_time=datetime.strptime(ordered_list[idx][3],   '%Y-%m-%d %H:%M:%S')
    while head_shop_id==ordered_list[tail_idx][1]:
        tail_time=datetime.strptime(ordered_list[tail_idx][3], '%Y-%m-%d %H:%M:%S')
        if tail_time - head_time > timedelta(hours=1):
            tail_idx-=1
            break
        tail_idx+=1
        
    tail_time=datetime.strptime(ordered_list[tail_idx][3], '%Y-%m-%d %H:%M:%S')
    if head_shop_id==ordered_list[tail_idx][1] and tail_time - head_time <= timedelta(hours=1):
        user_id=set()
        for i in range(idx, tail_idx+1):
            user_id.add(ordered_list[i][2])
        if (tail_idx-idx+1)/len(user_id)>=3:
            
            if ans_dict.__contains__(head_shop_id):
                for item in user_id:
                    ans_dict[head_shop_id].add(item)
            else:
                ans_dict[head_shop_id]=set()
                for item in user_id:
                    ans_dict[head_shop_id].add(item)
            

    else:
        if ans_dict.__contains__(head_shop_id):
            continue
        else:
            ans_dict[head_shop_id]=set('0')
shopId,userId = [], []
for key, value in ans_dict.items():
    if len(value)>1 and '0' in value:
        value.remove('0')
    shopId.append(key)
    userId.append('&'.join(value))

WriteCsv(shopId,userId)