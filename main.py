import streamlit as st
import folium
from streamlit_folium import st_folium

# Streamlit 앱 제목
st.title("광주동신여자고등학교 위치 지도")

# 학교의 위도와 경도
latitude = 35.16849
longitude = 126.92478

# Folium 지도 생성
m = folium.Map(location=[latitude, longitude], zoom_start=16)

# 학교 위치에 마커 추가
folium.Marker(
    [latitude, longitude],
    popup="<b>광주동신여자고등학교</b><br>광주광역시 북구 동문대로 50",
    tooltip="광주동신여자고등학교"
).add_to(m)

# Folium 지도를 Streamlit에 표시
st_data = st_folium(m, width=700, height=500)

