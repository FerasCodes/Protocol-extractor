# Protocol-extractor

Protocol Extractor is a Python tool that analyzes PCAP files to extract and list unique network protocols using `tshark`.

## Features

- Traverse directories to find PCAP files
- Extract unique protocols from each file
- Save the list of protocols to an output file

## Requirements

- Python 3.6+
- Wireshark (`tshark`) 

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ferascodes/Protocol-extractor.git
   cd Protocol-extractor

  ```

2. Ensure tshark is installed and accessible. Download [Wireshark](https://www.wireshark.org/) from Wireshark's Official Site.

## Usage 

```sh
python pacp_protocol_parser.py -d <directory> -o <output_file> [-t <tshark_path>]
```

### Arguments

- `-d`, `--directory`: 
  - **Description**: Path to the directory containing PCAP files.
  - **Required**: Yes

- `-o`, `--output`: 
  - **Description**: Path to the output file for storing unique protocols.
  - **Required**: Yes

- `-t`, `--tshark`: 
  - **Description**: Path to the `tshark` executable.
  - **Required**: No
  - **Default**: `C:\Program Files\Wireshark\tshark.exe`

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Wireshark for providing [tshark](https://www.wireshark.org/) 
    
