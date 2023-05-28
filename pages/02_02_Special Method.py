import streamlit as st

st.title('特殊メソッド')
st.write('''\
VScodeのようなIDEでPythonを利用していると，よくサジェストに`__xxx__`のようなメソッドが表示されます．それらは特殊メソッドであり，多くの特殊メソッドは組み込み関数の`len`や`abs`，または演算子`+`や`-`，`[]`の振る舞いを定義します．
''')
st.code('''\
>>> class S:
...    def __len__(self):
...        print('called __len__()')
...        return 0
...    def __add__(self, other):
...        print('called __add__()')
...
>>> s = S()
>>> len(sample)
called __len__()
0
>>> s + s
called __add__()
''')

st.write('''\
他のオブジェクト指向言語を学んだ経験があれば，Pythonの`list`に，`list.length()`のような長さを取得するメソッドがないことに疑問を抱いたことがあるでしょう．

我々はある`list`の長さを取得するには`len()`を利用しますが，内部的には`list`は`__len__()`という特殊メソッドを持っており，`len()`は`__len__()`を呼び出しています．
''')

st.info('あなたがPythonインタプリタでない限り，特殊メソッドを直接呼び出すことはありません')
