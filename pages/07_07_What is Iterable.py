import streamlit as st

st.title('Iterableを知る')

st.header('01. Iterableとは')

st.write('''
Iterableとは，反復可能なオブジェクトの意味で，**要素を一度に一つずつ返せる**オブジェクトのことを指します．

最たる例は`list`で，次いで`tuple`が挙げられます．また`str`も文字の列ですから，一つ一つの文字を返すことができるIterableです．
他に`dict`や`set`なども要素を一つずつ返すことができるのでIterableです．さらには`range`や`enumerate`，`map`オブジェクトも同様にIterableです．

一方で`int`や`float`，`function`や`module`などは要素を一つずつ返すことができないので，Iterableではありません．
''')

st.code('''
>>> a = [1, 2, 3,]
>>> for i in a:
...     print(i)
...
1
2
3
>>> b = 'py'
>>> for s in b:
...     print(s)
...
p
y
>>> c = {'a': 1, 'b': 2, 'c': 3}
>>> for k in c:
...     print(k)
...
a
b
c
''')

st.header('02. IterableとIterator')