import streamlit as st
import manty_hall
import time

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Monty_open_door.svg/1200px-Monty_open_door.svg.png", width = 500)
st.title(":goat: Monty Hell Game Simulate")

number_input = st.number_input("Enter Number for simulate",
                min_value=1, max_value=1000000,
                value=100
                )
colm1, colm2 = st.columns(2)

with colm1:
    st.subheader("win percentage without switching")
    chart1 = st.line_chart(x=None, y= None)
    
with colm2:
    st.subheader("win percentage with switching")
    chart2 = st.line_chart(x=None, y=None)

win_with_swtich = 0
win_without_switch = 0

for i in range(number_input):
    win_with_swicthing, win_without_switching = manty_hall.simulate_game(1)

    win_with_swtich += win_with_swicthing
    win_without_switch += win_without_switching
    
    chart1.add_rows([win_without_switch / (i + 1)])
    chart2.add_rows([win_with_swtich / (i + 1)])
    time.sleep(.01)
    
#note me: به طور خودکار مقدار ایکس یک به یک میره جلو و وایی هم مقداری هست که بهش اختصاص دادیم

# chart2 = st.line_chart(x=None, y=None)
# chart2.add_rows([win_with_swtich / (i + 1)])