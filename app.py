import streamlit as vAR_st
from streamlit_option_menu import option_menu
from PIL import Image
import pyautogui
import source.area_perimeter as ap
import source.clear as cr
import source.fact as fact
import source.palindrome_ as pld
import source.prime as prime
import source.square as sc
from source.statistics import stat

vAR_st.set_page_config(layout='wide')
with open('style\style2.css') as vAR_f:
    vAR_st.markdown (f"<style>{vAR_f.read()}</style>",unsafe_allow_html=True)

if 'placeholder' not in vAR_st.session_state:
    vAR_st.session_state.placeholder = "select"

col1, col2, col3 = vAR_st.columns([1.5,5,2])
with col1:
    vAR_st.write("")
with col2:
    vAR_img = Image.open("image\Logo_final.png")
    vAR_st.image(vAR_img,width=500)
with col3:
    vAR_st.write("")

with vAR_st.sidebar:
    selected=vAR_st.selectbox("Menu",('Area & Perimeter','Factorial','Square and Cube','Statistics','Palindrome','Prime or not'))
    vAR_lib=vAR_st.selectbox("",("Libraries","Streamlit","Pillow"))
    if vAR_st.button("Clear/Reset"):
        pyautogui.hotkey("ctrl","F5")

if __name__=="__main__":
    try:
        if selected=="Area & Perimeter":
            ap.areaperimeter()
        if selected=="Factorial":
            fact.factorial()
        if selected=="Palindrome":
            pld.palindrome()
        if selected=="Prime or not":
            prime.primeornot()
        if selected=="Square and Cube":
            sc.squarecube()
        if selected=="Statistics":
            stat()
    except BaseException as error:
        vAR_st.error(error)
