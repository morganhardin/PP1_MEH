#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:51:18 2024

@author: morganhardin
"""

import streamlit as st
#pip install streamlit-option-menu in terminal
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
    
selected = option_menu(
    menu_title = "StatMapSecure",
    options = ["Home", "Scan Netstat", "Scan Nmap", "Track"],
    icons = ["house", "terminal", "terminal", "list-columns-reverse"],
    menu_icon = "shield-shaded",
    default_index = 0,
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
    st.header("Welcome to StatMapSecure", divider = True)
    st.write("This software application will check for security vulnerabilities. **Run Netstat before Nmap and both scans before Tracking.**")
    
    col1, col2, col3 = st.columns(3, gap = "small")
    with col1:
        with st.container(border = True):
            st.write("**Netstat**")
            st.write("Netstat finds all the IP addresses connected to a target device. All the network connections are shown for every established connection on the target network.")
            button_style = """
                            <style>
                            .stButton > button {
                                color: #fff;
                                background: #3498db;
                            }
                            .stButton:hover > button:hover {
                                color: #fff;
                                background: #384046;
                                border-color: #384046
                            }
                            </style>
                            """
            st.markdown(button_style, unsafe_allow_html=True)
            button = st.button("Scan using Netstat", use_container_width = True)
            if button:
                selected = "Scan Netstat"
                st.switch_page("pages/ScanNetstat.py")
    with col2:
        with st.container(border = True):
            st.write("**Nmap**")
            st.write("Nmap returns all the ports, open or closed, and the port names for specific IP addresses. It uses the IP addresses found from Netstat and discovers hosts on a network.")
            button_style = """
                            <style>
                            .stButton > button {
                                color: #fff;
                                background: #3498db;
                            }
                            .stButton:hover > button:hover {
                                color: #fff;
                                background: #384046;
                                border-color: #384046
                            }
                            </style>
                            """
            st.markdown(button_style, unsafe_allow_html=True)
            button = st.button("Scan using Nmap", use_container_width = True)
            if button:
                selected = "Scan Nmap"
                st.switch_page("pages/ScanNmap.py")
    with col3:
        with st.container(border = True):
            st.write("**Track**")
            st.write("This section will return the information from every scan in one section from the text file. Every scan and the date of the scan is saved each time a command is executed.")
            button_style = """
                            <style>
                            .stButton > button {
                                color: #fff;
                                background: #3498db;
                            }
                            .stButton:hover > button:hover {
                                color: #fff;
                                background: #384046;
                                border-color: #384046
                            }
                            </style>
                            """
            st.markdown(button_style, unsafe_allow_html=True)
            button = st.button("Track Now", use_container_width = True)
            if button:
                selected = "Track"
                st.switch_page("pages/Track.py")
elif selected == "Scan Netstat":
    st.switch_page("pages/ScanNetstat.py")
elif selected == "Scan Nmap":
    st.switch_page("pages/ScanNmap.py")
elif selected == "Track":
    st.switch_page("pages/Track.py")
    
    
    
    
    
    
    
    