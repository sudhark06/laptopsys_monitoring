import psutil
import time
from datetime import datetime

def get_system_stats():
    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "net_sent": psutil.net_io_counters().bytes_sent,
        "net_recv": psutil.net_io_counters().bytes_recv
    }

def log_to_console(stats):
    print(f"[{stats['time']}] CPU: {stats['cpu_percent']}% | "
          f"Memory: {stats['memory_percent']}% | "
          f"Disk: {stats['disk_percent']}% | "
          f"Net Sent: {stats['net_sent']} | Net Recv: {stats['net_recv']}")

if __name__ == "__main__":
    print("Starting PC Performance Monitor...\nPress Ctrl+C to stop.")
    try:
        while True:
            stats = get_system_stats()
            log_to_console(stats)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
