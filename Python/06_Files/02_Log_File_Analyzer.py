import os


def create_sample_log():
    """Creates a sample log file so you can test the program right away."""
    sample_data = """2026-09-04 08:15:22 [INFO] Application started successfully.
2026-09-04 08:20:10 [WARNING] Low memory warning detected.
2026-09-04 09:05:44 [ERROR] Failed to connect to database.
2026-09-04 09:12:00 [INFO] User 'alice' logged in.
2026-09-04 10:00:15 [ERROR] NullPointerException in payment module.
2026-09-04 10:30:00 [WARNING] High CPU usage detected.
"""
    if not os.path.exists("server.log"):
        with open("server.log", "w") as file:
            file.write(sample_data)
        print("Created a sample 'server.log' file for you!")


def analyze_logs():
    create_sample_log()

    info_count = 0
    warning_count = 0
    error_count = 0
    errors = []

    try:
        # Open the file in read mode ('r')
        with open("server.log", "r") as file:
            # Read the file line by line (great for large logs)
            for line in file:
                if "[INFO]" in line:
                    info_count += 1
                elif "[WARNING]" in line:
                    warning_count += 1
                elif "[ERROR]" in line:
                    error_count += 1
                    errors.append(line.strip())

        # Display the summary report
        print("\n" + "=" * 35)
        print("        LOG FILE ANALYSIS REPORT")
        print("=" * 35)
        print(f"Total INFO messages:    {info_count}")
        print(f"Total WARNING messages: {warning_count}")
        print(f"Total ERROR messages:   {error_count}")

        # Print out just the error lines if any were found
        if errors:
            print("\n--- Detailed Error Log ---")
            for err in errors:
                print(f"❌ {err}")

    except FileNotFoundError:
        print("Error: The log file could not be found.")


if __name__ == "__main__":
    analyze_logs()
