import psutil
import datetime
import platform
import re
import requests
class Computer:
    def __init__(self):
        # 基本信息
        self.user = psutil.users()[0][0]
        self.name = platform.node()
        self.os_version = platform.platform()
        self.cpu = platform.processor()
        self.cpu_sum = psutil.cpu_count(logical=False)
        self.startup = datetime.datetime.fromtimestamp(psutil.users()[0][3])
        self.runtime = datetime.datetime.now()-datetime.datetime.fromtimestamp(psutil.users()[0][3])

        # 内存信息
        self.cpu_percent = psutil.cpu_percent()
        # 内存消耗百分比
        self.memory_spend_percent = psutil.virtual_memory().percent
        # 内存消耗
        self.memory_spend_sum = round(psutil.virtual_memory().used / 1024 ** 2)
        # 内存总量
        self.memory_all_sum = round(psutil.virtual_memory().total / 1024 ** 2)
        # 内存空闲
        self.memory_free_sum = round(psutil.virtual_memory().free / 1024 ** 2)

        #硬盘信息
        self.disk_info = []
        for i in range(len(psutil.disk_partitions())):
            disk = psutil.disk_partitions()[i].device
            disk_space = round(psutil.disk_usage(disk).total/1024**3)
            disk_used = round(psutil.disk_usage(disk).used/1024**3)
            disk_used_percent = round(psutil.disk_usage(disk).percent)
            disk_free = round(psutil.disk_usage(disk).free/1024**3)
            self.disk_info.append({'disk_space':disk_space,'disk_used':disk_used,'disk_used_percent':disk_used_percent,'disk_free':disk_free})

        # 网络信息
        net_io = psutil.net_io_counters()
        self.ip = self.get_ip_info()[0]
        self.adress = self.get_ip_info()[1]
        self.send_flow = round(net_io.bytes_sent/1024**2)
        self.receive_flow = round(net_io.bytes_recv/1024**2)
        self.send_package = round(net_io.packets_sent/1024**1)
        self.receive_package = round(net_io.packets_recv/1024**1)

    def get_ip_info(self):
        res1 = requests.get('http://httpbin.org/ip')
        ip = re.findall('"origin": "(.*?)"', res1.text)[0]
        res2 = requests.get('https://www.hao7188.com/ip/{}.html'.format(ip))
        ip_dress_data = re.findall('<span>(.*?)</span>', res2.text)[2]
        return ip, ip_dress_data

