import time
import random
import streamlit as st

bar = st.progress(0, text='waiting')

for i in range(100):
    # bar.progress(i + 1, text='waiting' + '.' * (i // 10 % 3))
    # time.sleep(random.random() / (i + 1))
    pass
else:
    bar.empty()
    st.title('Welcome to My Blog')

    st.write('\n')
    st.write('\n')

    st.write('''
    このサイトでは，Pythonの入門書を読み終えた方々がさらに深くPythonを学べるよう，9つのトピックについて断片的に紹介します。
    それぞれのトピックは初心者が次のステップへ進むために重要でありながらも，魅力的で興味が尽きない内容です．

    ただし，このサイトの情報は[Python公式ドキュメント](python.org)のような総合的なリソースに比べて包括的ではなく，また，部分的に説明が不十分な箇所も存在します．
    ですので，特定のトピックに興味が湧いた場合は，公式ドキュメントや書籍，他のブログ等を積極的に参照していただくことをお勧めします．

    このサイトが皆様のプログラミングでの表現力を広げる機会になることを願って．
    ''')

    st.write('<p style="text-align:right;">筆者</p>', unsafe_allow_html=True)

    st.balloons()
