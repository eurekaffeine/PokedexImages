#!/usr/bin/env python3
"""
PNG to WebP Converter for PokedexImages

This script converts all PNG files in the official-artwork directory to WebP format.
If a WebP file with the same filename already exists, it skips the conversion.
"""

import os
from pathlib import Path
from PIL import Image
import argparse


def convert_png_to_webp(source_dir, quality=85, lossless=False):
    """
    Convert PNG files to WebP format in the specified directory.
    
    Args:
        source_dir (str): Path to the directory containing PNG files
        quality (int): WebP quality (0-100, ignored if lossless=True)
        lossless (bool): Whether to use lossless compression
    """
    source_path = Path(source_dir)
    
    if not source_path.exists():
        print(f"Error: Directory '{source_dir}' does not exist.")
        return
    
    if not source_path.is_dir():
        print(f"Error: '{source_dir}' is not a directory.")
        return
    
    # Find all PNG files
    png_files = list(source_path.glob("*.png"))
    
    if not png_files:
        print(f"No PNG files found in '{source_dir}'.")
        return
    
    print(f"Found {len(png_files)} PNG files in '{source_dir}'")
    
    converted_count = 0
    skipped_count = 0
    error_count = 0
    
    for png_file in png_files:
        # Generate WebP filename
        webp_file = png_file.with_suffix('.webp')
        
        # Check if WebP file already exists
        if webp_file.exists():
            print(f"Skipping {png_file.name} - {webp_file.name} already exists")
            skipped_count += 1
            continue
        
        try:
            # Open and convert the image
            with Image.open(png_file) as img:
                # Convert RGBA to RGB if necessary for better compression
                # Keep RGBA if the image has transparency
                if img.mode == 'RGBA':
                    # Check if the image actually uses transparency
                    if img.getextrema()[3][0] < 255:  # Has transparency
                        save_kwargs = {'format': 'WEBP', 'lossless': lossless}
                        if not lossless:
                            save_kwargs['quality'] = quality
                    else:
                        # No transparency, convert to RGB for better compression
                        img = img.convert('RGB')
                        save_kwargs = {'format': 'WEBP', 'quality': quality}
                else:
                    save_kwargs = {'format': 'WEBP', 'quality': quality}
                
                # Save as WebP
                img.save(webp_file, **save_kwargs)
                
            print(f"Converted: {png_file.name} -> {webp_file.name}")
            converted_count += 1
            
        except Exception as e:
            print(f"Error converting {png_file.name}: {str(e)}")
            error_count += 1
    
    # Print summary
    print("\n" + "="*50)
    print("CONVERSION SUMMARY")
    print("="*50)
    print(f"Total PNG files found: {len(png_files)}")
    print(f"Successfully converted: {converted_count}")
    print(f"Skipped (WebP exists): {skipped_count}")
    print(f"Errors: {error_count}")
    print("="*50)


def main():
    parser = argparse.ArgumentParser(description='Convert PNG files to WebP format')
    parser.add_argument(
        '--directory', '-d',
        default='./official-artwork',
        help='Directory containing PNG files (default: ./official-artwork)'
    )
    parser.add_argument(
        '--quality', '-q',
        type=int,
        default=85,
        help='WebP quality (0-100, default: 85)'
    )
    parser.add_argument(
        '--lossless', '-l',
        action='store_true',
        help='Use lossless compression (ignores quality setting)'
    )
    
    args = parser.parse_args()
    
    # Validate quality
    if not 0 <= args.quality <= 100:
        print("Error: Quality must be between 0 and 100")
        return
    
    print("PNG to WebP Converter")
    print("="*30)
    print(f"Directory: {args.directory}")
    print(f"Quality: {'Lossless' if args.lossless else args.quality}")
    print("="*30)
    
    convert_png_to_webp(args.directory, args.quality, args.lossless)


if __name__ == "__main__":
    main()