import streamlit as st

st.header('사용자 입력 폼')
with st.form('my_form'):
    name = st.text_input('이름')
    age = st.number_input('나이', value=10, step=1)
    agreed = st.checkbox('약관에 동의합니다.')
    submitted = st.form_submit_button('제출')

if submitted :
    st.info(f'이름 : {name}, 나이 : {age}')
    if agreed:
        st.info("약관에 동의함")

import time
@st.cache_data
def change_text():
    text = st.title("텍스트가 변할 겁니다.")
    time.sleep(5)
    text.info("변했네요.")

change_text()