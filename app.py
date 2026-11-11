import streamlit as st
import psutil
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Smart Server Health Monitor", page_icon="🖥️", layout="wide")

st.title("Smart Server Health Monitoring System")
st.caption("A beginner-friendly DevOps project to monitor CPU, memory, disk, and server health.")

# Thresholds can be adjusted here.
CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISK_LIMIT = 85

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Refresh server metrics", type="primary"):
    st.rerun()

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")
boot_time = datetime.fromtimestamp(psutil.boot_time())
now = datetime.now()

cpu_value = round(cpu, 1)
memory_value = round(memory.percent, 1)
disk_value = round(disk.percent, 1)

st.subheader("Current server status")
c1, c2, c3 = st.columns(3)
c1.metric("CPU Usage", f"{cpu_value}%")
c2.metric("Memory Usage", f"{memory_value}%")
c3.metric("Disk Usage", f"{disk_value}%")

alerts = []
if cpu_value >= CPU_LIMIT:
    alerts.append(f"CPU usage is high ({cpu_value}%).")
if memory_value >= MEMORY_LIMIT:
    alerts.append(f"Memory usage is high ({memory_value}%).")
if disk_value >= DISK_LIMIT:
    alerts.append(f"Disk usage is high ({disk_value}%).")

if alerts:
    st.error("Potential server issue detected")
    for alert in alerts:
        st.write(f"- {alert}")
else:
    st.success("Server health looks good. No threshold alerts detected.")

st.subheader("Resource details")
d1, d2, d3 = st.columns(3)
d1.write(f"**Memory used:** {memory.used / (1024**3):.2f} GB")
d1.write(f"**Memory available:** {memory.available / (1024**3):.2f} GB")
d2.write(f"**Disk used:** {disk.used / (1024**3):.2f} GB")
d2.write(f"**Disk free:** {disk.free / (1024**3):.2f} GB")
d3.write(f"**CPU cores:** {psutil.cpu_count(logical=True)}")
d3.write(f"**Server started:** {boot_time.strftime('%d %b %Y, %I:%M %p')}")

st.session_state.history.append({
    "Time": now.strftime("%H:%M:%S"),
    "CPU": cpu_value,
    "Memory": memory_value,
    "Disk": disk_value
})
st.session_state.history = st.session_state.history[-30:]

st.subheader("Recent resource usage")
history_df = pd.DataFrame(st.session_state.history)
fig = go.Figure()
for column in ["CPU", "Memory", "Disk"]:
    fig.add_trace(go.Scatter(
        x=history_df["Time"], y=history_df[column],
        mode="lines+markers", name=column
    ))
fig.update_layout(
    xaxis_title="Time",
    yaxis_title="Usage (%)",
    yaxis=dict(range=[0, 100]),
    legend_title="Resource",
    height=380
)
st.plotly_chart(fig, use_container_width=True)

st.caption(
    f"Last checked: {now.strftime('%d %b %Y, %I:%M:%S %p')} | "
    f"Alert limits — CPU: {CPU_LIMIT}%, Memory: {MEMORY_LIMIT}%, Disk: {DISK_LIMIT}%"
)
