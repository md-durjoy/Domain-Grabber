import os
import re

print("""
██████   ██████  ███    ███  █████  ██ ███    ██        ██████  ██████   █████  ██████  ██████  ███████ ██████  
██   ██ ██    ██ ████  ████ ██   ██ ██ ████   ██       ██       ██   ██ ██   ██ ██   ██ ██   ██ ██      ██   ██ 
██   ██ ██    ██ ██ ████ ██ ███████ ██ ██ ██  ██ █████ ██   ███ ██████  ███████ ██████  ██████  █████   ██████  
██   ██ ██    ██ ██  ██  ██ ██   ██ ██ ██  ██ ██       ██    ██ ██   ██ ██   ██ ██   ██ ██   ██ ██      ██   ██ 
██████   ██████  ██      ██ ██   ██ ██ ██   ████        ██████  ██   ██ ██   ██ ██████  ██████  ███████ ██   ██                                                                                                                                                                                                                                                                                                                                                                               
TOOL: Domain Extractor
""")

input_file = input("Enter the input text file name (must be a .txt file): ")
output_file = input("Enter the output file name (must end with .txt): ")

# Check if the input file exists and has the correct extension
if not os.path.isfile(input_file):
    print(f"Invalid input file! '{input_file}' does not exist.")
    exit()

if not input_file.endswith('.txt'):
    print("Invalid input file! Please provide a valid .txt file.")
    exit()

if not output_file.endswith('.txt'):
    print("Output file must end with .txt!")
    exit()

domains = []
with open(input_file, 'r') as file:
    for line in file:
        # Update regex to match only domain names
        found_domains = re.findall(r'([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', line)
        for domain in found_domains:
            if domain not in domains:
                domains.append(domain)

with open(output_file, 'w') as file:
    for domain in domains:
        file.write(domain + '\n')

print(f"Extracted {len(domains)} domains and saved to '{output_file}'.")
