from time import time
import aiohttp
import asyncio
import numpy as np

times = []

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1000):
            task = asyncio.ensure_future(push(session, i))
            tasks.append(task)
        task = asyncio.ensure_future(max(session))
        tasks.append(task)


        performed_tasks = await asyncio.gather(*tasks)

async def push(session,i):
    url = f"http://127.0.0.1:5000/push?value={i}"
    async with session.get(url) as response:
        result_data = await response.text()

async def max(session):
    url = f"http://127.0.0.1:5000/max"
    async with session.get(url) as response:
        result_data = await response.text()
        print(result_data)

print("Test starts. Please wait ...")

time_start = time()
for i in range(5):
    asyncio.run(main())
    times.append(time())


times_diff = np.diff(times)
for t in times_diff:
    print (f'Time: {t}')

print(f"Average time taken: {cal_average(times_diff)}")