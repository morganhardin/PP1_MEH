#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:51:18 2024

@author: morganhardin
"""

import streamlit as st
#pip install streamlit-option-menu in terminal
from streamlit_option_menu import option_menu
from data import commands as commands

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
    
selected = option_menu(
    menu_title = "StatMapSecure",
    options = ["Home", "Scan Netstat", "Scan Nmap", "Track"],
    icons = ["house", "terminal", "terminal", "list-columns-reverse"],
    menu_icon = "shield-shaded",
    default_index = 3,
    orientation = "horizontal",
    styles = {
        "container": {"padding": "12.5px", 
                      "background-color": "#3498db",
                      "top": "50%"}, 
        "menu-title": {"color": "#fff", 
                       "font-size": "35px",
                       "font-weight": "bold",
                       "text-align": "center"},
        "icon": {"color": "#fff", "font-size": "25px"},
        "menu-icon": {"color": "#fff", "font-size": "35px"},
        "nav-link": {
            "color": "#fff",
            "font-size": "25px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#384046"},
    "nav-link-selected": {"background-color": "#1d6fa5"}}
)

if selected == "Home":
    st.switch_page("./Home.py")
elif selected == "Scan Netstat":
    st.switch_page("pages/ScanNetstat.py")
elif selected == "Scan Nmap":
    st.switch_page("pages/ScanNmap.py")
elif selected == "Track":
    st.header('Track', divider = True)
    ip, port = commands.track()
    col1, col2 = st.columns(2, gap = "small")
    with col1:
        with st.container(border = True):
            st.write("**IP Addresses Found**")
            st.write(ip)
    with col2:
        with st.container(border = True):
            st.write("**Port Information Found:**")
            st.write(port)