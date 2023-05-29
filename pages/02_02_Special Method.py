import streamlit as st

st.title('特殊メソッド')

st.header('1. 特殊メソッドとは')

st.write('''
他のオブジェクト指向言語を学んだ経験があれば，Pythonの`list`に，`list.length()`のような長さを取得するメソッドがないことに疑問を抱いたことがあるはずです．

Pythonではある`list`の長さを取得するには`len()`を利用しますが，内部的には`list`は`__len__()`というメソッドを持っており，`len()`は`__len__()`を呼び出しています．

またVScodeのようなIDEでPythonを利用していると，よくサジェストに`__xxx__`のようなメソッドが表示されます．それらは**特殊メソッド**(special method)と呼ばれ，組み込み関数の`len`や`abs`，または演算子`+`や`-`，`[]`等の振る舞いを定義します．
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

st.caption('''\

''')

st.info('あなたがPythonインタプリタでない限り，特殊メソッドを直接呼び出すことはありません')

st.markdown('''
以下に特殊メソッドの一覧を示します．(2023/05/28時点ではChatGPTv4に出力させており，必ずしも正しい情報を提供しているとは限りません)

| 特殊メソッド | 説明 | 補足事項 |
|-------------|-----|-------|
| `__new__(cls, ...)` | オブジェクトの生成を制御します。これはクラスメソッドで、オブジェクトのインスタンス化の前に呼び出されます。 |  |
| `__init__(self, ...)` | オブジェクトの初期化。コンストラクタとも呼ばれます。 | `self`は常に最初の引数になります。 |
| `__del__(self)` | オブジェクトが破棄されるときに呼び出される。デストラクタとも呼ばれます。 | `__del__`は頻繁に使用すべきではありません。リソースのクリーンアップには代わりにコンテクストマネージャを使用することが推奨されています。 |
| `__repr__(self)` | オブジェクトの「公式」文字列表現を返します。 | `eval(repr(x))`を使用して、オブジェクトを再構築できるように、これは可能な限り正確な表現を返すべきです。 |
| `__str__(self)` | オブジェクトの「非公式」または「便利」な文字列表現を返します。 | このメソッドは`str()`内で呼び出され、人間にとって読みやすい形式でオブジェクトを表現します。 |
| `__add__(self, other)` | "+"演算子のオーバーロード。`self + other`を定義します。 |  |
| `__sub__(self, other)` | "-"演算子のオーバーロード。`self - other`を定義します。 |  |
| `__mul__(self, other)` | "*"演算子のオーバーロード。`self * other`を定義します。 |  |
| `__truediv__(self, other)` | "/"演算子のオーバーロード。`self / other`を定義します。 | Python 3では`__div__`が`__truediv__`に置き換えられました。 |
| `__mod__(self, other)` | "%"演算子のオーバーロード。`self % other`を定義します。 |  |
| `__pow__(self, other)` | "**"演算子のオーバーロード。`self ** other`を定義します。 |  |
| `__lt__(self, other)` | "<"演算子のオーバーロード。`self < other`を定義します。 |  |
| `__le__(self, other)` | "<="演算子のオーバーロード。`self <= other`を定義します。 |  |
| `__eq__(self, other)` | "=="演算子のオーバーロード。`self == other`を定義します。 |  |
| `__ne__(self, other)` | "!="演算子のオーバーロード。`self != other`を定義します。 |  |
| `__gt__(self, other)` | ">"演算子のオーバーロード。`self > other`を定義します。 |  |
| `__ge__(self, other)` | ">="演算子のオーバーロード。`self >= other`を定義します。 |  |
| `__len__(self)` | `len()`関数のオーバーロード。オブジェクトの「長さ」を定義します。 | 主にシーケンス（リストやタプル）やコレクション（辞書やセット）で使われます。 |
| `__getitem__(self, key)` | `self[key]`アクセスを定義します。 | シーケンスやマッピングに使用されます。 |
| `__setitem__(self, key, value)` | `self[key] = value`代入を定義します。 | シーケンスやマッピングに使用されます。 |
| `__delitem__(self, key)` | `del self[key]`操作を定義します。 | シーケンスやマッピングに使用されます。 |
| `__iter__(self)` | オブジェクトに対するイテレーションを定義します。`for x in self`の動作をコントロールします。 |  |
| `__contains__(self, item)` | `item in self`チェックを定義します。 | デフォルトでは、このメソッドは`__iter__()`または`__getitem__()`を使用してアイテムを探します。 |
| `__call__(self, *args, **kwargs)` | オブジェクトを関数として呼び出すことを可能にします。`self(args, kwargs)` |  |
| `__enter__(self)` | コンテクストマネージャとしてのオブジェクトのエントリポイントを定義します。`with self:`ブロックの開始時に呼び出されます。 | `with`ステートメントと共に使用されます。 |
| `__exit__(self, exc_type, exc_value, traceback)` | コンテクストマネージャとしてのオブジェクトのエグジットポイントを定義します。`with self:`ブロックの終了時に呼び出されます。 | `with`ステートメントと共に使用されます。 |
| `__getattribute__(self, name)` | 属性アクセスを制御します。`self.name` |  |
| `__setattribute__(self, name, value)` | 属性の設定を制御します。self.name = valueという形式の属性設定が試みられた時に呼び出されます。 |  |
| `__delattribute__(self, name)` | 属性の削除を制御します。del self.nameという形式の属性削除が試みられた時に呼び出されます。 |  |
| `__getattr__(self, name)` | `self.name`を定義します。特殊メソッド`__getattribute__`が属性を見つけられない場合に呼び出されます。 | |
| `__setattr__(self, name, value)` | 属性設定を制御します。`self.name = value` |  |
| `__delattr__(self, name)` | 属性削除を制御します。`del self.name` |  |
| `__hash__(self)` | `hash(self)`を定義します。オブジェクトがハッシュ可能かどうかを決定します。 | ハッシュ可能なオブジェクトは辞書のキーとして使用できます。 |
| `__bool__(self)` | `bool(self)`を定義します。オブジェクトの真偽値を決定します。 | デフォルトでは、このメソッドは`__len__()`を使用します。`__len__()`が0を返すと、`__bool__()`は`False`を返します。それ以外の場合、`True`を返します。 |
| `__abs__(self)` | `abs(self)`を定義します。 | 絶対値を返すべきです。 |
| `__round__(self, n)` | `round(self, n)`を定義します。 | n桁で四捨五入するべきです。 |
| `__floor__(self)` | `math.floor(self)`を定義します。 |  |
| `__ceil__(self)` | `math.ceil(self)`を定義します。 |  |
| `__trunc__(self)` | `math.trunc(self)`を定義します。 |  |
| `__pos__(self)` | `+self`を定義します。 |  |
| `__neg__(self)` | `-self`を定義します。 |  |
| `__invert__(self)` | `~self`を定義します。 | ビット反転です。 |
| `__lshift__(self, other)` | `self << other`を定義します。 | ビットシフトです。 |
| `__rshift__(self, other)` | `self >> other`を定義します。 | ビットシフトです。 |
| `__and__(self, other)` | `self & other`を定義します。 | ビット単位のANDです。 |
| `__or__(self, other)` | `self \| other`を定義します。 | ビット単位のORです。 |
| `__xor__(self, other)` | `self ^ other`を定義します。 | ビット単位のXORです。 |
| `__index__(self)` | `self`を整数として返します。 | `bin()`, `hex()`, `oct()`などで使われます。 |
| `__complex__(self)` | `complex(self)`を定義します。 |  |
| `__int__(self)` | `int(self)`を定義します。 |  |
| `__float__(self)` | `float(self)`を定義します。 |  |
| `__bytes__(self)` | `bytes(self)`を定義します。 |  |
| `__format__(self, format_spec)` | `format(self, format_spec)`を定義します。 | 文字列フォーマットです。 |
| `__radd__(self, other)` | 右からの "+" 演算子のオーバーロード。 | other + self を定義します。 |
| `__rsub__(self, other)` | 右からの "-" 演算子のオーバーロード。 | other - self を定義します。 |
| `__rmul__(self, other)` | 右からの "*" 演算子のオーバーロード。 | other * self を定義します。 |
| `__rtruediv__(self, other)` | 右からの "/" 演算子のオーバーロード。 | other / self を定義します。 |
| `__rfloordiv__(self, other)` | 右からの "//" 演算子のオーバーロード。 | other // self を定義します。 |
| `__rmod__(self, other)` | 右からの "%" 演算子のオーバーロード。 | other % self を定義します。 |
| `__rdivmod__(self, other)` | 右からの "divmod()" のオーバーロード。 | divmod(other, self) を定義します。 |
| `__rpow__(self, other)` | 右からの "**" 演算子のオーバーロード。 | other ** self を定義します。 |
| `__rlshift__(self, other)` | 右からの "<<" 演算子のオーバーロード。 | other << self を定義します。 |
| `__rrshift__(self, other)` | 右からの ">>" 演算子のオーバーロード。 | other >> self を定義します。 |
| `__rand__(self, other)` | 右からの "&" 演算子のオーバーロード。 | other & self を定義します。 |
| `__ror__(self, other)` | 右からの "\|" 演算子のオーバーロード。 | other \| self を定義します。 |
| `__rxor__(self, other)` | 右からの "^" 演算子のオーバーロード。 | other ^ self を定義します。 |
| `__iadd__(self, other)` | "+=" 演算子のオーバーロード。 | self += other を定義します。 |
| `__isub__(self, other)` | "-=" 演算子のオーバーロード。 | self -= other を定義します。 |
| `__imul__(self, other)` | "*=" 演算子のオーバーロード。 | self *= other を定義します。 |
| `__itruediv__(self, other)` | "/=" 演算子のオーバーロード。 | self /= other を定義します。 |
| `__ifloordiv__(self, other)` | "//=" 演算子のオーバーロード。 | self //= other を定義します。 |
| `__imod__(self, other)` | "%=" 演算子のオーバーロード。 | self %= other を定義します。 |
| `__ipow__(self, other)` | "**=" 演算子のオーバーロード。 | self **= other を定義します。 |
| `__ilshift__(self, other)` | "<<=" 演算子のオーバーロード。 | self <<= other を定義します。 |
| `__irshift__(self, other)` | ">>=" 演算子のオーバーロード。 | self >>= other を定義します。 |
| `__iand__(self, other)` | "&=" 演算子のオーバーロード。 | self &= other を定義します。 |
| `__ior__(self, other)` | "\|=" 演算子のオーバーロード。 | self \|= other を定義します。 |
| `__ixor__(self, other)` | "^=" 演算子のオーバーロード。 | self ^= other を定義します。 |
| `__dir__(self)` | `dir(self)`を定義します。オブジェクトの属性の一覧を返すべきです。 | |
| `__class__(self)` | オブジェクトのクラスを取得します。 | |
| `__dict__(self)` | オブジェクトの属性ディクショナリを取得します。 | |
| `__sizeof__(self)` | `sys.getsizeof(self)`を定義します。オブジェクトのバイト数を返すべきです。 | |
| `__get__(self, instance, owner)` | ディスクリプター（descriptor）に対する属性取得を制御します。 | ディスクリプターは、属性へのアクセスを制御するための特殊メソッドです。 |
| `__set__(self, instance, value)` | ディスクリプターに対する属性設定を制御します。 | ディスクリプターは、属性へのアクセスを制御するための特殊メソッドです。 |
| `__delete__(self, instance)` | ディスクリプターに対する属性削除を制御します。 | ディスクリプターは、属性へのアクセスを制控するための特殊メソッドです。 |
| `__reversed__(self)` | `reversed(self)`を定義します。オブジェクトの逆順イテレーションを制御します。 | |
| `__slots__` | オブジェクトの属性を制限します。これによりメモリ使用量を削減できます。 | これは実際にはメソッドではなく、特別なクラス変数です。 |
''')

st.write('\n')

st.header('2. 特殊メソッドの利用例')
st.write('''\
これらの特殊メソッドのうち，特に解釈が困難であると思われるものについて説明します．
''')

st.subheader('2.1. `__new__`, `__init__`, `__del__`')
st.subheader('2.2. `__rxxx___`')
st.subheader('2.3. `__ixxx__`')

st.header('3. 特殊メソッドの実装例')
st.write('''
特殊メソッドを利用してPythonで値オブジェクトを実現する方法を紹介します．
''')

st.code('''
from __future__ import annotations
from typing import Any


class ValueClass:
    class RebindError(TypeError):
        pass

    class UnbindError(TypeError):
        pass

    def __init__(self: ValueClass, value: Any) -> None:
        self.something_field = value

    def __setattr__(self: ValueClass, __name: str, __value: Any) -> None:
        if __name in self.__dict__:
            raise self.RebindError(f"Can't rebind ValueClass({__name})")
        self.__dict__[__name] = __value

    def __delattr__(self: ValueClass, __name: str) -> None:
        if __name in self.__dict__:
            raise self.UnbindError(f"Can't unbind ValueClass({__name})")
        raise NameError(__name)

    def __eq__(self: ValueClass, other: ValueClass):
        return self.something_field == other.something_field

''')
