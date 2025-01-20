# System Security and Authenticity Checker

This Python project is designed to check various aspects of a Windows system related to security, authenticity, and potential threats. It provides the following features:

- **Antivirus Status**: Checks whether antivirus protection (e.g., Windows Defender) is enabled.
- **PC Authenticity**: Verifies if the system is genuine and checks for any dual-boot configurations.
- **Suspicious Registry Keys**: Scans for suspicious registry entries that might indicate malware or unauthorized software.
- **Suspicious Drivers**: Looks for suspicious drivers, such as those that may allow direct memory access (DMA).
- **Anti-Cheat Services**: Checks if known anti-cheat services (e.g., EasyAntiCheat, BattlEye) are running.
- **Recent Threats**: Retrieves the list of recent threats detected by Windows Defender.

## Features

1. **Antivirus Status Check**: Uses PowerShell to check if antivirus protection is active.
2. **Dual-Boot and Authenticity Check**: Uses `bcdedit` to detect if the system is running multiple operating systems.
3. **Registry Key Scan**: Scans the registry for suspicious keys that might indicate the presence of unwanted programs.
4. **Driver Scan**: Scans the system for suspicious disk drivers.
5. **Anti-Cheat Services Check**: Verifies if services like EasyAntiCheat or BattlEye are running to prevent cheating in games.
6. **Recent Threats**: Retrieves a list of recent threats detected by Windows Defender, with a detailed report on actions taken.

## Prerequisites

- Python 3.x
- PowerShell (for executing system commands)
- `psutil` library (for managing system processes)
- `winreg` (for interacting with the Windows registry)

To install the required dependencies:

```bash
pip install psutil
```

## Usage

### 1. Check Antivirus Status

To check the status of Windows Defender or another antivirus, run the function `get_antivirus_status()`.

```python
status = get_antivirus_status()
print(status)
```

### 2. Check PC Authenticity

To verify if the system is genuine and check for dual-boot configurations, run the function `check_pc_authenticity()`.

```python
authenticity_status = check_pc_authenticity()
print(authenticity_status)
```

### 3. Check Suspicious Registry Keys

To check for suspicious registry keys under the `Run` key:

```python
suspicious_keys = check_suspicious_registry_keys()
print(suspicious_keys)
```

### 4. Check Suspicious Drivers

To check for suspicious disk drivers, such as those that support Direct Memory Access (DMA):

```python
suspicious_drivers = check_suspicious_drivers()
print(suspicious_drivers)
```

### 5. Check Running Anti-Cheat Services

To check if any known anti-cheat services (like EasyAntiCheat or BattlEye) are running:

```python
running_anti_cheat_services = check_running_anticheat()
print(running_anti_cheat_services)
```

### 6. Get Recent Threats

To retrieve the recent threats detected by Windows Defender:

```python
recent_threats = get_recent_threats()
print(recent_threats)
```

## Error Handling

The script includes basic error handling for the following scenarios:
- PowerShell command failures
- Missing permissions for accessing the registry or system resources
- Any unexpected errors during function execution

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
