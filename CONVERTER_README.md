# PNG to WebP Converter

This script converts PNG files to WebP format in the `official-artwork` directory. It automatically skips files where a corresponding WebP file already exists.

## Requirements

- Python 3.6+
- Pillow (PIL)

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic usage (converts files in ./official-artwork with quality 85):
```bash
python convert_png_to_webp.py
```

### Custom directory:
```bash
python convert_png_to_webp.py --directory /path/to/your/png/files
```

### Custom quality (0-100):
```bash
python convert_png_to_webp.py --quality 90
```

### Lossless compression:
```bash
python convert_png_to_webp.py --lossless
```

### Full options:
```bash
python convert_png_to_webp.py --directory ./official-artwork --quality 85
```

## Features

- ✅ Automatically skips files where `${filename}.webp` already exists
- ✅ Preserves transparency for PNG files that use it
- ✅ Converts RGBA to RGB for better compression when transparency isn't needed
- ✅ Configurable quality settings
- ✅ Lossless compression option
- ✅ Detailed progress reporting
- ✅ Error handling and summary statistics

## Command Line Options

- `--directory, -d`: Directory containing PNG files (default: ./official-artwork)
- `--quality, -q`: WebP quality 0-100 (default: 85)
- `--lossless, -l`: Use lossless compression (ignores quality setting)

## Example Output

```
PNG to WebP Converter
==============================
Directory: ./official-artwork
Quality: 85
==============================
Found 1500 PNG files in './official-artwork'
Skipping 1.png - 1.webp already exists
Skipping 2.png - 2.webp already exists
Converted: 1026.png -> 1026.webp
Converted: 1027.png -> 1027.webp
...

==================================================
CONVERSION SUMMARY
==================================================
Total PNG files found: 1500
Successfully converted: 45
Skipped (WebP exists): 1455
Errors: 0
==================================================
```