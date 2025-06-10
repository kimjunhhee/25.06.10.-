import streamlit as st
st.title("나의 첫 app")
st.write("hello")
name=st.text_input("이름 입력")
if name:
  if name=="김준희":
    st.succcess("반갑습니다. 김준희님!")
  else:
    st.warning("누구세요?)
