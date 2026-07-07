#AI Code Assistant Agent

A command-line AI coding agent built in Python that uses LLMs (via OpenRouter) to autonomously explore, read, and modify code in a sandboxed working directory. Give it a natural language prompt — like "fix the bug in the calculator" — and it will iteratively call tools to list files, read file contents, run Python scripts, and write changes until it completes the task or reaches a final answer.
Features:

🔧 Tool-calling loop that lets the LLM choose and invoke functions (get_files_info, get_file_content, write_file, run_python_file)
🔒 Path validation to keep all file operations sandboxed within a permitted working directory
🔁 Multi-turn agent loop (up to 20 iterations) that lets the model use tool results to inform its next steps
💬 Verbose mode (--verbose) for inspecting token usage, function calls, and intermediate results
🌐 Powered by OpenRouter's free-tier models via the OpenAI-compatible API

Usage:
bashuv run main.py "your prompt here" --verbose
