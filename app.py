# -- coding: utf-8 --
import streamlit as st
from streamlit.components.v1 import html
from haversine import haversine

html1 =html("""
                <!DOCTYPE html>
                <html>
                <body>
                <a id="pos"  href="" )"></a>

                <script>
                let x = document.getElementById("pos");

                function getLocation() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition);
                } else { 
                    let pos = "http://localhost:8501/?pos=none"+'_'+"none";
                }
                return position.coords.latitude+"_"+position.coords.longitude
                }

                function showPosition(position) {
                let pos = "http://localhost:8501/?pos="+position.coords.latitude+"_"+position.coords.longitude
                window.location.replace(pos)
                }
                getLocation() 
                                       
                </script>

                </body>
                </html>
            """ ,height=600)

# html1.empty()
# 파라미터 가져오기
req_dict = st.experimental_get_query_params()

# 안쪽 html
if req_dict:
    pos = req_dict['pos'][0].split("_")
    curr_pos = (float(pos[0]), float(pos[1]))
    target_place = (37.541, 126.986)
    distance = haversine(target_place, curr_pos, unit = 'm')
    
    st.text(curr_pos)
    st.text(f"서울과의 거리 : {distance}m")
    html1.empty()
# 바깥쪽 html
else:
    st.info(" ")
    

# url = "http://localhost:8501/"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
# res = soup.select("//*[@id="pos"]")
# print(res)



# def current_location():
#     here_req = requests.get("http://www.geoplugin.net/json.gp")

#     if (here_req.status_code != 200):
#         print("현재좌표를 불러올 수 없음")
#     else:
#         location = json.loads(here_req.text)
#         crd = {"lat": str(location["geoplugin_latitude"]), "lng": str(location["geoplugin_longitude"])}

#     return crd

# crd = current_location()
# print(crd)
# <p id="pos" style="display: none" ></p>
    
    
    
# html1 =html("""
#                 <!DOCTYPE html>
#                 <html>
#                 <body>
#                 <p id="pos" ></p>

#                 <script>
#                 let x = document.getElementById("pos");

#                 function getLocation() {
#                 if (navigator.geolocation) {
#                     navigator.geolocation.getCurrentPosition(showPosition);
#                 } else { 
#                     x.innerHTML = "위치서비스가 제공되지 않는 브라우저입니다.";
#                 }
#                 }

#                 function showPosition(position) {
#                 x.innerHTML = "***"+position.coords.latitude+"_"+position.coords.longitude+"***"
#                 }
#                 getLocation()                
#                 </script>

#                 </body>
#                 </html>
#             """ )

# url = "http://localhost:8501/"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
# print(soup)