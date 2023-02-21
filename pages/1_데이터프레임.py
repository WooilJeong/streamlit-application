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
st.header("데이터프레임")
st.subheader("Sub Text")

# 컨텐츠
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.dataframe(df)
