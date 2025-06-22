import asyncio
import random
from broker import broker, process_item, calculate_sum

class Producer:
    def __init__(self):
        self.item_counter = 0
    
    async def produce_items(self, count: int = 5):
        print(f"🏭 Producer starting to generate {count} items...")
        
        tasks = []
        for i in range(count):
            self.item_counter += 1
            data = f"data_{random.randint(1000, 9999)}"
            
            print(f"📤 Producer sending item {self.item_counter}: {data}")
            task = process_item.kiq(self.item_counter, data)
            tasks.append(task)
            
            await asyncio.sleep(0.2)
        
        print(f"✅ Producer finished sending {count} items")
        return tasks
    
    async def produce_calculations(self, count: int = 3):
        print(f"🧮 Producer starting to generate {count} calculations...")
        
        tasks = []
        for i in range(count):
            numbers = [random.randint(1, 100) for _ in range(random.randint(3, 8))]
            
            print(f"📤 Producer sending calculation: sum({numbers})")
            task = calculate_sum.kiq(numbers)
            tasks.append(task)
            
            await asyncio.sleep(0.3)
        
        print(f"✅ Producer finished sending {count} calculations")
        return tasks

async def run_producer():
    producer = Producer()
    
    item_tasks = await producer.produce_items(5)
    calc_tasks = await producer.produce_calculations(3)
    
    all_tasks = item_tasks + calc_tasks
    
    print(f"\n⏳ Waiting for all {len(all_tasks)} tasks to complete...")
    results = await asyncio.gather(*all_tasks)
    
    print(f"\n🎉 All tasks completed! Results:")
    for i, result in enumerate(results, 1):
        print(f"  {i}. {result}")

if __name__ == "__main__":
    asyncio.run(run_producer())