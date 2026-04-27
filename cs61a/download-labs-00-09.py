import requests
import os


def download_labs(start, end):
    base_url = "https://cs61a.org/lab/lab{:02d}/lab{:02d}.zip"

    for i in range(start, end + 1):
        lab_name = f"lab{i:02d}"
        url = base_url.format(i, i)
        file_path = os.path.join("labs", f"{lab_name}.zip")

        print(f"Downloading {lab_name} from {url}...")

        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(file_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Successfully saved to {file_path}")
            else:
                print(
                    f"Failed to download {lab_name} (Status code: {response.status_code})"
                )
        except Exception as e:
            print(f"An error occurred while downloading {lab_name}: {e}")


if __name__ == "__main__":
    # Download labs 00 through 09
    download_labs(0, 9)
