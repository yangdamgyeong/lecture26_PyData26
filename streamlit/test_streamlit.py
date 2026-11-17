import streamlit as st

st.title("Hello, Streamlit World~~")

name = "damgyeong"
st.title(f'Hello, {name}~~~ Welcome to Streamlit World!!!')

import pandas as pd
df = pd.DataFrame({
    'A' : [1, 2, 3, 4],
    'B' : [10, 20, 30, 40]
})

st.write(df)
st.header(name)
st.info(name)
st.error(name)
st.success(name)

import time
text = st.title("텍스트가 변할 겁니다.")
time.sleep(5)
text.info("변했네요.")