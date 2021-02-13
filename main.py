import streamlit as st
import numpy as np
import pandas as pd
# インストールするのはPillowだがインポートするパッケージの名前はPillowではなくPILなので注意
from PIL import Image 

st.title("Streamlit 入門")
"DataFrame"

df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[100,200,300,400]
})

# 動的
"動的なテーブル"
st.dataframe(df,width=500,height=300)

# 静的
"静的なテーブル"
st.table(df)

# マークダウン記法
"""
マークダウン記法
# 章
## 節
### 項

```python
import pandas as pd
import streamlit as st
import numpy as np
```
"""

# チャートを描く
"チャートを描く"
df = pd.DataFrame(
    np.random.rand(20,3), # 正規分布で乱数を生成する（行,列）
    columns=["a","b","c"]
)
"line_chart"
st.line_chart(df)
"area_char"
st.area_chart(df)
"bar_chart"
st.bar_chart(df)


# マップをプロットする
"マップをプロットする"
df = pd.DataFrame(
    np.random.rand(100,2)/[10,10] + [35.69,139.70],
    columns=["lat","lon"]
)
"map"
st.map(df)


# 画像を表示
"画像を表示する"
img = Image.open("image.jpg")
st.image(img, caption="sample image", use_column_width=True)


" "
"▼ここからインタラクティブパート"
"="*30

"やること一覧"
img2 = Image.open("screen_shot1.png")
st.image(img2, use_column_width=True)

# チェックボックス
"チェックボックスによるメディアの表示可否"
if st.checkbox("Show Image？"):
    st.image(img, caption="sample image", use_column_width=True)


# セレクトボックス
"セレクトボックスによる値の動的変更"
option = st.selectbox(
    "あなたの好きな数字を教えて下さい。",
    list(range(1,11))
)

"あなたの好きな数字は" , option, "です。"


# テキスト入力
"テキスト入力による値の動的な変更"
option2 = st.text_input("あなたの趣味を教えて下さい。")
"あなたの趣味は" , option2, "です。"


# スライダー
"スライダーによる値の動的変更"
condition = st.slider(
    "あなたの今の調子は？",
    0,100,50) # 最小、最大、初期値
"あなたの今のコンディション：", condition



" "
"▼ここからレイアウトパート"
"="*30

"やること一覧"
img3 = Image.open("screen_shot2.png")
st.image(img3, use_column_width=True)

"サイドバーの追加"
st.sidebar.write("▼ここはサイドバーだぞっ！")
side_option = st.sidebar.text_input("あなたの苦手な虫は？")
side_condition = st.sidebar.slider("あなたのモチベは？",0,100,50) 

"あなたの苦手な虫：", side_option
"あなたのモチベーション：", side_condition


"２カラムレイアウトにする"
left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムにImageを表示")
if button:
    right_column.image(img, caption="sample image", use_column_width=True)


"expanderの追加"
expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ内容1を書く")
expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ内容2を書く")
expander3 = st.beta_expander("問い合わせ3")
expander3.write("問い合わせ内容3を書く")


"""
# 以上！
[参照したYoutube](https://www.youtube.com/watch?v=zp-kAt1Ih5k&feature=youtu.be)
"""



