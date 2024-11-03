import os
import subprocess
import argparse

def extract_protocols(pcap_file, tshark_path):
    """Extracts the list of protocols from a pcap file using tshark. Returns a set of protocols."""
    protocols = set()
    tshark_cmd = [tshark_path, '-r', pcap_file, '-T', 'fields', '-e', '_ws.col.Protocol']

    try:
        output = subprocess.check_output(tshark_cmd, stderr=subprocess.DEVNULL, universal_newlines=True)
        for line in output.splitlines():
            protocol = line.strip()
            if protocol:
                protocols.add(protocol)
    except subprocess.CalledProcessError as e:
        print(f"Error analyzing {pcap_file}: {e}")
    
    return protocols

def parse_pcaps(directory, output_file, tshark_path):
    """Traverses directories, parses PCAP files, and writes unique protocols to a file."""
    all_protocols = set()

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pcap'):
                pcap_file = os.path.join(root, file)
                print(f"Analyzing {pcap_file}...")
                pcap_protocols = extract_protocols(pcap_file, tshark_path)
                new_protocols = pcap_protocols - all_protocols
                if new_protocols:
                    print(f"New protocols found: {', '.join(new_protocols)}")
                all_protocols.update(pcap_protocols)

    with open(output_file, 'w') as f:
        for protocol in sorted(all_protocols):
            f.write(f"{protocol}\n")

    print(f"Protocols have been saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(prog='Protocol-extractor', description="Extract unique protocols from PCAP files.")
    parser.add_argument('-d', '--directory', required=True, help="Path to the main directory containing the PCAP files")
    parser.add_argument('-o', '--output', required=True, help="Path to the output file for storing unique protocols")
    parser.add_argument('-t', '--tshark', default='C:\\Program Files\\Wireshark\\tshark.exe', help="Path to tshark executable")
    args = parser.parse_args()

    parse_pcaps(args.directory, args.output, args.tshark)

if __name__ == "__main__":
    main()
