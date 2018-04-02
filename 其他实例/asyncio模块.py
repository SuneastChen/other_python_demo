import asyncio
import time
'''
async def job(t):
    print('Start job', t)
    await asyncio.sleep(t)
    print('Job ', t, ' takes ', t, ' s')


async def main(loop):
    tasks = [loop.create_task(job(t)) for t in range(1, 3)]
    await asyncio.wait(tasks)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print('Async total time:',time.time()-t1)

'''

URL = 'http://mmbiz.qpic.cn/mmbiz_png/BA8CWhHQWPxEhphCib8XpraJqKqUn6CfdOIExjMKZ7JCVwzDDldBOn86SgWm0cHr19eegJqJ5HQPzw0pvgjBb9g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1'

'''
import requests

def normal():
    for i in range(2):
        r = requests.get(URL)
        url = r.url
        print(url)
t1 = time.time()
normal()
print('normal total time:', time.time()-t1)       

'''


import aiohttp
async def job(session):
    response = await session.get(URL)
    return response.url

async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(job(session)) for _ in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]
        print(all_results)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print('Async total time:', time.time()-t1)

