import streamlit as vAR_st
import math
import source.head as head


def cleartext():
        vAR_st.session_state["clr1"]=0
        vAR_st.session_state["clr2"]=0
def ratio():
    head.title()
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    with col1:
        vAR_st.markdown("### ")
        vAR_st.markdown("### Enter Input 1")
        vAR_st.markdown("## ")
        vAR_st.markdown("### Enter Input 2")
    with col2:
        x=vAR_st.number_input("",key="clr1")
        y=vAR_st.number_input("",key="clr2")
    x=int(x)
    y=int(y)
    with bc1:
        if vAR_st.button("Submit"):
            try:
                z=str(int(int(round(x/(math.gcd(x,y)),0))))+':'+str(int(round(y/(math.gcd(x,y)),0)))
            with col1:
                vAR_st.markdown("###")
                vAR_st.markdown("### Answer is")
            with col2:
                vAR_st.write('')
                vAR_st.subheader(z)
            except ZeroDivisionError:
                with col2:
                    vAR_st.subheader("Cannot Divide by zero")
    with bc2:
        vAR_st.button("Clear",on_click=cleartext)

