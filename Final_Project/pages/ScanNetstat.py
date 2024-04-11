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
    default_index = 1,
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
    st.header('Netstat', divider = True)
    st.write(commands.netstat())
elif selected == "Scan Nmap":
    st.switch_page("pages/ScanNmap.py")
elif selected == "Track":
    st.switch_page("pages/Track.py")