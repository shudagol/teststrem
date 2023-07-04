import streamlit as st
st.title('Test stream lit')
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
