import streamlit as st
import numpy as np
import pandas as pd
from ipynb.fs.full.Indexation import definition
from ipynb.fs.full.Indexation import recherche
from ipynb.fs.full.Indexation import fonction_grammaticale
from ipynb.fs.full.Indexation import synant

st.title('Word Processor')
mot = st.text_input("Psst try to type a word here and see what u get ;)")
if mot:
    defi = definition(mot)
    fg = fonction_grammaticale(mot)
    documents, poids, tfidf, freq, pert = recherche(mot)

    if (defi =="" and not documents and pert == ""):
        st.markdown("<h1 style='text-align: center; color: red; font-variant: small-caps;'>Word does not exist <br> maybe try again ?</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([3, 3, 3])
        with col2:
            st.image('C:/Users/SKYMIL/PycharmProjects/pythonProject/anxiety (1).png', width=200, output_format="auto")
        st.stop()
    st.subheader("Definition")
    if (defi == ""):
        st.write("No definition , Word seems to be unfound")
    else:
        st.write(mot+"("+fg[0]+")")
        st.write(defi)
    st.subheader("Search Result")

    if not documents or pert=="":
        st.markdown(
            "<h1 style='text-align: center; color: red; font-variant: small-caps;'>Ooops , No results were found <br> maybe try again ?</h1>",
            unsafe_allow_html=True)
        col1,col2,col3 = st.columns([3, 3, 3])
        with col2:
            st.image('C:/Users/SKYMIL/PycharmProjects/pythonProject/person.png', width=200, output_format="auto")
        st.stop()

    data1 = {
        'documents': documents ,
        'poids': poids ,
        'tfidf': tfidf,
        'frequence' : freq
    }

    df = pd.DataFrame(data1)
    st.table(df)

    st.subheader("Synonyms & Antonyms")

    synonyms,antonyms = synant(mot)

    data2 = {
        'synonyms': synonyms
    }
    df2 = pd.DataFrame(data2)
    data3 = {
        'antonyms': antonyms
    }
    df3 = pd.DataFrame(data3)


    col1,col2 = st.columns(2)
    with col1:
        st.subheader('Synonyms')
        num_element_df2 = len(df2)
        if num_element_df2>10:
            st.table(df2.head(10))
        else:
            st.table(df2)
    with col2:
        st.subheader('Antonyms')
        num_element_df3 = len(df3)
        if num_element_df3 > 10:
            st.table(df3.head(10))
        else:
            st.table(df3)

    st.subheader('The most relevant document.')
    st.write(pert)



