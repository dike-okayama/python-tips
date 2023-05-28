import streamlit as st

st.title("クロージャについて")

st.header("1. クロージャとは何者か")
st.text(
    """\
クロージャとは、関数とその関数が定義された環境を合わせたものです。

"""
)

st.header("2. クロージャの例")
st.code(
    """\
def outer(a, b):
    def inner():
        return a + b
    return inner

"""
)
