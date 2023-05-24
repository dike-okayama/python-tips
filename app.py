import streamlit as st

st.title("Python tips")

st.header("1. transpose of a matrix")
st.code('''\
>>> mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> zip(*matrix[::-1])
[(7, 4, 1), (8, 5, 2), (9, 6, 3)]
''')
st.caption('...')

st.header("2. smoothing a list")
st.code('''\
>>> mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> sum(mat, start=[])
[1, 2, 3, 4, 5, 6, 7, 8, 9]
''')
st.caption('...')

st.header("3. unpack nested tuple")
st.code('''\
>>> a, b, (c, d) = (1, 2, (3, 4))
>>> a, b, c, d
>>> (1, 2, 3, 4)
''')

st.header("4. get first or last Nth elements")
st.code('''\
>>> first, second, *rest, last = range(5)
>>> first, second, rest, last
(0, 1, [2, 3], 4)
''')
st.caption('...')

st.header("5. f-strings for debugging")
st.code('''\
>>> var = 42
>>> f'{var = }'
'var = 42'
''')

st.header("6. create a dictionary from list")
st.code('''\
>>> kvlist = ['a', 1, 'b', 2, 'c', 3]
>>> dict(zip(*[iter(kvlist)] * 2)))
>>> {'a': 1, 'b': 2, 'c': 3}
''')
st.caption('''\
The * operator means copy the list, and unpack the copied list.
''')

st.header("7. Queue-structure with list")
st.code('''\
>>> def Queue():
...     _que = []
...     _it = iter(_que)
...     def enqueue(x):
...         _que.append(x)
...     def dequeue():
...         return next(_it)
...     return enqueue, dequeue
...
>>> enqueue, dequeue = Queue()
>>> enqueue(1)
>>> enqueue(2)
>>> dequeue()
1
>>> enqueue(3)
>>> dequeue()
2
>>> dequeue()
3
''')
