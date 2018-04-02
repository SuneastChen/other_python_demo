# _*_ coding:utf-8 _*_
#!/usr/bin/python34

import psutil
print('------------------------查看cpu------------------------')
print(psutil.cpu_count())  #查看逻辑cpu    #--->4
print(psutil.cpu_count(logical=False))    #查看物理cpu   #--->2
#---->>>双核四线程
print(psutil.cpu_times()) #返回cup使用情况的对象
#scputimes(user=27814.43359375, system=11998.84375, idle=139652.046875(空闲的cpu), interrupt=226.88786602020264, dpc=544.7711284905672)
print(psutil.cpu_times().idle)     #直接查看空闲的cpu信息
print(psutil.cpu_times()[0])     #直接查看user的cpu信息

print('------------------------查看内存------------------------')
print(psutil.swap_memory())   #查看物理交换内存,在linux用free命令查看
#sswap(total=8472199168, used=4872294400, free=3599904768, percent=57.5, sin=0, sout=0)
memory=psutil.swap_memory()
print(memory.used/memory.total)  #查看内存已使用比例
#linux下查看指定的内存使用情况:
#free -m | grep 'Swap' | awk '{print $2}'

print(psutil.virtual_memory())   #查看虚拟内存,与鲁大师显示相同
#svmem(total=4236099584, available=1199579136, percent=71.7, used=3036520448, free=1199579136)

print('------------------------查看磁盘------------------------')
print(psutil.disk_partitions())    #查看挂载点,磁盘根目录,生成列表   linux下可用df -lh查看
#[sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='F:\\', mountpoint='F:\\', fstype='', opts='cdrom'), sdiskpart(device='G:\\', mountpoint='G:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='H:\\', mountpoint='H:\\', fstype='NTFS', opts='rw,fixed')]

print(psutil.disk_usage('/'))    #查看磁盘容量使用情况,'/'表示根目录
#sdiskusage(total=52428795904, used=45179371520, free=7249424384, percent=86.2)

print(psutil.disk_io_counters())  #查看读写的次数与字节数量
#sdiskio(read_count=475069, write_count=380521, read_bytes=11536753664, write_bytes=15663880192, read_time=16224233620, write_time=1409142660)

print('------------------------查看网络------------------------')
print(psutil.net_io_counters())   #查看网卡合并流量
#snetio(bytes_sent=116998650, bytes_recv=1652321951, packets_sent=1715103, packets_recv=2914801, errin=0, errout=0, dropin=0, dropout=0)

print(psutil.net_io_counters(pernic=True))   #分别查看网卡信息
#{'Teredo Tunneling Pseudo-Interface': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'VirtualBox Host-Only Network': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), '本地连接': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'isatap.{B6C62516-0237-4DCD-8E82-2E2CC6E8A999}': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'isatap.{0AC6F436-F93C-4830-AFEB-B07526BC5CFF}': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'isatap.{E0F70F62-B2F6-4C16-8489-DC2B0F9167DF}': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'Loopback Pseudo-Interface 1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'isatap.{31A3DD70-0062-492A-98B7-5FDB56984A62}': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), '无线网络连接 3': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), '无线网络连接 2': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), '无线网络连接': snetio(bytes_sent=117040792, bytes_recv=1652406301, packets_sent=1715287, packets_recv=2915422, errin=0, errout=0, dropin=0, dropout=0)}

print('------------------------查看用户信息------------------------')
print(psutil.users())   #查看用户信息
#[suser(name='cxd', terminal=None, host='0.0.0.0', started=1503620418.0)]

print(psutil.boot_time())  #查看开机时间,返回时间戳   linux下用可以用 uptime 命看
#1503620389.0

print('------------------------查看进程信息------------------------')
print(psutil.pids())    #查看所有进程号  linux 下用ps -aux
#[0, 4, 388, 576, 640, 656, 704, 736, 756, 764, 880, 940, 980, 416, 620, 432, 996, 1272, 1464, 1544, 1732, 1740, 1848, 1176, 1344, 1704, 1908, 1916, 2140, 2188, 2924, 1964, 1508, 1320, 1668, 1864, 3844, 3916, 4036, 1144, 2264, 3352, 2096, 3668, 4196, 4416, 4644, 2328, 5156, 5180, 5596, 5984, 2760, 8280, 14036, 15024, 14924, 22920, 12364, 23392, 22968, 26588, 28124, 27156, 29476, 27868, 31816, 32096, 32260, 14284, 29704, 18704, 5420, 32376, 2256, 20072]

# print(psutil.Process(29704))    #查看具体的pid信息
#---->> psutil.Process(pid=29704, name='SogouExplorer.exe')