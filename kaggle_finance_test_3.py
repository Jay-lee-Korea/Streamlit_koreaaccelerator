import pandas as pd
import streamlit as st

# 데이터 로드
data_file = 'yc_s+f2024_utf8_file.csv'  # CSV 파일 경로
data = pd.read_csv(data_file)

# Streamlit 앱 구성
st.title("Y Combinator 2024 Batch Companies")
st.write("이 대시보드는 Y Combinator 2024 프로그램에 참여한 기업들의 데이터를 제공합니다.")

# 데이터 테이블 표시
st.subheader("Company List")
st.dataframe(data)

# 특정 섹터 필터링
sector = st.selectbox("Filter by Sector", options=data['Sector'].unique())
filtered_data = data[data['Sector'] == sector]
st.write(f"**{sector}** 섹터에 속한 회사들:")
st.dataframe(filtered_data)
