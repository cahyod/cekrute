import argparse
import requests
import subprocess
import platform

def get_public_ip():
    try:
        # Fetch the public IP using ipify API
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except Exception as e:
        return f"An error occurred: {e}"

def traceroute(host):
    try:
        # Determine the traceroute command based on the OS
        if platform.system().lower() == "windows":
            command = ['tracert', host]  # Windows uses tracert
        else:
            command = ['traceroute', host]  # Linux/macOS use traceroute

        # Run the command and capture output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            return f"An error occurred: {result.stderr.decode('utf-8')}"
        return result.stdout.decode('utf-8')
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Perform traceroute and show public IP")
    parser.add_argument('-t', '--target', type=str, required=True, help="Target host for traceroute")
    args = parser.parse_args()

    # Get public IP
    public_ip = get_public_ip()
    print(f"Your public IP address is: {public_ip}")

    # Perform traceroute
    target_host = args.target
    print(f"\nPerforming traceroute to {target_host}...\n")
    traceroute_result = traceroute(target_host)
    print(traceroute_result)

if __name__ == "__main__":
    main()

