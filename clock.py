from datetime import datetime
import time

def get_current_time_with_precise_parts():
    # Get the current time with nanosecond precision
    current_time_ns = time.time_ns()

    # Extract datetime components
    now = datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    # Calculate milliseconds, microseconds, and nanoseconds from `current_time_ns`
    milliseconds = (current_time_ns // 1_000_000) % 1_000
    microseconds = (current_time_ns // 1_000) % 1_000
    nanoseconds = current_time_ns % 1_000

    return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:03}:{microseconds:03}:{nanoseconds:03}"

def start_clock():

    try:
        while True:
            # Get the formatted current time
            current_time = get_current_time_with_precise_parts()

            # Print the current time with overwrite
            print(f"\r{current_time}", end="")
            time.sleep(0.01)  # Update every 10 milliseconds for a smooth display
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    start_clock()

