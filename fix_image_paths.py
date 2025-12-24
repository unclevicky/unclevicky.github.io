#!/usr/bin/env python3
"""
Fix image paths in generated HTML files by replacing Windows backslashes with forward slashes.
"""

import os
import re

# Configuration
OUTPUT_DIR = 'output'


def fix_html_file(file_path):
    """Fix image paths in a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace backslashes in image URLs with forward slashes
        # This targets URLs like: https://example.com/photos\image.jpg
        fixed_content = re.sub(r'(https?://[^"\']+)\\([^"\'\\]+)', r'\1/\2', content)
        
        # Add .jpg extension to image URLs that don't have it
        # This targets URLs like: https://example.com/photos/image
        fixed_content = re.sub(r'(https?://[^"\']+/photos/[^"\'\\/]+?)([^."\']+)"', r'\1\2.jpg"', fixed_content)
        
        # Fix image paths with thumb suffixes
        # This targets URLs like: https://example.com/photos/imagea and https://example.com/photos/imagethumb
        fixed_content = re.sub(r'(https?://[^"\']+/photos/[^"\'\\/]+?)(a|t)\b', r'\1.\2.jpg', fixed_content)
        
        # Remove unwanted suffixes from image filenames in URLs
        # This targets URLs like: https://example.com/photos/imagea.jpg (remove 'a' suffix)
        # and https://example.com/photos/imagethumb.jpg (remove 't' suffix)
        fixed_content = re.sub(r'(https?://[^"\']+/photos/[^"\'\\/]+?)(a|t)\.jpg\b', r'\1.jpg', fixed_content)
        
        # Fix None captions
        fixed_content = fixed_content.replace('alt="None"', '')
        
        if fixed_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"Fixed: {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def fix_all_html_files():
    """Fix image paths in all HTML files in the output directory."""
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                fix_html_file(file_path)


if __name__ == '__main__':
    print("Fixing image paths in HTML files...")
    fix_all_html_files()
    print("Done!")
