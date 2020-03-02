
from  MachineInfo import *

if __name__=='__main__':
    print("Machine IP:", thismachine.machine_ip)
    print("Machine MAC:",thismachine.machine_mac())
    print("Wifi Interface:",thismachine.wifi_interface())
    print("Ethernet Interface:",thismachine.ethernet_interface())
    #print("Internet Status: Connected"if thismachine.internet_connection() else "Internet Status: Not Connected")
    print("Internet Status: Connected" if thismachine.internet_connection() else "Internet Status: Not Connected")
    print("Memory Used:",thismachine.memory_usage(),"GB")
    print("CPU Usage:",thismachine.cpu_usage(),"%")
