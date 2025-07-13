"""
🧵 Python Multithreading Practice
This script demonstrates core concepts of Python's threading module, including
parallel execution, race conditions, thread safety, and performance comparison.
"""

import threading
import time
import requests

# 1. ✅ Create two threads that run concurrently
def task1():
    print("Task 1 is running...")

def task2():
    print("Task 2 is running...")

# 2. ✅ Use threading to download files in parallel
def download_file(url):
    response = requests.get(url)
    print(f"Downloaded {len(response.content)} bytes from {url}")

# 3. ✅ Simulate a race condition
counter = 0

def race_condition():
    global counter
    for _ in range(100000):
        temp = counter
        temp += 1
        counter = temp

# 4. ✅ Use Lock to handle race condition
lock = threading.Lock()
safe_counter = 0

def thread_safe_increment():
    global safe_counter
    for _ in range(100000):
        with lock:
            temp = safe_counter
            temp += 1
            safe_counter = temp

# 5. ✅ Thread that counts numbers and prints
def count_numbers(name):
    for i in range(5):
        print(f"{name} counting: {i}")
        time.sleep(0.5)

# 6. ✅ Create a multi-threaded counter
def multi_threaded_counter():
    threads = []
    for i in range(3):
        thread = threading.Thread(target=count_numbers, args=(f"Thread-{i+1}",))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# 7. ✅ Demonstrate Thread.join() usage
def show_join():
    def simple_task():
        print("Starting task...")
        time.sleep(1)
        print("Task completed.")

    thread = threading.Thread(target=simple_task)
    thread.start()
    thread.join()  # Wait until thread finishes
    print("Main thread resumes after join.")

# 8. ✅ Use daemon threads
def background_logger():
    while True:
        print("[Daemon] Logging...")
        time.sleep(1)

# 9. ✅ Time how long multi-threaded vs. normal code takes
def count_slow():
    for _ in range(5):
        time.sleep(1)

def performance_compare():
    start = time.time()
    count_slow()
    count_slow()
    print("⏳ Sequential Time:", time.time() - start)

    start = time.time()
    t1 = threading.Thread(target=count_slow)
    t2 = threading.Thread(target=count_slow)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("⚡ Parallel Time:", time.time() - start)

# 10. ✅ Thread-safe increment of shared variable using Lock
thread_safe_value = 0

def safe_increment():
    global thread_safe_value
    for _ in range(100000):
        with lock:
            thread_safe_value += 1

def run_safe_threads():
    t1 = threading.Thread(target=safe_increment)
    t2 = threading.Thread(target=safe_increment)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("✅ Thread-safe value:", thread_safe_value)

# === Run All Tasks ===
if __name__ == "__main__":
    print("\n1. Concurrent Threads:")
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("\n2. Parallel File Download:")
    urls = ["https://httpbin.org/image/png", "https://httpbin.org/image/jpeg"]
    for url in urls:
        threading.Thread(target=download_file, args=(url,)).start()

    print("\n3. Race Condition Example:")
    threads = [threading.Thread(target=race_condition) for _ in range(2)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print("❌ Race Condition Counter:", counter)

    print("\n4. Race Condition Fixed with Lock:")
    threads = [threading.Thread(target=thread_safe_increment) for _ in range(2)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print("✅ Safe Counter with Lock:", safe_counter)

    print("\n5. Counting Thread:")
    count_thread = threading.Thread(target=count_numbers, args=("Counter",))
    count_thread.start()
    count_thread.join()

    print("\n6. Multi-threaded Counter:")
    multi_threaded_counter()

    print("\n7. Thread Join Demo:")
    show_join()

    print("\n8. Daemon Thread (runs in background):")
    daemon = threading.Thread(target=background_logger, daemon=True)
    daemon.start()
    time.sleep(3)  # Let daemon run briefly

    print("\n9. Performance Comparison:")
    performance_compare()

    print("\n10. Thread-safe Increment:")
    run_safe_threads()
