import streamlit as st

def calculate_thevenins(vth,rth,r1):
    i1 = vth / (rth + r1)
    p1 = i1**2 * r1
    return i1,p1

st.title('Thevenins theorem')

tab1,tab2 = st.tabs(["compute","Explanation"])

with tab1:
    col1 , col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            vth = st.number_input("Vth (v)",value =1)
            rth = st.number_input("Rth (ohms)",value =1)
            r1 = st.number_input("RL (ohms)",value=1)

            compute = st.button("compute")


        with col2:
            with st.container(border=True):
                if compute:
                    i1,p1 = calculate_thevenins(vth,rth,r1)
                    st.write(f'I1 = {i1:.2f} A')
                    st.write(f'P1 = {p1:.2f} W')
            # vout = st.empty()
            # iout =


with tab2:
    st.write("This is explanation tab")