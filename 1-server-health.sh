#!/bin/bash
date;
echo "uptime: $(uptime)"
echo "Currently connected:"
w
echo "--------------------"
echo "Last logins:"
last -a |head -3
echo "--------------------"
echo "Disk and memory usage:"
df -h | xargs | awk '{print "Free/total disk: " $11 " / " $9}'
free -m | xargs | awk '{print "Free/total memory: " $17 " / " $8 " MB"}'
echo "--------------------"
start_log=$(head -1 /var/log/syslog |cut -c 1-12)
oom=$(grep -ci kill /var/log/syslog)
echo -n "OOM errors since $start_log :" $oom
echo ""
echo "--------------------"
echo "Utilization and most expensive processes:"
top -b |head -3
echo
top -b |head -10 |tail -4
echo "--------------------"
echo "Open TCP ports:"
nmap -iflist
echo "--------------------"
echo "Current connections:"
netstat -s
echo "--------------------"
echo "processes:"
ps auxf --width=200
echo "--------------------"
echo "vmstat:"
vmstat 1 5
