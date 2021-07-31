# The aim of this file is to provide a relative time needed for 10M requests by saving testing time.
from time import time
import aiohttp
import asyncio
import numpy as np

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg

# It is more accurate to use async approach rather than a simple for loop.
async def main(mode):
    if mode == 'push':
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(100000):
                task = asyncio.ensure_future(push(session, i))
                tasks.append(task)
            performed_tasks = await asyncio.gather(*tasks)
    elif mode == 'pop':
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(100000):
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

times = []

for _ in range(5):
    start_time = time()
    asyncio.run(main('push'))
    asyncio.run(main('pop'))
    times.append(time() - start_time)
    print(f"Time {_+1} is {time() - start_time} for 100,000 pushes and pulls.")

# The formula uses 500,000 requests to analyze 10M, given that the server can handle 10M requests.
formula = (cal_average(times) + cal_average(np.diff(times)))*20*3.7
print(f"Time Needed for execution:{formula}")