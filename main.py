import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Display Image')
# 画像を表示するための処理
# checkboxにcheckが入っていれば画像を表示、それ以外は非表示。インデントを忘れないようにする
if st.checkbox('Show Image'):
  img = Image.open('sample.png')
  st.image(img,caption='CJM',use_column_width=True)

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  latest_iteration.text(f'iteration{i+1}')
  bar.progress(i + 1)
  # カウントを0.1秒ずつ遅らせる
  time.sleep(0.1)

# option = st.selectbox(
#   'あなたの好きな数字を教えてください',
#   list(range(1,11))
# )
# 'あなたの好きな数字は',option,'です'

# text = st.text_input('あなたの趣味はなんですか?')
# 'あなたの趣味は',text,'です'
# condition = st.slider('貴方の今の調子は？',0,100,50)
# '貴方の今の調子は:',condition

# サイドバーにしたい時はsidebarを追加する
# text = st.sidebar.text_input('あなたの趣味はなんですか?')
# condition = st.sidebar.slider('あなたの今の調子はどうですか?')
# 'あなたの趣味は',text,'です'
# 'あなたの今の調子は',condition,'です'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if(button):
  right_column.write('右カラムですがな')

# 簡単にQ&Aが作成可能
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')


# df = pd.DataFrame({
#   '1列目' : [1, 2, 3, 4],
#   '2列目' : [10, 20, 30, 40],
# })

# st.write(df)こちらは縦と横の引数を選択できない
# st.dataframe(df.style.highlight_max(axis=0),width=500,height=500)
# st.table(df.style.highlight_max(axis=0))
# dataframeは動的なテーブルが作成可能（ソート）
# tableは静的なテーブルが作成可能

# h1 h2 h3のようなもの

# """
# # 章
# ## 節
# ### 項


# ```python
# impoort streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# df = pd.DataFrame(
#   np.random.rand(20,3),
#   columns=['a','b','c']
# )
# 折れ線グラフ
# st.line_chart(df)
# st.area_chart(df)
# 棒グラフ
# st.bar_chart(df)

df = pd.DataFrame(
  np.random.rand(100,2)/[50,50] + [35.69,139.70],
  columns=['lat','lon']
)
# mapの出力
# st.map(df)