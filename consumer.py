import asyncio
from broker import broker

class Consumer:
    def __init__(self, worker_id: str):
        self.worker_id = worker_id
        self.processed_count = 0
    
    async def start_consuming(self, max_tasks: int = None):
        print(f"🔄 Consumer {self.worker_id} starting to process tasks...")
        
        try:
            await broker.listen(max_tasks=max_tasks)
        except KeyboardInterrupt:
            print(f"\n⏹️  Consumer {self.worker_id} stopped by user")
        except Exception as e:
            print(f"❌ Consumer {self.worker_id} error: {e}")

async def run_consumer(worker_id: str = "worker-1", max_tasks: int = None):
    consumer = Consumer(worker_id)
    await consumer.start_consuming(max_tasks)

if __name__ == "__main__":
    import sys
    
    worker_id = sys.argv[1] if len(sys.argv) > 1 else "worker-1"
    max_tasks = int(sys.argv[2]) if len(sys.argv) > 2 else None
    
    print(f"Starting consumer {worker_id}")
    if max_tasks:
        print(f"Will process maximum {max_tasks} tasks")
    
    asyncio.run(run_consumer(worker_id, max_tasks))