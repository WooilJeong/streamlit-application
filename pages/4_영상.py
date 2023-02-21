import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium

# 페이지 기본 설정
st.set_page_config(
    page_icon="✨",
    page_title="Streamlit Application Page",
    layout="wide",
)

# 페이지 헤더, 서브 헤더 설정
st.header("영상")
st.subheader("Sub Text")

# 컨텐츠
video_url_list = [
    'https://www.youtube.com/watch?v=XACHCUduqh0',
    'https://www.youtube.com/watch?v=o25-om93D0E',
]

# 2열 생성
col1, col2 = st.columns([1, 1])
# 1행 1열, 1행 2열, 2행 1열, 2행 2열 순으로 영상 출력 (반복문 이용, n개의 영상 출력)
for i in range(0, len(video_url_list), 2):
    with col1:
        try:
            st.video(video_url_list[i])
        except:
            pass
    with col2:
        try:
            st.video(video_url_list[i+1])
        except:
            pass
