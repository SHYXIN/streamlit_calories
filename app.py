import streamlit as st
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open('model.pkl','rb'))


st.write("卡路里燃烧计算器应用程序")

gender = st.selectbox("选择性别",("男","女"))

if (gender == "男"):
    g = 0
else:
    g = 1

age = st.number_input("输入年龄: ")

height = st.number_input("输入身高: ")

weight = st.number_input("输入体重：")

duration = st.number_input("输入锻炼持续时长： ")

heartrate = st.number_input("输入心率: ")

bodytemp = st.number_input("输入体温：")

# df = pd.DataFrame(columns = ['Gender','Age','Height','Weight',
#                                                    'Duration','Heart_Rate',
#                                                    'Body_temp'],
#                                         data = np.array([g,age,height,weight,duration,heartrate,bodytemp]).reshape(1,7))
# st.dataframe(df)
feature_values = [g,age,height,weight,duration,heartrate,bodytemp]


prediction = model.predict(np.array(feature_values).reshape(1, -1))

if st.button("预测"):
    st.write("消耗的卡路里")
    st.success(prediction)
