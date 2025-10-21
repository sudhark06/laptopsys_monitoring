import streamlit as st
import psutil
import time

st.title("💻 System Performance Monitor")

placeholder = st.empty()

while True:
    with placeholder.container():
        st.metric("CPU Usage", f"{psutil.cpu_percent()}%")
        st.metric("Memory Usage", f"{psutil.virtual_memory().percent}%")
        st.metric("Disk Usage", f"{psutil.disk_usage('/').percent}%")
        st.metric("Network Sent (MB)", round(psutil.net_io_counters().bytes_sent / 1e6, 2))
        st.metric("Network Received (MB)", round(psutil.net_io_counters().bytes_recv / 1e6, 2))
    time.sleep(2)
