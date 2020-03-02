

# Built-in Libraries
import configparser
import netifaces as ni
import numpy as np
import psutil
import urllib.request
import os
import time

from properties.machine import *
from properties.embedded import *

#add properties file for all hardcoded values
#cont. monitoring

class MachineInfo:
    @property
    def machine_ip(self):
        try:
            #con. stat. fr check
            try:
                ip = ni.ifaddresses(ethernet_interface)[ni.AF_INET][0]['addr']
                return ip

            except:
                ip = ni.ifaddresses(wifi_interface)[ni.AF_INET][0]['addr']
                return ip

        except:
            return "Not Connected"

    def machine_mac(self):
        try:
            x = ni.ifaddresses(ethernet_interface)[ni.AF_INET][0]['addr']
            return ni.ifaddresses(ethernet_interface)[ni.AF_LINK][0]['addr']

        except:
            MAC = ni.ifaddresses(wifi_interface)[ni.AF_LINK][0]['addr']
            return MAC

    def wifi_interface(self):
        lst = ni.interfaces()
        return (lst[2])

    def ethernet_interface(self):
        lst = ni.interfaces()
        return (lst[1])

    def internet_connection(self):
        try:
            urllib.request.urlopen(request_url)
            return True
        except:
            return False


    def memory_usage(self):
        x = (np.array(psutil.virtual_memory()) / 1000000000)
        used = available_memory - x[1]
        return '%.2f' % used

    def cpu_usage(self):
        return psutil.cpu_percent(interval= cpu_interval)


thismachine = MachineInfo()


