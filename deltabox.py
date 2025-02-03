import psutil
import time
from collections import defaultdict
import csv

class DeltaBox:
    def __init__(self, log_interval=60, log_file='deltabox_log.csv'):
        self.log_interval = log_interval
        self.log_file = log_file
        self.process_energy_usage = defaultdict(float)

    def get_power_usage(self):
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                with proc.oneshot():
                    pid = proc.info['pid']
                    name = proc.info['name']
                    cpu_percent = proc.info['cpu_percent']
                    self.process_energy_usage[name] += cpu_percent
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def log_usage(self):
        with open(self.log_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Application', 'Energy Usage (%)'])
            for app, usage in self.process_energy_usage.items():
                writer.writerow([app, usage])

    def run(self):
        try:
            while True:
                self.get_power_usage()
                time.sleep(self.log_interval)
        except KeyboardInterrupt:
            self.log_usage()
            print(f"Power usage logged to {self.log_file}")

if __name__ == '__main__':
    deltabox = DeltaBox()
    deltabox.run()