from src.collector.remoteok import fetch_jobs


def main():
    html = fetch_jobs()

    print(f"Downloaded {len(html)} bytes")


if __name__ == "__main__":
    main()