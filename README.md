# ProactiveMonitoring Case Study
# Walmart Ascend Program
# 1. Server Uptime
# 2. Monitor CPU Usage

Prerequisites:
1. Should have Windows System
2. Python is installed in the Windows machine with Python Path is configured in System Variables.
3. Should have Oracle VM Virtualbox application
4. Install Ubuntu OS in the VM as 'MouliUbuntu' -- Do not mind the name of the VM
5. Serverup_CpuUsage.py should be placed in C:\Program Files\Oracle\VirtualBox
6. alertmanager.yml should be placed in Alert Manager Folder.
7. prometheus.yml, rules.yml should be placed in Prometheus Folder.
8. Windows_Exporter should be up and running.

Steps to Run:
1. Open Oracle VM Virtualbox and Start the MouliUbuntu VM.
2. Open terminal and run command 'cd C:\Program Files\Oracle\VirtualBox>' without single quotes.
3. Run command 'vboxmanage metrics collect MouliUbuntu CPU/Load/User:avg' without single quotes. This will start collecting the metric. Use ctrl+c to terminate the collection display.
4. Verify whether the metrics are capturing by using 'vboxmanage metrics query MouliUbuntu CPU/Load/User:avg' command.
5. use 'python Serverup_CpuUsage.py' command to start the python custom exporter server.

Verify Prometheus Graph for Server_Up Metric.
Verify Promethues Alerts if 5 alerts are showing.
Verify Alert manager if any of the alerts are fired (Happens only when the rules in 'rules.yml' file are met)
