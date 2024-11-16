#!/usr/bin/env python3
from pwn import *

def run_simple_test():
    # Start the process using pwntools
    process_name = "./target"  # Path to your compiled binary
    proc = process(process_name)


    proc.recvuntil("Enter your Steps of the YMCA Song:".encode())
    # Send a large payload of "A"s to trigger buffer overflow
    payload = b"A" * 1000
    proc.sendline(payload)
    
    # Wait for the process to terminate and check the exit code
    proc.wait()

    # Check for segmentation fault (exit code -11)
    if proc.poll() == -11:
        print("Test passed: Segmentation fault (SIGSEGV) detected!")
    else:
        print(f"Test failed: Process exited with code {proc.poll()}")

    # Close the process
    proc.close()


    # Close the process
    proc.close()

if __name__ == "__main__":
    run_simple_test()


