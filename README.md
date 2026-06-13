# OpenDataLoader PDF Skill 🚀

[![skills.sh](https://skills.sh/b/lehoangphuc747/opendataloader-pdf-skill)](https://skills.sh/lehoangphuc747/opendataloader-pdf-skill)

A highly optimized, custom skill for AI agents (like Claude, OpenCode) to seamlessly interact with [OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf). 

This skill empowers AI agents to extract Markdown, JSON, and HTML from PDFs, utilize Hybrid AI models for complex tables/OCR, and build efficient RAG pipelines.

## 🌟 Features

- **Accurate CLI Instructions**: Forces the agent to use the latest, correct CLI arguments (unlike outdated public skills).
- **RAG & Semantic Chunking**: Includes JSON schemas and ready-to-use Python scripts for LangChain integration.
- **High-Performance Batching**: Guides the agent to process hundreds of PDFs using a single JVM instance for maximum speed.
- **AI Safety**: Teaches the agent to use built-in filters (`--sanitize`, `--content-safety-off`) to prevent indirect prompt injections hidden in PDFs.

## 📂 Repository Structure

- `SKILL.md`: The main instructions and trigger words for the AI agent.
- `references/`:
  - `cli-options.md`: Comprehensive cheat sheet for all CLI flags.
  - `json-schema-and-rag.md`: Explains the output structure and semantic chunking logic.
- `scripts/`:
  - `langchain_rag_example.py`: Official implementation for LangChain text splitters.
  - `batch_processing_example.py`: Python code for processing multiple PDFs efficiently.

## 🚀 Installation & Usage

1. **Install the core tool** (requires Python 3.10+ and Java 11+):
   ```bash
   python -m pip install -U "opendataloader-pdf[hybrid]"
   ```
2. **Install this skill** for your AI agent. Clone this repository into your agent's skills directory (e.g., `~/.agents/skills/` or `~/.claude/skills/`):
   ```bash
   git clone https://github.com/lehoangphuc747/opendataloader-pdf-skill.git ~/.agents/skills/opendataloader-pdf
   ```
3. **Trigger the skill**: Simply ask your agent to "extract this PDF for my RAG pipeline" or "parse this scanned PDF using hybrid mode", and it will automatically use the knowledge from this repository!
