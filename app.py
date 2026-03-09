import streamlit as st

st.title("About Streamlit")
st.header("A simple section that'll explain:")
st.write("Interactive introduction to Streamlit components")

st.markdown("""
* What does it do?
* Who is the target user?
* What input does the app collect, and what output does it shows

""")

st.divider()

# me part

st.header("Profile")

col1, col2 = st.columns(2)
with col1:
    option = st.selectbox(
        'Click me for introductory information',
        ('Select --', 'Name', 'Age', 'Course', 'Section')
    )

    if st.checkbox("Here's a picture of baby yoda for luck!"):
        st.image("https://imageio.forbes.com/specials-images/imageserve/5f9c50b1e392338a52d670be/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds")

with col2:
    if option == 'Name':
        st.info("Hi! I'm Mark Vincent A. Bartolay")
    elif option == 'Age':
        st.info("I'm 19 years old")
    elif option == 'Course':
        st.info("I'm taking Bachelor of Science in Information Technology")
    elif option == 'Section':
        st.info("I'm currently in 2nd Year in ICS-01-401A")

st.divider()

# start

st.header("Streamlit Introduction")

tab1, tab2, tab3 = st.tabs([
    "What does it do?", 
    "Who is the target user?", 
    "Inputs & Outputs"
])
with tab1:
    st.info("This app is a simple introduction to Streamlit, a powerful framework for building interactive web applications in Python. It allows users to create and share data-driven applications with ease, making it an ideal tool for data scientists, analysts, and developers.")
    st.code("import streamlit as st\n\nst.title('Hello, Streamlit!')")
with tab2:
    st.info("The target user of this app is anyone interested in learning about Streamlit or building interactive web applications in Python. This includes data scientists, analysts, and developers who want to create engaging and informative data visualizations and dashboards.")
    st.caption("This tab explains who can benefit from Streamlit")
with tab3:
    st.success("The app collects user input through various widgets like selectboxes, sliders, and text inputs. The output is displayed in real-time using Streamlit's built-in components like markdown, tables, and charts.")

# conclusion

st.divider()

st.header("Conclusion")

st.success("Great! Now you have an idea of what Streamlit is and how it can be used to create interactive web applications. Rate your understanding of Streamlit on a scale of 1 to 10:")
rating = st.slider("Rate your understanding of Streamlit", 1, 10, 5)
st.write(f"Your rating: {rating}")
st.button("Submit")
st.balloons()

hours = st.number_input("How many hours did you study Streamlit today?", 0, 24)
st.info(f"You studied {hours} hours today")

learn = st.radio(
    "Did you learn something new about Streamlit today?",
    ("Yes", "No")
)

st.text_input("Share your experience with Streamlit")
st.info("Thanks for sharing!")


upload_image = st.file_uploader("Upload an image to share your Streamlit experience")
if upload_image:
    st.image(upload_image, width=150)