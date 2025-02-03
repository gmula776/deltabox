# DeltaBox

DeltaBox is a Python program designed to track power usage by applications on Windows devices. By monitoring CPU usage, DeltaBox helps users optimize energy consumption by identifying applications that consume the most power.

## Features

- Tracks CPU usage of running applications.
- Logs energy usage data to a CSV file.
- Helps optimize energy consumption on Windows devices.

## Requirements

- Python 3.6+
- `psutil` library

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python 3.6 or higher installed.
3. Install the necessary library by running:
   ```
   pip install psutil
   ```

## Usage

1. Run the `deltabox.py` script:
   ```
   python deltabox.py
   ```
2. The program will start tracking CPU usage of running applications.
3. To stop the program and log the data, press `Ctrl+C`.
4. The power usage data will be saved to `deltabox_log.csv`.

## Configuration

- You can change the logging interval by modifying the `log_interval` parameter when initializing the `DeltaBox` class. The default interval is 60 seconds.
- Change the output file name by setting the `log_file` parameter.

## License

This project is licensed under the MIT License.

## Disclaimer

DeltaBox tracks CPU usage as an approximation for energy consumption. Actual power usage may vary based on other factors such as hardware, application efficiency, and system state.