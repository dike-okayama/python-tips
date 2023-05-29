import streamlit as st

st.title("デコレータとクロージャ")

st.header('1. 高階関数について')
st.write('''
Pythonの関数は**第一級オブジェクト**(first-class object)です．これが意味するところは，整数や文字列，リストといったオブジェクトと同様に，
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

st.info('通常functools.lru_cache()は次節で紹介するデコレータ構文とともに利用されます')

st.header('2. デコレータとは')

st.write('''
デコレータとは，関数を引数に取り，別の関数を返す高階関数です．その関数の定義を変更することなく，関数の振る舞いを拡張することができます．
''')

st.write('''
（陳腐な例ですが）ある関数の実行時間を計測する例を考えましょう．
''')

st.code('''
>>> def func():
...     ...
...
>>> import time
>>> start = time.time()
>>> func()
>>> end = time.time()
>>> print(end - start)
x.xxxxxxxx
''')
st.caption('関数の実行前後で`time.time()`を呼び出し，その差を計算しています．')

st.write('''
計測が今回限りであったり，計測対象の関数が一つだけであれば，上のような方法でも問題ありませんが，そうでない場合は毎度同じようなコードを書くのは面倒です．

このようなケースではデコレータが有効に働きます．共通の処理を高階関数として定義し，それをデコレータとして利用することで，関数の振る舞いを拡張しましょう．
''')

st.code('''
>>> def decorator(func):
...     def wrapper():
...         start = time.time()
...         func()
...         end = time.time()
...         print(end - start)
...     return wrapper
...
>>> @decorator
>>> def func():
...     ...
...
>>> @decorator
>>> def func2():
...     ...
...
>>> func()
x.xxxxxxxx
>>> func2()
y.yyyyyyyy
''')
st.caption('`@decorator`は，`func = decorator(func)`と等価です．')

st.write('''
以前のコードと比較すると，非常に簡潔で再利用性が高まりました．

特に修飾される関数が引数を取る場合は，可変長引数やキーワード引数を利用してください．
''')

st.code('''
>>> def decorator(func):
...    def wrapper(*args, **kwargs):
...        func(*args, **kwargs)
...    return wrapper
...
>>> @decorator
>>> def func(arg1, arg2, kwarg1=None, kwarg2=None):
...    ...
...
>>> func(1, 2, kwarg1=3, kwarg2=4)
...
''')
st.info('''
2行目の`*args`, `**kwargs`の`*`,`**`はそれぞれ可変長引数とキーワード引数を受け取ることを明示しています．\n
3行目の`*args`, `**kwargs`の`*`,`**`はアンパック演算子です．
''')

st.markdown('---')

st.write('''
尚`@`にはデコレータ以外に，Python3.5で導入された`@`(matmul)行列積演算子としての役割も存在します．（デコレータ自体はそれより以前から存在しました）

特に`numpy.ndarray`等では，`a @ b`演算子は`a.__matmul__(b)`を呼び出し，行列のドット積を計算します．
''')

st.code('''
>>> import numpy as np
>>> a = np.array([[1, 1], [1, 1]])
>>> a @ a
array([[2, 2],
       [2, 2]])
''')

st.markdown('---')
st.header("3. クロージャとは")

st.write('''
クロージャとは，非グローバルな変数にアクセスできる関数のことです．
''')

st.write("""
関数は実行後，通常そのローカル環境は破棄されます．一度関数を抜けると，その環境には二度とアクセスできません．
""")

st.code('''
>>> def func():
...     var = 1
...     return var
...
>>> func()
1
''')
st.caption('`func()`の実行中ローカル変数`var`は存在しますが，実行後には`var`は破棄されます．')

st.write('''
しかし，クロージャでは関数のローカル環境を記憶します．
''')

st.code('''
>>> def enclosure():
...     free_var = 1
...     def closure():
...         return free_var
...     return closure
...
>>> closure = enclosure()
>>> closure()
1
''')
st.caption('''
`enclosure()`の実行後も`free_var`は破棄されません．
''')

st.info('クロージャを通して非グローバル変数`free_var`にアクセスできました．')

st.write('''
もちろん読み取りだけではなく，書き込みも可能です．
''')

st.code('''
>>> def enclosure():
...     free_var = 1
...     def increment():
...         nonlocal free_var
...         free_var += 1
...         return free_var
...     def decrement():
...         nonlocal free_var
...         free_var -= 1
...         return free_var
...     def get():
...         return free_var
...     return increment, decrement, get
...
>>> inc, dec, get = enclosure()
>>> get()
1
>>> inc()
2
>>> dec()
1
''')
st.caption('''
nonlocalキーワードは，一つ外側のスコープにある変数を参照することを明示します．
''')

st.write("""
まとめると，クロージャとは，関数内部で定義されてはいないが，内部で参照されている非グローバルな変数を記憶している関数のことです．
（グローバルスコープではない）拡張されたスコープを有する関数ともいえます．

ある関数が自身の作成事に存在した変数の環境を「閉じ込め」，後から呼び出し時にその環境の利用を可能にすることから，クロージャはまた**関数閉包**とも呼ばれます．
""")

st.info('文脈によっては，その関数が作成された環境（変数とその値）を指すこともあります．')

st.header('4. クロージャの応用')
st.write('''
クロージャの利点の一つとして，グローバル変数を減らし，データの安全性を高める点があります．

例えば二項係数の計算が複数回行われる場合，予め階乗テーブルを作成しておくと効率的に二項係数を計算できます．
''')

st.code('''
>>> max_n = 100
>>> facts = [1] * max_n  # facts[i] := i!
>>> for i in range(1, max_n):
...     facts[i] = facts[i - 1] * i
...
>>> def combination(n, r):
...     return facts[n] // facts[r] // facts[n - r]
...
>>> combination(100, 50)
100891344545564193334812497256
''')

st.write('''
上のコードでは`combination()`関数は`facts`というグローバル変数を参照していますが，誤って`facts`を変更してしまう恐れがあります．

`facts`が`combinations`以外から参照されないのであれば，`facts`をクロージャによって隠蔽した方が安全です．
''')

st.code('''
>>> def make_combination(max_n):
...     facts = [1] * max_n
...     for i in range(1, max_n):
...         facts[i] = facts[i - 1] * i
...     def combination(n, r):
...         return facts[n] // facts[r] // facts[n - r]
...     return combination
...
>>> combination = make_combination(max_n=100)
>>> combination(100, 50)
100891344545564193334812497256
''')
st.info('''
`facts`は非グローバル変数となり，誤って変更される可能性はなくなりました．
''')
