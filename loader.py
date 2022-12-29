import pandas as pd
from haversine import haversine

def loadParkingList(lat,long):
    data = pd.read_csv(".\\data\\parking_data_20191224.csv", encoding='cp949')
    print(data.columns)
    data = data[['주차장명','위도','경도','주차구획수','주차장구분','주차장유형','주차장도로명주소','요금정보','연락처']]
    data = data.astype({'위도':'object'})
    data = data.astype({'경도':'object'})
    
    target_place = (lat, long)
    data['거리'] = data.apply(lambda x: (x[1],x[2]), axis=1) 
    data['거리'] = data['거리'].apply(lambda x: haversine(target_place,x,unit="m"))
    
    data = data.sort_values(by="거리", ascending=True)[:10]
    data['거리'] = data['거리'].apply(lambda x: str(round(x,1))+"m")
    
    return data
    
    # distance = haversine(target_place, curr_pos, unit = 'm')

