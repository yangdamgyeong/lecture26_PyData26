import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import font_manager, rc
import mylib.myTextAnalyzer as ta

#decorate @
@st.dialog('데이터 확인하기', width='large')
def view_raw_data_dialog(data_df):
    num_data = st.number_input('확인할 데이터 수', value=10)
    st.write(data_df.head(num_data))

@st.cache_data
def visualize_graph(counter, num_words):

    #matplotlib 한글 폰트 설정
    font_path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    # 데이터 준비
    word_list = [word for word, _ in counter.most_common(num_words)] #x
    count_list = [count for _, count in counter.most_common(num_words)] #y

    #pyplot과 streamlit을 연동하기 위한 객체 생성
    fig, ax = plt.subplots()

    #pyplot 객체로 그래프 그리기
    ax.barh(word_list[::-1], count_list[::-1])

    #pyplot 결과물을 Streamlit 에서 실행
    st.pyplot(fig)

def visualize_wordcloud(counter, num_words):

    # wordcloud 객체 생성
    wc = ta.generate_wordcloud(counter, num_words)

    #pyplot과 streamlit을 연동하기 위한 객체 생성
    fig, ax = plt.subplots()

    #pyplot 객체로 wordcloud 그리기
    ax.imshow(wc)
    ax.axis('off')

    #pyplot 결과물을 streamlit에서 실행
    st.pyplot(fig)