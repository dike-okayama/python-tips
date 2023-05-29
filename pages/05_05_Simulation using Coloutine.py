import streamlit as st

st.title('コルーチンによる回転寿司顧客注文シミュレーション')

st.write('''\
顧客の来店から退店，またその間の寿司のパネル注文の離散事象シミュレーション（DES: Discrete Event Simulation）をコルーチンによって実現しましょう．

まずは簡単な仮定を置いたシミュレーションを行い，徐々に現実的なモデルでのシミュレーションを試みます．
''')

st.markdown('''\
## Contents

0. コルーチンとは
1. はじめてのシミュレーション
2. ランダムなシミュレーション
3. 現実に即したシミュレーション
4. より現実的なモデルへ

''')

st.header('0. コルーチンとは')

st.write('''\
コルーチンの本体はジェネレータです．ジェネレータ関数の定義には通常の関数定義の中で `yield` キーワードを使用します．
''')

st.code('''\
>>> def my_generator():
...     yield 1
...     yield 2
...     yield 3
...
>>> gen = my_generator()
>>> gen
<generator object my_generator at 0x105959d90>
''')

st.write('''\
ジェネレータから値を取得するには `next()` 関数を使用します．`next()`は引数として与えられたジェネレータを次の`yield ...`まで実行し，`yield` の右辺の値を返します．
''')

st.code('''\
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3
''')

st.write('''\
通常の関数と異なるのは，`next()` を呼び出すと関数の実行が終了するのではなく，`yield` の右辺の値を返した後，関数の実行が一時停止することです．この遅延評価機構はフィボナッチ数列や無限数列の生成などに便利です．
''')

st.code('''\

>>> def fibo():
...    a, b = 0, 1
...    while True:
...        yield a
...        a, b = b, a + b
...
>>> fib = fibo()
>>> next(fib)
0
>>> next(fib)
1
>>> next(fib)
1
>>> next(fib)
2
>>> next(fib)
3
>>> next(fib)
5
>>> next(fib)
8
''')

st.info('ジェネレータは**一方的**に値を生成することに注意してください．')

st.markdown('''---''')

st.write('''\
コルーチンはジェネレータの拡張です．`.send(...)` メソッドにより，コルーチンに対して値を送信することが出来ます．

`.send(...)`は引数として与えられた値を，`yield`式そのものとして評価し，次の`yield`まで実行します．
''')

st.caption('特に代入式は右辺から実行されることに注意してください')

st.code('''\
>>> def my_coroutine():
...    a = yield 1
...    b = yield a
...    yield a + b
...
>>> colo = my_coroutine()  # 1
>>> next(colo)  # 2
1
>>> colo.send(2)  # 3
2
>>> colo.send(3)  # 4
5
''')

st.write('''\
(1) コルーチンオブジェクトが生成されました\n
(2) `next()`によって最初の`yield`まで実行され，`yield`の右辺の値(=1)が返り値となります\n
(3) `send()`によって渡された値(=2)は，`yield`式の値そのものとして評価されます．つまり，`yield 1` が2と評価され，aに2が代入されます．さらに`next()`同様`send()`は次の`yield`まで実行し，次の`yield`の右辺の値(a=2)が返り値となります\n
(4) `send()`によって渡された値(=3)は，`yield a`を3として評価し，bに3が代入されます．さらに次の`yield`まで実行され，次の`yield`の右辺の値(a+b=5)が返り値となります\n
''')

st.info('''\
コルーチンが `.send(...)` を受け付けるにはそれまでに一度 `next()` が呼び出されている必要があります．これはコルーチンの予備動作として必須の操作です
''')

st.write('''\
尚，空になったジェネレータやコルーチンに対し，`next()` を呼び出すと `StopIteration` 例外を送出します．
''')

st.code('''\
>>> def my_generator():
...    yield 1
>>> gen = my_generator()
>>> next(gen)
1
>>> next(gen)
Traceback (most recent call last):
  ...
StopIteration
''')

st.markdown('''
**Note**

-   コルーチンとジェネレータの違い
    -   ジェネレータとコルーチンの差異はその使用目的にあります．ジェネレータがデータの生成のために一方的に利用されるのに対し，コルーチンではデータの生成と消費の両方に利用されます
        -   例えばジェネレータがフィボナッチ数列を生成するなら，コルーチンはそれまでに受け取った値の累積平均を生成できます
''')

st.header('1. はじめての顧客シミュレーション')

