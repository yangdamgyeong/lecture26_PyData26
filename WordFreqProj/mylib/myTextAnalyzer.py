import pandas as pd
from collections import Counter
from konlpy.tag import Okt
from wordcloud import WordCloud

def load_corpus(datafile):
    data_df = pd.read_csv(datafile)
    return data_df

def get_freq_word(data_df, target_col):

    #분석 대상 컬럼을 리스트로 추출
    target_list = list(data_df[target_col])

    #리스트의 문서를 단어리스트로 생성 (품사태깅, 불용어제거)
    word_list = get_korean_word_list(target_list)

    #단어리스트로부터 Counter객체 생성
    counter = Counter(word_list)
    return counter

def get_korean_word_list(target_list):
    #품사 태깅
    tagger = Okt().pos
    my_tags = ['Noun' , 'Adjective', 'Verb']
    my_stopwords = ['영화', '것', '이', '더']

    result_list = [] #최종 단어 리스트

    for target in target_list:
        word_list = [ word for word, tag in tagger(target) if word not in my_stopwords and tag in my_tags ]
        result_list.extend(word_list)

    return result_list

#def generate_barh_graph(counter):


def generate_wordcloud(counter, num_words):
    font_path = 'C:/Windows/Fonts/malgun.ttf'

    wc = WordCloud(
        font_path=font_path,
        width=800,
        height=800,
        background_color="white",
        max_words=num_words
    )

    wc = wc.generate_from_frequencies(counter)
    return wc