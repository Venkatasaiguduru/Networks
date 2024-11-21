import streamlit as st

def cal_nortons(v,r1,r2):
    i_n = v/(r1+r2)
    return i_n


st.title("Nortons Theorem")

tab1,tab2 = st.tabs(["compute","Explanation"])

with tab1:
    col1,col2=st.columns(2)

    with col1:
        with st.container(border=True):
            v = st.number_input("V (v)",value =1)
            r1 = st.number_input("R1 (ohms)",value =1)
            r2 = st.number_input("R2 (ohms)",value=1)

            compute = st.button("compute")

        with col2:
            with st.container(border=True):
                if compute:
                    i_n = cal_nortons(v,r1,r2)
                    st.write(f'{i_n} A')

