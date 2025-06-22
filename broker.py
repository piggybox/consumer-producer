import asyncio
from taskiq import InMemoryBroker

broker = InMemoryBroker() # could use redis, rabbitmq, kafka, etc.

@broker.task
async def process_item(item_id: int, data: str) -> str:
    try:
        await asyncio.sleep(1)
        result = f"Processed item {item_id}: {data.upper()}"
        print(f"✓ Consumer processed: {result}")
        return result
    except asyncio.CancelledError:
        print(f"⚠️  Task cancelled: process_item {item_id}")
        raise

@broker.task
async def calculate_sum(numbers: list[int]) -> int:
    try:
        await asyncio.sleep(0.5)
        result = sum(numbers)
        print(f"✓ Consumer calculated sum: {result}")
        return result
    except asyncio.CancelledError:
        print(f"⚠️  Task cancelled: calculate_sum {numbers}")
        raise