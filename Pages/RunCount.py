import os

def get_run_count():
    count_file_path = "../TestCases/run_count.txt"

    # Check if the count file exists
    if os.path.exists(count_file_path):
        with open(count_file_path, "r") as file:
            count = int(file.read())
        return count
    else:
        # If the file doesn't exist, assume it's the first run
        return 0

def increment_and_save_count():
    count_file_path = "../TestCases/run_count.txt"

    # Get the current count
    count = get_run_count()

    # Increment the count
    count += 1

    # Save the updated count to the file
    with open(count_file_path, "w") as file:
        file.write(str(count))

# Example usage:
current_run_count = get_run_count()
print(f"This is run number {current_run_count + 1}")

# Perform your Selenium actions here

# Increment and save the run count after the program execution
increment_and_save_count()
