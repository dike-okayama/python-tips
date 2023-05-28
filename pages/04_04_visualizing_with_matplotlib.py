import streamlit as st

st.title("Visualizing with Matplotlib")

st.text(
    """\
ここでは、Matplotlibを使ってグラフを描画する方法を紹介します．
...
"""
)

st.header("1. matplotlibのインポート")
st.caption(
    """\
numpyやpandasをnpやpdとしてインポートするのと同じように、matplotlibにも慣習的な読み込み方法が存在します．
"""
)
st.code(
    """\
import matplotlib as mpt
import matplotlib.pyplot as plt
"""
)

st.text(
    """\
特にIpython notebook内で対話的にmatplotlibを利用する場合は，%matplotlibコマンドを使います．
%matplotlib inline を使用すると，Matplotlibプロットは静的なイメージとして表示されます．コードセルの出力としてプロットが表示され，プロット自体は静的な画像としてレンダリングされます．プロットを変更したり操作することはできません．
%matplotlib notebook を使用すると，Matplotlibプロットは対話型の表示モードで表示されます．プロットはインタラクティブなウィジェットとして表示され，プロットをズームしたりパンしたりすることができます．また，プロットを変更したりアップデートしたりすることも可能です．

"""
)
