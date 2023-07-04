import streamlit as st
st.title('Hello guys')
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
