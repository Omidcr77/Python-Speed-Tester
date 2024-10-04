import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()

    print("Selecting the best server based on ping...")
    st.get_best_server()

    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    print(f"Download speed: {download_speed:.2f} Mbps")

    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload speed: {upload_speed:.2f} Mbps")

    print("Testing ping...")
    ping = st.results.ping
    print(f"Ping: {ping:.2f} ms")

if __name__ == "__main__":
    test_internet_speed()
