import os
import psutil
import datetime
import subprocess
import winreg

def get_antivirus_status():
    """Check if antivirus is turned off (Windows Defender example)."""
    try:
        # Use a properly formatted PowerShell command
        cmd = [
            "powershell",
            "-Command",
            "Get-MpComputerStatus | Format-Table AMServiceEnabled, AntivirusEnabled -AutoSize"
        ]
        status = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL)
        return status.strip()
    except subprocess.CalledProcessError as e:
        return f"Error checking antivirus status: {e}"
    except Exception as ex:
        return f"An unexpected error occurred: {ex}"

def check_pc_authenticity():
    """Check if the PC is genuine and identify dual-boot configurations."""
    try:
        # Check for boot entries using bcdedit
        output = subprocess.check_output(["bcdedit"], text=True, stderr=subprocess.DEVNULL)
        dual_os = "Windows Boot Manager" in output and output.count("Windows Boot Loader") > 1
        return f"Genuine system detected. Dual OS: {'Yes' if dual_os else 'No'}"
    except subprocess.CalledProcessError as e:
        return f"Error checking PC authenticity: {e}"
    except Exception as ex:
        return f"An unexpected error occurred: {ex}"

def check_suspicious_registry_keys():
    """Check for suspicious registry keys."""
    suspicious_keys = []
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run") as key:
            i = 0
            while True:
                try:
                    value = winreg.EnumValue(key, i)
                    suspicious_keys.append(value)
                    i += 1
                except OSError:
                    break
        return suspicious_keys
    except Exception as ex:
        return f"Error checking registry keys: {ex}"

def check_suspicious_drivers():
    """Check for suspicious drivers."""
    suspicious_drivers = []
    try:
        drivers = psutil.disk_partitions()
        for driver in drivers:
            if "DMA" in driver.opts.upper():
                suspicious_drivers.append(driver.device)
        return suspicious_drivers
    except Exception as ex:
        return f"Error checking drivers: {ex}"

def check_running_anticheat():
    """Check if anti-cheat services (EAC, BattlEye) are running."""
    anticheat_services = ["EasyAntiCheat", "BattlEye"]
    running_services = []
    try:
        for process in psutil.process_iter(['name']):
            if any(anticheat in process.info['name'] for anticheat in anticheat_services):
                running_services.append(process.info['name'])
        return running_services
    except Exception as ex:
        return f"Error checking anti-cheat: {ex}"

def get_recent_threats():
    """Retrieve the recent threats list from Windows Defender."""
    try:
        cmd = [
            "powershell",
            "-Command",
            "Get-MpThreat | Format-Table -AutoSize"
        ]
        threats = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL)
        return threats.strip()
    except subprocess.CalledProcessError as e:
        return f"Error retrieving threats: {e}"
    except Exception as ex:
        return f"An unexpected error occurred: {ex}"

def display_menu():
    """Display a menu to navigate the tool's features."""
    menu_options = {
        1: ("Check Antivirus Status", get_antivirus_status),
        2: ("Check PC Authenticity", check_pc_authenticity),
        3: ("Check Suspicious Registry Keys", check_suspicious_registry_keys),
        4: ("Check Suspicious Drivers", check_suspicious_drivers),
        5: ("Check Running Anti-Cheat", check_running_anticheat),
        6: ("Get Recent Threats", get_recent_threats),
        7: ("Exit", None)
    }

    while True:
        print("\n=== PC Monitoring Tool ===")
        for key, (description, _) in menu_options.items():
            print(f"{key}. {description}")
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 7:
                print("Exiting tool. Goodbye!")
                break
            elif choice in menu_options:
                action = menu_options[choice][1]
                if action:
                    result = action()
                    print(f"\n{result}\n")
                else:
                    print("Invalid option!")
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    display_menu()
