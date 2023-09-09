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
cpu = psutil.cpu_times_percent(interval=0.4, percpu=False)
print(cpu)

pcpu = pp.cpu_times()
print(pcpu)
print(pcpu[0] + pcpu[1])

pmem = pp.memory_full_info()
print(pmem)
print(pmem.uss)

# https://dzone.com/articles/using-the-psutil-module-for-system-monitoring-bonu
# http://www.pointborn.com/article/2019/1/17/379.html
# https://stackoverflow.com/questions/49357887/how-to-get-current-disk-io-and-network-io-into-percentage-using-python
# https://github.com/jeetsukumaran/Syrupy
# https://learnk8s.io/setting-cpu-memory-limits-requests
# https://www.baeldung.com/linux/process-periodic-cpu-usage
# https://github.com/zhuyifei1999/guppy3
# https://pypi.org/project/memory-profiler/
# https://unix.stackexchange.com/questions/554/how-to-monitor-cpu-memory-usage-of-a-single-process
# https://opensource.com/article/18/7/fun-perf-and-python
# https://devpress.csdn.net/python/62f4dc607e6682346618902c.html
# https://geekflare.com/process-cpu-memory-monitoring/
# https://blog.px.dev/cpu-profiling-2/
# https://github.com/nylas/nylas-perftools
# https://www.nylas.com/blog/performance/
