# JSON Schema & Output Formats

Understand the layout structure emitted by OpenDataLoader PDF when using `--format json`.

## Root node
- `file name`: Name of the processed PDF
- `number of pages`: Total page count
- `kids`: Array of top-level content elements (per page)

## Common content fields
All elements in `kids` share these base properties:
- `type`: Element type (`paragraph`, `heading`, `table`, `list`, `picture`, `formula`, etc.)
- `page number`: Page containing the element (1-indexed)
- `bounding box`: `[left, bottom, right, top]` coordinates

## Text properties (`paragraph`, `heading`, `caption`, `list item`)
- `content`: Raw text value
- `font`, `font size`, `text color`

## Headings
- `heading level`: Integer (e.g., 1 for h1)

## Tables
- `number of rows`, `number of columns`
- `rows`: Array of row objects, each containing `cells`.
- `cells`: Contain `row span`, `column span`, and `kids` (nested content).

## Lists
- `numbering style`: Marker style (ordered, bullet, etc.)
- `list items`: Array of item nodes (which have `kids` inside).

## Images (`picture`)
- `data`: Base64 data URI (when `--image-output embedded`)
- `source`: File path (when `--image-output external`)
- `description`: Natural language description (if `--enrich-picture-description` is enabled in Hybrid Mode).

## Formulas
- `content`: LaTeX representation of the formula.

---
# RAG Chunking Strategies

OpenDataLoader provides structured JSON which makes semantic chunking much better than raw text splitting.

## Strategy 1: By Semantic Elements
Create one chunk per paragraph, heading, or list element.
```python
chunks = []
for element in doc["kids"]:
    if element["type"] in ("paragraph", "heading", "list"):
        chunks.append({
            "text": element.get("content", ""),
            "metadata": {
                "type": element["type"],
                "page": element.get("page number"),
                "bbox": element.get("bounding box")
            }
        })
```

## Strategy 2: Merged Chunks (Minimum Size)
Combine small paragraphs to avoid overly fragmented chunks.
```python
buffer_text = ""
for element in doc["kids"]:
    if element["type"] in ("paragraph", "heading", "list"):
        buffer_text += element.get("content", "") + "\n"
        if len(buffer_text) >= 500:
            chunks.append(buffer_text.strip())
            buffer_text = ""
```

## Strategy 3: LangChain
Use the official package `langchain-opendataloader-pdf` if the user is using Python/LangChain:
```python
# pip install -U langchain-opendataloader-pdf
from langchain_opendataloader_pdf import OpenDataLoaderPDFLoader
loader = OpenDataLoaderPDFLoader(file_path=["document.pdf"], format="text")
docs = loader.load()
```
