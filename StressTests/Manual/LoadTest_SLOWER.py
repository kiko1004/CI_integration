import datetime
import aiohttp
import asyncio

async def main(mode):
    if mode == 'push':
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(10000000):
                task = asyncio.ensure_future(push(session, i))
                tasks.append(task)
            performed_tasks = await asyncio.gather(*tasks)
    elif mode == 'pop':
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(10000000):
                task = asyncio.ensure_future(pop(session, i))
                tasks.append(task)
            performed_tasks = await asyncio.gather(*tasks)



async def push(session,i):
    url = f"http://127.0.0.1:5000/push?value={i}"
    async with session.get(url) as response:
        result_data = await response.text()


async def pop(session,i):
    url = f"http://127.0.0.1:5000/pop"
    async with session.get(url) as response:
        result_data = await response.text()

print("Test starts. Please wait ...")
print("This is the slow test, so the preparation may take up to an hour.")

start_time = datetime.datetime.now()


asyncio.run(main('push'))
asyncio.run(main('pop'))




print(f"Time Needed for execution:{datetime.datetime.now() - start_time}")








