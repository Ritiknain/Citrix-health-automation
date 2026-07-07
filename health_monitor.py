import os
import subprocess

def ping_vdas(vdas):
    results = {}
    for vda in vdas:
        result = subprocess.run(['ping', '-n', '1', vda], capture_output=True, text=True)
        results[vda] = "Online" if "Received" in result.stdout else "Unreachable"
    return results


def count_errors(filepath):
    error_count=0
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            for line in f:
                if 'ERROR' in line:
                    error_count+=1
        return error_count
    else:        
        print(f"File {filepath} not found.")
        return 0
        
def scan_logs(folder):
    error_dict={}
    for file in os.listdir(folder):
        if file.endswith(".log"):
            filepath=os.path.join(folder,file)
            count=count_errors(filepath)
            
            error_dict[file]=count
    return error_dict


def print_report(log_data,vdas):
    print("=== Citrix health check ===")

    print("\nPing Status of VDAs:")
    vda_results = ping_vdas(vdas)
    for vda, status in vda_results.items():
        print(f"{vda:15} — {status}")

    print("\n=== Log Error Report ===")
    for file, count in log_data.items():
        if count > 1:
            print(f"{file:15}   - {count} ERRORS")
        else:
            print(f"{file:15}   - {count} ERROR")
    worst = max(log_data, key=log_data.get)
    print(f"Worst file: {worst} with {log_data[worst]} errors")

vdas = ["VDA01", "VDA02", "google.com", "VDA03"]

print_report(scan_logs("logs"), vdas)