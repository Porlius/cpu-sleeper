import os
import time
import psutil
import shutil
import tempfile
from colorama import init, Fore, Style

# Initialize colorama (required for Windows to handle ANSI colors)
init()

def monitor_cpu_usage(threshold):
    """
    Monitors the CPU usage and reduces workload if usage exceeds a threshold.
    
    :param threshold: CPU usage threshold in percentage. If usage exceeds this value, 
                      the process will pause to reduce CPU load.
    """
    while True:
        # Get the current CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Print current CPU usage in light blue
        print(Fore.LIGHTBLUE_EX + f"Current CPU Usage: {cpu_usage}%")
        
        # If CPU usage exceeds the threshold, sleep for a longer period to reduce load
        if cpu_usage > threshold:
            print(Fore.LIGHTBLUE_EX + f"CPU usage exceeds {threshold}%. Reducing process speed...")
            time.sleep(2)  # Pause for 2 seconds to reduce CPU load
        else:
            time.sleep(1)  # Regular pause to prevent overloading the CPU

def clean_temp_files():
    """
    Cleans up temporary files from the system.
    It focuses on common directories where temporary files are stored.
    """
    temp_dir = tempfile.gettempdir()
    print(Fore.LIGHTBLUE_EX + f"Cleaning temporary files in {temp_dir}...")

    try:
        # Remove all files and directories inside the temp directory
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove directory
            except Exception as e:
                print(Fore.LIGHTBLUE_EX + f"Failed to delete {file_path}. Reason: {e}")

        print(Fore.LIGHTBLUE_EX + "Temporary files cleaned up successfully.")
    except Exception as e:
        print(Fore.LIGHTBLUE_EX + f"Failed to clean temporary files. Reason: {e}")

def print_menu():
    """
    Prints the interactive menu options for the user.
    """
    print(Fore.LIGHTBLUE_EX + "\n=== CPU Usage Optimizer Menu ===")
    print(Fore.LIGHTBLUE_EX + "1. Set CPU usage threshold")
    print(Fore.LIGHTBLUE_EX + "2. Monitor CPU usage")
    print(Fore.LIGHTBLUE_EX + "3. Clean temporary disk files")
    print(Fore.LIGHTBLUE_EX + "4. Exit")
    print(Fore.LIGHTBLUE_EX + "===============================")

def main():
    threshold = 30  # Default threshold value for CPU usage
    while True:
        print_menu()
        choice = input(Fore.LIGHTBLUE_EX + "Choose an option: ")
        
        if choice == '1':
            # Set CPU usage threshold
            try:
                new_threshold = int(input(Fore.LIGHTBLUE_EX + "Enter the new CPU usage threshold (percentage): "))
                if 0 < new_threshold <= 100:
                    threshold = new_threshold
                    print(Fore.LIGHTBLUE_EX + f"Threshold set to {threshold}%")
                else:
                    print(Fore.LIGHTBLUE_EX + "Please enter a value between 1 and 100.")
            except ValueError:
                print(Fore.LIGHTBLUE_EX + "Invalid input. Please enter a valid integer.")
        
        elif choice == '2':
            # Start monitoring CPU usage with the set threshold
            print(Fore.LIGHTBLUE_EX + f"Monitoring CPU usage with a {threshold}% threshold. Press Ctrl+C to stop.")
            try:
                monitor_cpu_usage(threshold)
            except KeyboardInterrupt:
                print(Fore.LIGHTBLUE_EX + "\nMonitoring stopped.")
        
        elif choice == '3':
            # Clean temporary disk files
            print(Fore.LIGHTBLUE_EX + "Cleaning temporary disk files...")
            clean_temp_files()
        
        elif choice == '4':
            # Exit the program
            print(Fore.LIGHTBLUE_EX + "Exiting the program...")
            break
        
        else:
            print(Fore.LIGHTBLUE_EX + "Invalid option. Please choose a valid menu option.")

if __name__ == "__main__":
    main()
