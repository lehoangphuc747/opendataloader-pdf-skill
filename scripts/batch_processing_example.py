#!/usr/bin/env python3
"""
Batch Processing Example (from opendataloader-pdf official repo)

Demonstrates processing multiple PDFs in a single invocation to avoid
repeated Java JVM startup overhead. This is the recommended approach
for large-scale document pipelines.
"""

from __future__ import annotations
import json
import time
from pathlib import Path
import opendataloader_pdf

def batch_convert_list(pdf_paths: list[str], output_dir: str):
    """Method 1: Convert multiple PDFs in a single JVM invocation."""
    print(f"Batch converting {len(pdf_paths)} files...")
    opendataloader_pdf.convert(
        input_path=pdf_paths,
        output_dir=output_dir,
        format="json,markdown",
        quiet=True,
    )
    return sorted(Path(output_dir).glob("*.json"))

def batch_convert_directory(directory: str, output_dir: str):
    """Method 2: Convert all PDFs in a directory (recursive)."""
    print(f"Converting entire directory {directory}...")
    opendataloader_pdf.convert(
        input_path=directory, # Passes the folder path directly
        output_dir=output_dir,
        format="json,markdown",
        quiet=True,
    )
    return sorted(Path(output_dir).glob("*.json"))

if __name__ == "__main__":
    # Example usage
    # pdfs = ["file1.pdf", "file2.pdf"]
    # batch_convert_list(pdfs, "./output_list")
    # batch_convert_directory("./pdf_folder", "./output_dir")
    pass
