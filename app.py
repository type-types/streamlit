import streamlit as st
import time

st.title('상태 표시 및 알림 요소 📊')

# 메시지 표시
st.header('알림 메시지')
st.success('성공 메시지!')
st.info('정보 메시지.')
st.warning('경고 메시지!')
st.error('오류 메시지!')

# 예외 표시
st.header('예외 표시')
try:
    1/0
except Exception as e:
    st.exception(e)

# 진행 상황 표시
st.header('진행 상황 표시')

# 프로그레스 바
st.subheader('프로그레스 바')
progress_bar = st.progress(0)
for i in range(101):
    progress_bar.progress(i)
    time.sleep(0.01)

# 상태 메시지
st.subheader('상태 메시지')
with st.status("데이터 처리 중...", expanded=True) as status:
    st.write("데이터 다운로드 중...")
    time.sleep(1)
    st.write("데이터 변환 중...")
    time.sleep(1)
    st.write("분석 완료!")
    status.update(label="작업 완료!", state="complete")

# 스피너
st.subheader('스피너')
with st.spinner('처리 중...'):
    time.sleep(2)
    st.success('완료!')

# 풍선 효과
if st.button('축하해주세요!'):
    st.balloons()  # 또는 st.snow()