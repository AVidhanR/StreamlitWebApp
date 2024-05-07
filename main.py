import streamlit as st

container = st.container()
container.title("AVidhanR")
container.write("A Simple Web App")
# method 1
btn = container.button("Contact me")
if btn:
    container.balloons()
# method 2
# if container.button("Press me"):
#    container.balloons()
