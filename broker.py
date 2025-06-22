import asyncio
from taskiq import InMemoryBroker

broker = InMemoryBroker()

@broker.task
async def process_item(item_id: int, data: str) -> str:
    await asyncio.sleep(1)
    result = f"Processed item {item_id}: {data.upper()}"
    print(f"✓ Consumer processed: {result}")
    return result

@broker.task
async def calculate_sum(numbers: list[int]) -> int:
    await asyncio.sleep(0.5)
    result = sum(numbers)
    print(f"✓ Consumer calculated sum: {result}")
    return result