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
st.header("차트")
st.subheader("Sub Text")

# 컨텐츠
chart_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
