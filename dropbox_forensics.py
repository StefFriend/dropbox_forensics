import requests
import logging
import hashlib
import os
from datetime import datetime

def create_timestamped_dir():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    directory = os.path.join(os.getcwd(), timestamp)
    os.makedirs(directory, exist_ok=True)
    return directory

def setup_logging(directory):
    log_file = os.path.join(directory, 'activity.log')
    logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode='w')

def change_link_format(url):
    if url.endswith('?dl=0'):
        return url[:-1] + '1'
    return url

def download_file(url, directory):
    try:
        local_filename = url.split('/')[-1].split('?')[0]
        if not local_filename.endswith('.zip'):
            local_filename += '.zip'
        local_filepath = os.path.join(directory, local_filename)
        
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(local_filepath, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192): 
                    file.write(chunk)
            return local_filepath
    except requests.RequestException as e:
        logging.error(f"Error downloading file: {e}")
        return None

def compute_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except IOError as e:
        logging.error(f"Error reading file for hashing: {e}")
        return None

def main():
    directory = create_timestamped_dir()
    setup_logging(directory)
    dropbox_link = input("Enter the Dropbox link: ")
    download_link = change_link_format(dropbox_link)

    downloaded_file = download_file(download_link, directory)
    if downloaded_file:
        file_hash = compute_hash(downloaded_file)
        logging.info(f"Downloaded file hash (SHA-256): {file_hash}")

if __name__ == "__main__":
    main()
