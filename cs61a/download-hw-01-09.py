import requests
import os


def download_labs(start, end, target_dir):
    # turns ~/ into /
    full_path = os.path.expanduser(target_dir)

    # ensure the target directory exists
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    base_url = "https://cs61a.org/hw/hw{:02d}/hw{:02d}.zip"

    for i in range(start, end + 1):
        lab_name = f"hw{i:02d}"
        url = base_url.format(i, i)
        file_path = os.path.join("hw", f"{lab_name}.zip")

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
    # Download hw 01 through 09
    my_project_path = "~/project/cs-study/cs61a/hw/"
    download_labs(1, 9, my_project_path)
