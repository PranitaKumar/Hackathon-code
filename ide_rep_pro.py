def identify_repeated_processes():
    # Get a list of running processes
    running_processes = [proc.name() for proc in psutil.process_iter()]

    # Count occurrences of each process
    process_count = {}
    for process in running_processes:
        process_count[process] = process_count.get(process, 0) + 1

    # Filter processes with multiple instances
    repeated_processes = {process: count for process, count in process_count.items() if count > 1}

    # Print repeated processes
    if repeated_processes:
        print("Repeated Processes:")
        for process, count in repeated_processes.items():
            print(f"{process}: {count} instances")
    else:
        print("No repeated processes found.")

if __name__ == "__main__":
    identify_repeated_processes()
