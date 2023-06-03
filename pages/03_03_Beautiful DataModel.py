import streamlit as st
import streamlit.components.v1 as components


def mermaid(code: str) -> None:
    components.html(f"""
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
                    height=800,
                    scrolling=True)


st.title('美しいデータモデル')

st.header('01. Pythonの一貫性')
st.write('''
Pythonにおける「数」の実装を題材に，Pythonのデータモデルへの美学を紹介します．
''')

st.write('''
`numbers`モジュールは，Pythonの数値型に関する一連の抽象基底クラスを提供します．
''')

st.code('''
>>> import numbers
>>> dir(numbers)
[..., 'Complex', 'Integral', 'Number', 'Rational', 'Real', ...]
''')

st.write('''
我々の世界がそうであるように，Pythonでも数値は階層的に定義されます．

`Number :> Complex :> Real :> Rational :> Integral`

順に，

- `Number`
  - 一般的な数値を表す抽象基底クラス
- `Complex`
  - 複素数を表す抽象基底クラス
- `Real`
  - 実数を表す抽象基底クラス
  - `Complex`のサブクラスで，複素数の一部（虚部が0の数）を表します
- `Rational`
  - 有理数を表す抽象基底クラス
  - `Real`のサブクラスで、実数の一部（分数で表現できる数）を表します
- `Integral`
  - 整数を表す抽象基底クラス
  - `Rational`のサブクラスで、有理数の一部（分母が1の数）を表します

また，各抽象基底クラスは，以下の抽象メソッドを持ちます．

- `Number`
  - 基本的な算術演算子を定義します．
  - `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, ...
- `Complex`
  - 複素数型が満たすべきメソッドを定義します
  - `__abs__`, `__complex__`, `real`, `imag`, `conjugate`
- `Real`
  - 実数型が満たすべきメソッドを定義します
  - `__float__`, `__round__`, `__trunc__`, `__floor__`, `__ceil__`, ...
- `Rational`
  - 有理数型が満たすべきメソッドを定義します
  - `numerator`, `denominator`
- `Integral`
  - 整数型が満たすべきメソッドを定義します
  - `__int__`, `__index__`, ...

そして，我々がよく知る具象クラスとは次のように対応付されます．

- `Number`
  - これはすべての数値型の最も一般的な抽象基底クラスで，すべての数値型（`int`、`float`、`complex`、`bool`など）がこのクラスを継承します
- `Complex`
  - この抽象基底クラスは、`complex`および`Real`クラスが継承します
- `Real`
  - この抽象基底クラスは，`float`、`Rational`、および`Decimal`が継承します
- `Rational`
  - この抽象基底クラスは`fractions.Fraction`および`Integral`が継承します
- `Integral`
    この抽象基底クラスは、`int`および`bool`が継承します
''')

st.write('''
UML図を以下に示します．
''')

mermaid('''
classDiagram
  class Number {
     __add__(self, other)
     __sub__(self, other)
     __mul__(self, other)
     __truediv__(self, other)
  }
  class Complex {
     __abs__(self)
     __complex__(self)
  }
  class Real {
     __round__(self, ndigits)
     __floor__(self)
     __ceil__(self)
  }
  class Rational {
     numerator
     denominator
  }
  class Integral {
     __int__(self)
     __index__(self)
  }
  class int {
     bit_length(self)
     to_bytes(self, length, byteorder, *, signed=False)
  }
  class bool {
     __and__(self, other)
     __or__(self, other)
     __xor__(self, other)
  }
  class float {
     is_integer(self)
     as_integer_ratio(self)
  }
  class complex {
     real
     imag
  }
  class Fraction {
     from_float(flt)
     from_decimal(dec)
  }
  class Decimal {
     sqrt(self)
     ln(self)
     exp(self)
  }
  Number <|-- Complex
  Complex <|-- Real
  Real <|-- Rational
  Rational <|-- Integral
  Integral <|-- int
  int <|-- bool
  Real <|-- float
  Complex <|-- complex
  Rational <|-- Fraction
  Real <|-- Decimal
''')

st.write('''
このような階層構造を持つことで，Pythonのさまざまな型に対応する一貫したインターフェースが実現できます．

例えば，Pythonであればいかなる型の数値でも，加算や乗算などの基本的な算術演算をサポートします．これは，すべての数値型が`Numbers`抽象基底クラスを継承しているためです．
''')

st.code('''
>>> 1 + True
2
>>> 1 + 1.0
2.0
>>> 1 + 1j
(1+1j)
''')
