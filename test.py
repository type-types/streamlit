import streamlit as st

st.title('퀴즈 서비스 🎯')

# 객관식 문제
st.header('객관식 문제')
st.write('다음 중 파이썬의 기본 데이터 타입이 아닌 것은?')
options = ['정수(int)', '문자열(str)', '배열(array)', '리스트(list)']
user_answer1 = st.radio('답을 선택하세요:', options)

# 주관식 문제
st.header('주관식 문제')
st.write('파이썬에서 "Hello, World!"를 출력하는 명령어는?')
user_answer2 = st.text_input('답을 입력하세요:')

# 제출 버튼
if st.button('제출하기'):
    # 객관식 정답 확인
    correct_answer1 = '배열(array)'
    if user_answer1 == correct_answer1:
        st.success('객관식 문제 정답입니다! 🎉')
    else:
        st.error(f'객관식 문제 오답입니다. 정답은 "{correct_answer1}" 입니다.')

    # 주관식 정답 확인
    correct_answer2 = 'print("Hello, World!")'
    if user_answer2.lower().strip() == correct_answer2.lower():
        st.success('주관식 문제 정답입니다! 🎉')
    else:
        st.error(f'주관식 문제 오답입니다. 정답은 "{correct_answer2}" 입니다.')

