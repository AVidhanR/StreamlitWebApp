import streamlit as st

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
btn = container.button("I'm Feeling lucky!")
if btn:
    st.balloons()

