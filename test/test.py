#-------
import streamlit as st
import time
import random

# ایجاد یک نمودار خطی خالی
chart = st.line_chart(x=None, y=None)

# اضافه کردن داده به نمودار
for i in range(10):
    # تولید یک عدد تصادفی بین 0 و 100
    new_value = random.randint(0, 100)
    
    # اضافه کردن عدد جدید به نمودار
    chart.add_rows([new_value])
    
    # مکث کوتاه برای دیدن تغییرات
    time.sleep(0.5)
    
#This test code was written by clude.ai
#-------