st.markdown('''

離散事象シミュレーション（DES: Discrete Event Simulation）とは，システムを一連の事象（イベント）としてモデル化したシミュレーションの一種です．シミュレーションの「クロック」は均等には進まず，モデル化された次のイベントが発生するシミュレーション時刻にまで直接ジャンプします．例えば，顧客の入店から退店までの様子を上位レベルの観点からシミュレーションすると，最初のイベントは入店すること，次のイベントは 1 皿注文することです．注文にかかる時間が 1 分であっても 100 分であっても関係ありません．注文イベントが発生すればクロックは 1 回の操作で注文時刻に更新されます．これは均一かつ連続的にクロックが進んでいく連続シミュレーション（_continuous simulation_）とは対照的です．

### 仮定

-   顧客は **間もなく**到着する
-   顧客は **5 分後**に 1 皿注文する
-   顧客は **1 皿**注文してから**5 分後**に退店する
-   顧客に関して
    -   顧客は 1 人客として来店する
    -   5 人来店する

''')

st.code('''\
import queue

DEFAULT_NUMBER_OF_CUSTOMERS = 5
DEFAULT_END_TIME = 15


def customer_process(customer_id, start_time=0):
    time = yield (start_time, customer_id, 'お店に到着')
    time = yield (time, customer_id, '1皿注文')
    yield (time, customer_id, '退店')


def compute_duration(previous_action):
    if previous_action == 'お店に到着':
        return 5
    if previous_action == '1皿注文':
        return 5
    if previous_action == '退店':
        return 0


# シミュレーションのスタート
event_que = queue.PriorityQueue()
customers = {
    i: customer_process(i)
    for i in range(DEFAULT_NUMBER_OF_CUSTOMERS)
}

for _, process in customers.items():
    time, customer_id, action = next(process)
    event_que.put((time, customer_id, action))

simulation_time = 0
print('time |         events')
print('-' * 30)
while simulation_time < DEFAULT_END_TIME:
    if event_que.empty():
        print('*** end of events ***')
        break

    current_event = event_que.get()
    simulation_time, customer_id, previous_action = current_event
    print(f'{simulation_time:>3}m |' + ' ' * customer_id, f'{customer_id=}',
          previous_action)
    active_process = customers[customer_id]
    next_time = simulation_time + compute_duration(previous_action)
    try:
        next_event = active_process.send(next_time)
    except StopIteration:
        del customers[customer_id]
    else:
        event_que.put(next_event)
else:
    msg = '*** お店は閉店しました．{} 人の客がお店に取り残されています． ***'
    print(msg.format(event_que.qsize()))
''')

st.header('2. ランダムなシミュレーション')

st.markdown('''\
### 仮定

-   顧客は **3 分おき**に到着する
-   顧客は 来店から **$x_{order}$ 分後**に 1 皿注文する
-   顧客は 直前の注文から **$x_{order} + x_{eating}$ 分後**にもう $1$ 皿注文する
-   顧客は **$x_k$ 皿**注文してから **$x_{eating}$ 分後**に退店する
-   $x$ は $[1,x]$ の一様分布に基づく変数である，ただし整数値に丸められる
-   顧客に関して
    -   顧客は 1 人客として来店する
    -   5 人来店する
''')

st.code('''\
import random
import queue

random.seed(1991)

DEFAULT_NUMBER_OF_CUSTOMERS = 5
EATING_DURATION = 5  # <0>
ORDERING_DURATION = 5  # <1>
DEFAULT_END_TIME = 100


def customer_process(customer_id, plates, start_time=0):
    time = yield (start_time, customer_id, 'お店に到着')
    for _ in range(plates - 1):  # <2>
        time = yield (time, customer_id, '1皿注文')
    time = yield (time, customer_id, '最後の注文')
    yield (time, customer_id, '退店')


def compute_duration(previous_action):  # <3>
    if previous_action == 'お店に到着':
        return random.randint(1, ORDERING_DURATION)
    if previous_action == '1皿注文':
        return random.randint(1, EATING_DURATION + ORDERING_DURATION)
    if previous_action == '最後の注文':
        return random.randint(1, EATING_DURATION)
    if previous_action == '退店':
        return 0


# シミュレーションのスタート
event_que = queue.PriorityQueue()
customers = {
    i: customer_process(i, random.randint(1, 10), start_time=3 * i)  # <4>
    for i in range(DEFAULT_NUMBER_OF_CUSTOMERS)
}

for _, process in customers.items():
    time, customer_id, action = next(process)
    event_que.put((time, customer_id, action))

simulation_time = 0
print('time |         events')
print('-' * 30)
while simulation_time < DEFAULT_END_TIME:
    if event_que.empty():
        print('*** end of events ***')
        break

    current_event = event_que.get()
    simulation_time, customer_id, previous_action = current_event
    print(f'{simulation_time:>3.1f}m |' + '  ' * customer_id,
          f'{customer_id=}', previous_action)
    active_process = customers[customer_id]
    next_time = simulation_time + compute_duration(previous_action)
    try:
        next_event = active_process.send(next_time)
    except StopIteration:
        del customers[customer_id]
    else:
        event_que.put(next_event)
else:
    msg = '*** お店は閉店しました．{}人の顧客がお店に取り残されています． ***'
    print(msg.format(event_que.qsize()))
''')

