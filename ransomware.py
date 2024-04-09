import os
import sys
import time
import subprocess

def main():
    if os.name == 'posix':
        # Create child process
        process_id = os.fork()

        # Indication of fork() failure
        if process_id < 0:
            print("fork failed!")
            # Return failure in exit status
            sys.exit(1)

        # PARENT PROCESS. Need to kill it.
        if process_id > 0:
            print("process_id of child process", process_id)
            # return success in exit status
            sys.exit(0)

        #unmask the file mode
        os.umask(0)

        #set new session
        sid = os.setsid()

        if sid < 0:
            # Return failure
            sys.exit(1)

        # Change the current working directory to root.
        os.chdir("/")

        # Close stdin, stdout, and stderr
        sys.stdin.close()
        sys.stdout.close()
        sys.stderr.close()

    # Open a log file in write mode.
    with open("Log.txt", "w+") as fp:
        while True:
            # Don't block context switches, let the process sleep for some time
            time.sleep(1)
            fp.write("Logging info...\n")
            fp.flush()
            # Implement and call some function that does core work for this daemon.

if __name__ == "__main__":
    main()
