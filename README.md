# Internet Speed Test with Python

This Python script allows you to quickly test your internet download and upload speeds, as well as the ping (latency), using the `speedtest-cli` library.

## Features
- Measures **download speed** (in Mbps)
- Measures **upload speed** (in Mbps)
- Measures **ping/latency** (in milliseconds)
- Automatically selects the best server based on ping

## Requirements

- Python 3.x
- `speedtest-cli` Python package

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/internet-speed-test.git
    ```

2. Navigate to the project directory:

    ```bash
    cd internet-speed-test
    ```

3. Install the required `speedtest-cli` library:

    ```bash
    pip install speedtest-cli
    ```

## Usage

To run the script and test your internet speed, simply execute the following command:

```bash
python speedtest.py
