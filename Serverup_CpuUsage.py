import time
import os
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server


class CustomCollector(object):
    def __init__(self):
        pass
  
    def collect(self):
        g1 = GaugeMetricFamily("Server_Status", '1-ServerUp 0-ServerDown', labels=['instance'])
        g2 = GaugeMetricFamily("vm_cpu_usage", 'CPU Usage in percentage', labels=['instance'])
        try:
            server_up = os.popen("VBoxManage list runningvms").read()
            #print('Initiating Custom Exporter')
            if ("MouliUbuntu" in server_up):
                i = 1
                g1.add_metric(["Server_Status"], i)
                yield g1
            else:
                i = 0
                g1.add_metric(["Server_Status"], i)
                yield g1
                raise Exception
            try:
                vm_cpu_usage_text = os.popen("VBoxManage metrics query  MouliUbuntu CPU/Load/User:avg").read()
                #print('VM CPU Usage string ' +vm_cpu_usage_text)
                tempvm = vm_cpu_usage_text[-7:]
                tempvm1 = tempvm[0:5]
                #print(tempvm)
                #print(tempvm1)
                vm_cpu_usage_num = float(tempvm1)
                g2.add_metric(["vm_cpu_usage"], vm_cpu_usage_num)
                yield g2
            except:
                print('Error in reading CPU usage! Please check...')
                g2.add_metric(["vm_cpu_usage"], 0)
                yield g2
        except:
            print('Server is down! Please check...')
            g2.add_metric(["vm_cpu_usage"], 0)
            yield g2

if __name__ == '__main__':
    start_http_server(8011)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)
