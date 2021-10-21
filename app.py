import streamlit as st
import random

title = st.title("じゃんけんゲーム")
hands= ['グー','チョキ','パー','出さない']
janken = st.radio('何を出しますか？', options=hands )
switch = st.sidebar.selectbox("勝負しますか?", ("まだ", "勝負！"))

n = random.randint(0,2)
com = hands[n]

if 'count0' not in st.session_state:
  st.session_state.count0 = 0
if 'count1' not in st.session_state:
  st.session_state.count1 = 0
if 'count2' not in st.session_state:
  st.session_state.count2 = 0
if 'count3' not in st.session_state:
  st.session_state.count3 = 0

i = (hands.index(janken) - n + 3) % 3

if switch == '勝負！':
  if janken == '出さない':
    st.write("相手は" + com + "を出していたのに"+"あなたは勝負から逃げました")
    st.write("## YOU LOSE")
    st.session_state.count3 +=1
  else:
    st.write("あなたは" + janken + "を出しました!","相手は" + com + "を出しました!")
    if i == 0:
      st.write("## 引き分け")
      st.session_state.count0 +=1
    elif i == 2:
      st.write("## YOU WIN!")
      st.session_state.count2+=1
    else:
      st.write("## YOU LOSE")
      st.session_state.count1+=1

st.write("勝ち:"+ str(st.session_state.count2) + " 負け:"+ str(st.session_state.count1) + " あいこ:"+ str(st.session_state.count0))
if st.session_state.count3 > 0:
  st.write("### 逃げ:"+ str(st.session_state.count3))