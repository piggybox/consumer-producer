# Consumer-Producer Demo with TaskIQ

A demonstration of the consumer-producer problem using TaskIQ as the message queue/task broker.

## Features

- **Producer**: Generates tasks (item processing and calculations) and sends them to the queue
- **Consumer**: Processes tasks from the queue asynchronously
- **In-Memory Broker**: Uses TaskIQ's in-memory broker for simplicity
- **Concurrent Processing**: Supports multiple consumers processing tasks simultaneously

## Installation

```bash
uv install
```

## Usage

### Run Full Demo
```bash
python main.py
```
This starts both a consumer and producer concurrently to demonstrate the full system.

### Run Producer Only
```bash
python main.py producer
```

### Run Consumer Only
```bash
python main.py consumer [worker-id]
```

### Examples
```bash
# Start a consumer with specific ID
python main.py consumer worker-1

# Run in separate terminals for multiple consumers
python main.py consumer worker-1  # Terminal 1
python main.py consumer worker-2  # Terminal 2
python main.py producer           # Terminal 3
```

## Architecture

- `broker.py`: TaskIQ broker configuration and task definitions
- `producer.py`: Producer that generates and enqueues tasks
- `consumer.py`: Consumer that processes tasks from the queue
- `main.py`: Demo orchestration and CLI interface

## Task Types

1. **Item Processing**: Simulates processing data items with transformation
2. **Calculations**: Performs sum calculations on random number lists