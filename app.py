import streamlit as st
from textblob import TextBlob


def main():
	st.title("Spelling Checker Apps")
	st.subheader("Build With Python & Streamlit")
	user=st.text_input("Enter a Sentence")
	obj=TextBlob(user)
	if st.button("Process"):
		st.success(obj.correct())



main()