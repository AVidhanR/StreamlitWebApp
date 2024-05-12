## Sample `Streamlit` Project
- Create a new project in `Pycharm` (Recommended)
- Create a new file and name it as `main.py`
- Install the below packages in your project.
```bash
pip install streamlit
```
- Write the below code,
```py
import streamlit as st
import numpy as np

container = st.container()
container.header("About me")
# * Interesting [streamlit]
# container.markdown(
#         """
#         <style>
#             /* Define custom CSS styles */
#             .custom-text {
#                 font-size: 1.5rem; /* Adjust font size as needed */
#                 font-weight: bold; /* Make text bold */
#             }
#         </style>
#         <p class = "custom-text">Bio: </p>
#         """,
#         unsafe_allow_html = True
#         )
container.text(
    "Hello! I'm Vidhan, A Compute Science undergraduate. \nI love to learn new Stuff and upgrade myself"
)
container.markdown(
    """
    <a href="https://github.com/AVidhanR" style="font-size: 1rem; text-decoration: none; color: sky-blue;">Vist my github</a>
    """,
    unsafe_allow_html = True
)
message = st.chat_message("assistant")
message.write("Hello human")
prompt = st.chat_input("Enter something")
if prompt:
    st.write(f"User has entered something: {prompt}")
message.bar_chart(np.random.randn(30, 3))
btn = container.button("I'm Feeling lucky!")
if btn:
    st.balloons()

```
- Save the code in your file [`main.py`]()
```bash
streamlit run main.py
```
- Open the `localhost:8501` or by clicking it from the terminal
