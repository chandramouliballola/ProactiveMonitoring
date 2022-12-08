# ProactiveMonitoring
Walmart Ascend Program
Proactive Monitoring Case Study
1. Server Uptime
2. Monitor CPU Usage

Prerequisites:
# Should have Windows System
# Python is installed in the Windows machine with Python Path is configured in System Variables.
# Should have Oracle VM Virtualbox application
# Install Ubuntu OS in the VM as 'MouliUbuntu' -- Do not mind the name of the VM

# Serverup_CpuUsage.py should be placed in C:\Program Files\Oracle\VirtualBox
# alertmanager.yml should be placed in Alert Manager Folder.
# prometheus.yml, rules.yml should be placed in Prometheus Folder.
# Windows_Exporter should be up and running.

Steps to Run:
1. Open Oracle VM Virtualbox and Start the MouliUbuntu VM.
2. Open terminal and run command 'cd C:\Program Files\Oracle\VirtualBox>' without single quotes.
3. Run command 'vboxmanage metrics collect MouliUbuntu CPU/Load/User:avg' without single quotes. This will start collecting the metric. Use ctrl+c to terminate the collection display.
4. Verify whether the metrics are capturing by using 'vboxmanage metrics query MouliUbuntu CPU/Load/User:avg' command.
5. use 'python Serverup_CpuUsage.py' command to start the python custom exporter server.

Verify Prometheus Graph for Server_Up Metric.
Verify Promethues Alerts if 5 alerts are showing.
Verify Alert manager if any of the alerts are fired (Happens only when the rules in 'rules.yml' file are met)
