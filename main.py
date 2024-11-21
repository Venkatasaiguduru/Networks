import streamlit as st

def another_page():
    st.write("This is another page")

pages = {
    "Theorems":[
        st.Page("thevenins.py",title="Thevenin's theorem"),
        st.Page("nortons.py",title="Norton's theorem"),
    ],
    "circuits":[
        st.Page(another_page,title="another page"),
    ],
}

pg = st.navigation(pages)
pg.run()