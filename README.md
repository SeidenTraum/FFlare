# FFlare

### Overview
This script encrypts and decrypts files using Fernet. <br>
This is not meant for production use, but rather as a simple tool for encrypting and decrypting files.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/seidentraum/fflare
   ```
2. Navigate to the project directory:
   ```bash
   cd fflare
   ```
3. Install the required dependencies:
   ```bash
   # Optionally create a virtual environment
   python3 -m venv venv
   source venv/bin/activate
   # Install the dependencies Install the dependencies
   pip install -r requirements.txt
   ```

### Usage
To run the script, use the following command:
```bash
python fflare -p String [-o Path] (-e | -d) <filepath>
```
Where:
- `-p` is the password for the encryption/decryption *
- `-o` is the output file path (Will use filepath.spx[.enc|.dec] if not specified)
- `-e` is the encryption flag *
- `-d` is the decryption flag *
- `<filepath>` is the path to the file to be encrypted or decrypted *