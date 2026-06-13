---
name: opendataloader-pdf
description: PDF parser and extractor. Use this skill when the user wants to extract text, markdown, or JSON from PDF files, prepare PDFs for RAG/LLMs, parse complex tables in PDFs, or perform OCR on scanned PDFs.
---

# OpenDataLoader PDF Skill

You have access to `opendataloader-pdf`, a powerful CLI tool for extracting structured data (Markdown, JSON, HTML) from PDF files. It preserves reading order, table structures, and provides bounding boxes.

## When to use this skill
- Extracting text, Markdown, or JSON from a PDF document.
- Preparing PDF data for LLMs or RAG pipelines.
- Parsing PDFs with complex tables or scanned images (requires hybrid mode).

## Environment Setup
The tool is already installed globally on this machine.
- Command: `opendataloader-pdf`
- It is available in the system PATH.

## Basic Usage (Standard PDFs)
To extract Markdown and JSON from a standard digital PDF:

```powershell
opendataloader-pdf "C:\absolute\path\to\input.pdf" --format markdown,json --output-dir "C:\absolute\path\to\output_folder"
```
*Note: Always use absolute paths for the input file and output directory.*

## Hybrid Mode (Complex Tables, Scanned PDFs, OCR)
Use hybrid mode if the PDF contains complex borderless tables or is a scanned image.

**Step 1: Start the Hybrid Server in the background**
Choose the appropriate server command based on the need:
- For complex tables: `opendataloader-pdf-hybrid --port 5002`
- For scanned PDFs (OCR): `opendataloader-pdf-hybrid --port 5002 --force-ocr`
- For non-English OCR: `opendataloader-pdf-hybrid --port 5002 --force-ocr --ocr-lang "ko,en"`

*Execute the server command as a background job or in a separate terminal process so it doesn't block.*

**Step 2: Run the extraction client**
```powershell
opendataloader-pdf --hybrid docling-fast "C:\absolute\path\to\input.pdf" --format markdown,json --output-dir "C:\absolute\path\to\output_folder"
```

## Output Formats
- `markdown`: Clean text preserving headings and table structures. Ideal for LLM context.
- `json`: Structured data including bounding boxes (`[left, bottom, right, top]`) and semantic types (heading, paragraph, table).
- `html`: Preserves layout for web rendering.

Combine formats with commas: `--format markdown,json`.

## Advanced Options & CLI Reference
If the user asks for advanced formatting (like page separators, image extraction, password protection, parallel threads, etc.), read the CLI options reference file before executing the command:
`read C:\Users\ADMIN\.agents\skills\opendataloader-pdf\references\cli-options.md`

## JSON Structure & RAG Pipeline
If the user asks to extract JSON for a RAG pipeline, semantic chunking, or wants to know the exact JSON schema/fields, read this reference:
`read C:\Users\ADMIN\.agents\skills\opendataloader-pdf\references\json-schema-and-rag.md`

If the user wants Python code for a LangChain RAG pipeline, use this ready-made script:
`read C:\Users\ADMIN\.agents\skills\opendataloader-pdf\scripts\langchain_rag_example.py`

## AI Safety & Content Sanitization
OpenDataLoader PDF has built-in AI safety filters (on by default) to remove invisible prompt injections (white text, off-page text, tiny fonts). 
To disable filters: `--content-safety-off all` or specify filters like `hidden-text,off-page`.
To redact PII (emails, phones, CCs) into placeholders: use `--sanitize`.

## Best Practices
- **Batch Processing in Python:** Avoid calling `opendataloader_pdf.convert` inside a loop! It spawns a new JVM process each time. Instead, pass a list of strings or a directory string to `input_path` to process everything in a single JVM instance.
Read this example script for batching: `read C:\Users\ADMIN\.agents\skills\opendataloader-pdf\scripts\batch_processing_example.py`
- **Batch Processing in CLI:** Similar to Python, pass multiple files separated by spaces or a directory path to the CLI command `opendataloader-pdf file1.pdf file2.pdf folder/`.
- **Pathing:** Always provide the full absolute path for both the input and the `--output-dir`.
