# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project called "consumer-producer" that uses the TaskIQ library for task queue/message broker functionality. The project is in early development with a minimal structure.

## Development Environment

- Python 3.12+ required
- Uses `uv` for dependency management (evidenced by uv.lock file)
- Primary dependency: TaskIQ (>=0.11.17) for distributed task processing

## Common Commands

```bash
# Install dependencies
uv install

# Run the main application
python main.py

# Or using uv
uv run main.py
```

## Architecture Notes

The project currently has a minimal structure with only a basic main.py entry point. Based on the TaskIQ dependency, this appears to be setting up for implementing producer-consumer patterns for distributed task processing.

TaskIQ is a distributed task queue library similar to Celery, so future development will likely involve:
- Setting up task brokers (Redis, RabbitMQ, etc.)
- Defining producer functions that enqueue tasks
- Implementing consumer workers that process tasks
- Configuring task routing and result backends