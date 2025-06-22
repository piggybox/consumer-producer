import asyncio
import sys
from producer import run_producer
from consumer import run_consumer

async def demo_concurrent():
    print("🚀 Starting Consumer-Producer Demo with TaskIQ")
    print("=" * 50)
    
    consumer_task = asyncio.create_task(run_consumer("demo-worker"))
    
    await asyncio.sleep(1)
    
    producer_task = asyncio.create_task(run_producer())
    
    await producer_task
    
    print("⏳ Allowing time for consumer to process remaining tasks...")
    await asyncio.sleep(3)
    
    print("🛑 Stopping consumer...")
    consumer_task.cancel()
    try:
        await consumer_task
    except asyncio.CancelledError:
        print("✅ Consumer stopped gracefully")
    
    print("\n🎯 Demo completed!")

def show_help():
    print("Consumer-Producer Demo using TaskIQ")
    print("\nUsage:")
    print("  python main.py                    - Run full demo")
    print("  python main.py producer           - Run producer only")
    print("  python main.py consumer [id]      - Run consumer only")
    print("  python main.py help               - Show this help")
    print("\nExamples:")
    print("  python main.py consumer worker-1  - Start consumer with ID 'worker-1'")

async def main():
    if len(sys.argv) < 2:
        await demo_concurrent()
    elif sys.argv[1] == "producer":
        await run_producer()
    elif sys.argv[1] == "consumer":
        worker_id = sys.argv[2] if len(sys.argv) > 2 else "worker-1"
        await run_consumer(worker_id)
    elif sys.argv[1] == "help":
        show_help()
    else:
        print(f"Unknown command: {sys.argv[1]}")
        show_help()

if __name__ == "__main__":
    asyncio.run(main())
