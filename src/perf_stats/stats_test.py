import psutil
import time
import os
# https://pypi.org/project/psutil/

# system wide info
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU usage: {cpu_usage}")

memory_usage = psutil.virtual_memory()
print(f"Memory Usage: {memory_usage.percent}%")
print(f"Memory Usage: {memory_usage.available}")

disk_usage = psutil.disk_usage('/')
print(f"Disk Usage: {disk_usage.percent}%")

addrs = psutil.net_if_addrs()
print(addrs.keys())
inf = 'Ethernet 2'
net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
net_in_1 = net_stat.bytes_recv
net_out_1 = net_stat.bytes_sent
time.sleep(1)
net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
net_in_2 = net_stat.bytes_recv
net_out_2 = net_stat.bytes_sent

net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 3)

print(f"Current net-usage:\nIN: {net_in} MB/s, OUT: {net_out} MB/s")

pid = os.getpid()
pp = psutil.Process(pid)
print(pp.cpu_percent(interval=2))
print(pp.memory_info())
# https://stackoverflow.com/questions/49357887/how-to-get-current-disk-io-and-network-io-into-percentage-using-python

