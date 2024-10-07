
# Domain-Scraper 

<img width="787" alt="image" src="https://github.com/user-attachments/assets/5ea977b4-39fb-47ca-8d45-5ad0f17d76fb">
 <!-- Replace with the actual path to your screenshot -->

## Description

The **Domain-Scraper** is a Python script that extracts unique domain names from URLs contained in a specified text file and saves them to a new text file. This tool is user-friendly and efficient for gathering domain names from lists of URLs.

## Prerequisites

- **Python 3.x**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Git**: Make sure you have Git installed to clone the repository. You can download it from [git-scm.com](https://git-scm.com/).

## Getting Started

1. **Clone the Repository**:

   Run the following command to clone the repository:
   ```bash
   git clone https://github.com/md-durjoy/Domain-Scraper.git
   ```

2. **Navigate into the Cloned Directory**:
   ```bash
   cd domain-grabber
   ```

## Running the Script
  
1. **Prepare Your Input File**:
   Ensure the input text file containing URLs is ready and located in the same directory.

2. **Run the Script**:
   Use Python to execute the script with the following command:
   ```bash
   python domain-grabber.py
   ```

3. **Provide Input and Output File Names**:
   When prompted, enter the input text file name (must end with `.txt`) and the desired output file name (must also end with `.txt`):
   ```plaintext
   Enter the input text file name (must be a .txt file): your_input_file.txt
   Enter the output file name (must end with .txt): output_file.txt
   ```

### Example

If your input file is named `urls.txt` and you want the output file to be `domains.txt`, you would enter:
```plaintext
Enter the input text file name (must be a .txt file): urls.txt
Enter the output file name (must end with .txt): domains.txt
```

### Output

The output will display how many domains were extracted and saved to the specified output file:
```plaintext
Extracted domains and saved to 'output_file.txt'.
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
