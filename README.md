# Dropbox Forensics Downloader

This Python script is designed to download contents from a public Dropbox link. It supports downloading either individual files or entire folders in ZIP format. For folders, the script modifies the link to download them as ZIP files. It logs all HTTP requests and computes the SHA-256 hash of the downloaded file.

## Features

- Downloads files or folders from a public Dropbox link.
- Automatically changes folder links from `?dl=0` to `?dl=1` for direct download as ZIP.
- Logs all HTTP requests and responses.
- Computes and logs the SHA-256 hash of the downloaded file.
- Creates a new directory for each execution, named with a timestamp.
- Supports both direct download links and links for viewing in the browser.

## Usage

1. Clone the repository.
2. Install required packages: `pip install -r requirements.txt`.
3. Run the script: `python dropbox_downloader.py`.
4. Enter the Dropbox link when prompted.

## Requirements

- Python 3
- Packages listed in `requirements.txt`.

## Contributing

Feel free to fork the project and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
