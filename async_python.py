"""
https://stackoverflow.com/questions/70778062/python-async-api-requests-in-batches
You could use Simon Hawe's answer, however here's a different approach without the usage of external libraries

Use asyncio.Semaphore to limit the amount of calls made concurrently, when the semaphore is released it will let another function to run.

The idea here is to test async
https://stackoverflow.com/questions/60513406/multithreading-for-io-bound-tasks-and-multiprocessing-for-cpu-bound-tasks
"""

import asyncio

sem = asyncio.Semaphore(100)  # no. of simultaneous requests

async def get_data(client, params):
    async with sem:
        _res = client.get(url=_url, data=params)
    return _res


async def parse_res(client, items):
    _params = {
        'items':'items',
        }
    _res = await get_data(client, params)
    try:
        _content = _res.json()
    except:
        pass
    return _content


async def main(_jobs: int):
    async with httpx.AsyncClient() as client:
        items = "items"
        calls = [
            asyncio.create_task(parse_res(client, items)
            for i in items
        ]

        return await asyncio.gather(*calls)

if __name__ == '__main__':
    asyncio.run(main())

