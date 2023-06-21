import streamlit as st

st.title('文と式と演算子と')

st.write('''
Pythonには前章で紹介した代入文の他にも，様々な種類の文があるため，ここではそれらを紹介します．
''')

st.header('1. if statement')

st.write("`if`文は条件として与えられたオブジェクトが真と評価される場合に，その後の文を実行します．")

st.write('''
`if`文は以下の手順で評価されます．
''')

st.write('''
「Pythonicなコード」有名な例として，シーケンスが空かどうかの判定には`len()`関数を利用**しない**が存在します．
''')

st.code('''
seq = [1, 2, 3]
if len(seq) > 0:  # not pythonic way
    print('seq is not empty')
if seq:  # pythonic way
    print('seq is not empty')
''')

st.header('2. for statement')
st.header('3. while statement')
st.header('4. try statement')
st.header('5. with statement')

st.header('6. del statement')

st.write(
    "del文は名前空間から**名前とオブジェクトの参照(紐付け)を削除**します．名前空間とは，変数名（つまりオブジェクトへの参照）と実際のオブジェクトがマッピングされる場所を指します．"
    "参照がなくなると，削除された変数名ではそのオブジェクトへアクセスできません．")

st.code('''
>>> a = 1
>>> del a
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
''')

st.write("また，`del`文は辞書のキーを削除するのにも用いられます．")
st.code('''
>>> a = [1, 2, 3, 4]
>>> del a[1]
>>> a
[1, 3, 4]
''')

st.write("リストのインデックスはリスト内の各要素への参照を表しており，この参照も一種の名前空間と捉えることができます．"
         "`del`文により特定のインデックスとその位置の要素との紐付けが削除され，その結果としてリストからその要素が削除されます．"
         "なお，削除後のリストでは動的に元の2番目以降の要素が前にシフトするため，削除したインデックスが二度と使えないということはありません．")

st.write("全要素を削除することも可能です．")
st.code('''
>>> a = [1, 2, 3, 4]
>>> del a[:]
>>> a
[]
''')

st.write("`del a[:]`とすることで，リスト`a`の全要素への参照が削除され，結果的にリスト`a`は空になります．")

st.write("ここで，いずれの場合でも直接的にオブジェクトを削除しているわけではないことに注意してください．")

st.write('この事実を端的に表現する良い例をMike Driscollが紹介しています．')
st.code('''
>>> my_list = [1, 2, 3, 4]
>>> for item in my_list:
    del item
>>> my_list
[1, 2, 3, 4]
''')
st.caption('`del`文はリストの要素を削除しません．名前空間からitemという変数を削除するのみです．')

st.write(
    "もちろん変数の削除によりオブジェクトへの参照がなくなり，間接的にオブジェクトが削除されることはあり得ます．"
    "特に特殊メソッド`__del__`はオブジェクトがガベージコレクトされる際に一度だけ呼び出される関数であり，`__del__()`が`del`文の振る舞いを定義するものではないことに留意してください．"
)

st.code('''
>>> class S:
...    def __del__(self):
...        print('called __del__()')
...
>>> s = S()
>>> del s
called __del__()
''')
st.caption(
    '`del s`により，`s`が名前空間から削除され，オブジェクトへの参照がなくなりました．結果としてオブジェクトはガベージコレクトされ，`__del__()`が呼び出されます．'
)

st.code('''
>>> class S:
...    def __del__(self):
...        print('called __del__()')
...
>>> s = t = S()
>>> del s
''')
st.caption(
    '`del s`により，`s`が名前空間から削除され，オブジェクトへの参照が1つ減りましたが，依然として`t`からの参照は残っています．'
    'オブジェクトはガベージコレクトされず，`__del__()`も呼び出されません．')

st.info(
    '`__del__()`は自身のオブジェクトがガベージコレクトされる直前に，外部リソースを開放するために利用されるもので，適切に実装するには難易度がやや高い代物です．'
)
