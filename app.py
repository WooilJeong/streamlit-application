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
st.header("Header Text")
st.subheader("Sub Text")


# 컬럼 분할
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    view = [100, 150, 30]
    st.write("리스트 뷰")
    st.write(view)

with col2:
    dview = {"a": 100, "b": 150, "c": 30}
    st.write("딕셔너리 뷰")
    st.write(dview)

with col3:
    sview = pd.Series(view)
    st.write("시리즈 뷰")
    st.write(sview)

# 컬럼 분할 후 메트릭 추가
cols = st.columns([1, 1, 2])
cols[0].metric("2/1", "1.3℃", "-0.1℃")
cols[0].metric("2/2", "1.3℃", "0.3℃")
cols[0].metric("2/3", "1.3℃", "0.4℃")
cols[1].metric("2/4", "1.3℃", "-0.5℃")
cols[1].metric("2/5", "1.3℃", "0.3℃")
cols[1].metric("2/6", "1.3℃", "-0.1℃")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
cols[2].line_chart(chart_data)
