import streamlit as st

st.title("クロージャ")

st.header('1. 高階関数について')
st.write('''
Pythonの関数は第一級オブジェクトです．これが意味するところは，整数や文字列，リストといったオブジェクトと同様に，
関数も変数に代入したり，別の関数の引数として渡したり，別の関数の戻り値として返したりすることができるということです．

特に他の関数を引数に取るか，戻り値として関数を返すか，あるいはその両方を行う関数を**高階関数**(higher-order function)と呼びます．
''')

st.write('''
身近な例の一つは，組み込み関数の`sorted()`やシーケンスの組み込みメソッド`.sort()`です．これらは，ソートの基準となる関数を引数`key`に取ります．
''')

st.code('''
>>> a = [3, -2, 5, 1, -4]
>>> sorted(a, key=abs)
[1, -2, 3, -4, 5]
''')

st.caption('''
absは引数の絶対値を返します．そのため，3, -2, 5, 1, -4は，絶対値が小さい順に並べ替えらました．
''')

st.write('''
今では若干レガシーな匂いを発しつつある，`map()`や`filter()`も高階関数の代表例です．
''')

st.code('''
>>> a = map(lambda x: x * x, range(5))
>>> print(*a)
0 1 4 9 16
''')

st.write('''
これらはいずれも関数を引数に取る高階関数ですが，関数を返すような高階関数は，`functools.partial()`や`functools.lru_cache()`などがあります．
''')

st.code('''
>>> import functools
>>> def fibo(n):
...     if n < 2:
...         return n
...     return fibo(n - 1) + fibo(n - 2)
...
>>> memo_fibo = functools.lru_cache(fibo)
>>> memo_fibo(100)
354224848179261915075
''')

st.caption('''
`functools.ler_cache()`は，引数に取った関数の戻り値をキャッシュする関数を返します．
''')

st.header("2. クロージャとは")
st.text("""
クロージャとは、関数とその関数が定義された環境を合わせたものです。

""")

st.header("2. クロージャの例")
st.code("""\
def outer(a, b):
    def inner():
        return a + b
    return inner

""")
