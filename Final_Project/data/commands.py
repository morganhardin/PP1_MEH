#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:51:18 2024

@author: morganhardin
"""

import streamlit as st
#pip install streamlit-option-menu in terminal
from streamlit_option_menu import option_menu
import subprocess
import os.path
import re
from datetime import datetime

path = '/Users/morganhardin/Documents/Spring/Programming/Final_Project/data'
log_netstat = 'log_netstat'
log_nmap = 'log_nmap'
track_netstat = 'track_netstat'
track_nmap = 'track_nmap'
log_ip = 'log_ip'
log_port = 'log_port'
netstat_path = os.path.join(path, log_netstat + '.txt')
nmap_path = os.path.join(path, log_nmap + '.txt')
ip_path = os.path.join(path, log_ip + '.txt')
port_path = os.path.join(path, log_port + '.txt')
track_netpath = os.path.join(path, track_netstat + '.txt')
track_nmappath = os.path.join(path, track_nmap + '.txt')

def netstat():
    f = open(netstat_path, 'w')
    cmd = ['netstat', '-a']
    subprocess.run(cmd, stdout = f)
    
    output = []
    lines = open(netstat_path, "r").readlines()
    for line in lines:
        if re.search(r"(\b\d{1,3}\.){3}(\d{1,3})\b(\.\w*){1}", line):
            output.append(re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line))
    
    final = []
    [final.append(x) for x in output if x not in final]

    f = open(ip_path, 'w')
    for i in final:
        for x in i:
            f.write(x+"\n")

    f = open(track_netpath, 'a')
    today = datetime.today()
    format = '%m-%d-%Y'
    today_date = today.strftime("Date: " + format + "\n")
    f.write(today_date)
    for i in final:
        for x in i:
            f.write(x+"\n")
    f.write('\n')
    
    f = open(ip_path, 'r')
    ip = ''
    for i in final:
        for x in i:
            ip += x + '  \n'
        
    return ip

def nmap():
    nmap = []
    lines = open(ip_path, "r").readlines()
    for line in lines:
        nmap.append(re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line))
        
    f = open(nmap_path, "w")
    for i in nmap:
        for x in i:
            cmd = ['nmap', x]
            subprocess.run(cmd, stdout = f)
    
    output = []
    lines = open(nmap_path, "r").readlines()
    for line in lines:
        if re.search(r"((\d+)\/(\w*)((\s)*(\w*(.)*)))", line):
            output.append(re.findall(r'((\d+)\/(\w*)((\s)*(\w*(.)*)))', line))
    
    final = []
    for i in output:
        final.append(i[0])
      
    file = open(port_path,'w')
    for i in final:
        file.write(i[0] + '\n')
        
    ports = []
    with open(port_path, "r") as file:
        lines = file.readlines()
        ports.append(lines)
    
    file = open(track_nmappath,'a')
    today = datetime.today()
    format = '%m-%d-%Y'
    today_date = today.strftime("Date: " + format + "\n")
    file.write(today_date)
    for i in ports:
        for x in i:
            file.write(x)
    file.write('\n')
    
    f = open(port_path, 'r')
    port = ''
    for i in final:
        port += i[0] + '  \n'   
            
    return port

def track():
    netstat = []
    with open(track_netpath, "r") as f:
        lines = f.readlines()
        netstat.append(lines) 

    nmap = []
    with open(track_nmappath, "r") as f:
        lines = f.readlines()
        nmap.append(lines)
        
    ip = ''
    for i in netstat:
        for x in i:
            x = str(x).replace('\n', '')
            ip += x + '  \n'
    
    port = ''
    for i in nmap:
        for x in i:
            x = str(x).replace('\n', '')
            port += x + '  \n'
        
    return ip, port