st.header('3. より現実に即したシミュレーション')

st.markdown('''
### 仮定

-   顧客は **$3+x_c$ 分おき**に到着する
-   顧客は 来店から **$x_{order}$ 分後**に 1 皿注文する
-   顧客は 直前の注文から **$x_{order} + x_{eating}$ 分後**にもう $1$ 皿注文する
-   顧客は **$x_k$ 皿**注文してから **$x_{eating}$ 分後**に退店する
-   $x$ は 指数分布に基づく変数である（分布の平均値は適宜指定する）
-   顧客に関して
     -   顧客は 1 人客として来店する
     -   **$x_a$** 人来店する
''')

st.code('''
import random
import queue

random.seed(1991)

DEFAULT_NUMBER_OF_CUSTOMERS = 10
DEFAULT_CUSTOMER_INTERVAL = 3
EATING_DURATION = 5
ORDERING_DURATION = 3
DEFAULT_END_TIME = 300


def customer_process(customer_id, plates, start_time=0):
    time = yield (start_time, customer_id, 'お店に到着')
    for _ in range(plates - 1):
        time = yield (time, customer_id, '1皿注文')
    time = yield (time, customer_id, '最後の注文')
    yield (time, customer_id, '退店')


def compute_duration(previous_action):
    if previous_action == 'お店に到着':
        interval = ORDERING_DURATION
    if previous_action == '1皿注文':
        interval = EATING_DURATION + ORDERING_DURATION
    if previous_action == '最後の注文':
        interval = EATING_DURATION
    if previous_action == '退店':
        return 1
    return int(random.expovariate(1 / interval))


# シミュレーションのスタート
event_que = queue.PriorityQueue()
customers = {
    i: customer_process(i,
                        random.randint(1, 10),
                        start_time=3 * i +
                        random.randint(1, DEFAULT_CUSTOMER_INTERVAL))  # <4>
    for i in range(DEFAULT_NUMBER_OF_CUSTOMERS)
}

for _, process in customers.items():
    time, customer_id, action = next(process)
    event_que.put((time, customer_id, action))

simulation_time = 0
print('time |         events')
print('-' * 30)
while simulation_time < DEFAULT_END_TIME:
    if event_que.empty():
        print('*** end of events ***')
        break

    current_event = event_que.get()
    simulation_time, customer_id, previous_action = current_event
    print(f'{simulation_time:>3.1f}m |' + '  ' * customer_id,
          f'{customer_id=}', previous_action)
    active_process = customers[customer_id]
    next_time = simulation_time + compute_duration(previous_action)
    try:
        next_event = active_process.send(next_time)
    except StopIteration:
        del customers[customer_id]
    else:
        event_que.put(next_event)
else:
    msg = '*** お店は閉店しました．{}人の顧客がお店に取り残されています． ***'
    print(msg.format(event_que.qsize()))
''')

st.markdown('''
**Note**

-   `random.expovariate(lambd)` は，指数分布に従うランダムな浮動小数点を生成します
    -   パラメータ `lambd` は，単位時間に平均で発生するイベントの数を表します
        -   例えば `rambd=1` のとき，単位時間あたりに平均 1 回のイベントが発生することを意味します
        -   例えば `rambd=1/10` のとき，単位時間あたりに平均 1/10 回のイベントが発生することを意味します，これはおよそ 10 秒に 1 回発生するイベントが次に起こるまでのランダムな秒数を返すことになります

''')

st.header('4. より現実的なモデルへ')

st.markdown('''
-   商品注文時間，商品喫食時間を実データから算出し利用する
-   商品の種類を増やす
    -   実データから各商品の注文確率を計算し，その確率に基づく商品を注文させる
-   商品の喫食による，満腹度を考える
    -   満腹度に基づいて退店確率が更新されるようなモデル
-   ピーク時間帯を複数導入する，強度を設定する
    -   一般的な店舗では昼と夜にピーク時間があります．それぞれの来客数の増え方は店舗によって異なります
-   席数を導入する
    -   席数を超えた顧客が来店した場合，待ち時間が発生するようにします
-   単身顧客から複数人の顧客を想定する

''')
