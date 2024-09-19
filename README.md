# cekrute
Check your ip public and route to the target

Here’s how you can write a Python script that performs a **traceroute** and also fetches your **public IP address**:

### 1. **Fetch Public IP Address**: 
You can use the `requests` library to get your public IP address from an external service like `ipify`.

### 2. **Perform Traceroute**:
To perform traceroute, Python does not have a built-in function, but you can use the `scapy` library or the `subprocess` module to call system commands.

### Explanation:
1. **Get Public IP**: The `get_public_ip()` function uses `requests` to get your public IP from the `ipify` service.
2. **Traceroute**: The `traceroute()` function calls the system’s traceroute command using the `subprocess` module. It works on Linux and macOS. On Windows, you can replace `traceroute` with `tracert`.

### Instructions:
### Install required libraries:
To use this script, make sure you have installed the necessary libraries:
```bash
pip install requests
```
**For Linux/macOS**:
   - Install `traceroute` using your package manager if it's not already installed:
     ```bash
     sudo apt-get install traceroute   # Debian/Ubuntu
     sudo yum install traceroute       # CentOS/Fedora
     brew install traceroute           # macOS (Homebrew)
     ```

**For Windows**:
   - You don't need to install anything, as `tracert` is included by default.

### Run the script:
```bash
python3 cekroute.py -t www.cahyo.web.id
```
