import requests
import logging
import hashlib

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='http_requests.log')

def change_link_format(url):
    if url.endswith('?dl=0'):
        return url[:-1] + '1'  # Replace dl=0 with dl=1
    return url

def download_file(url):
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            local_filename = url.split('/')[-1].split('?')[0]
            with open(local_filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192): 
                    file.write(chunk)
            return local_filename
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

# Example usage
dropbox_link = 'https://www.dropbox.com/s/example?dl=0'  # Replace with actual Dropbox link
download_link = change_link_format(dropbox_link)

downloaded_file = download_file(download_link)
if downloaded_file:
    file_hash = compute_hash(downloaded_file)
    logging.info(f"Downloaded file hash (SHA-256): {file_hash}")
