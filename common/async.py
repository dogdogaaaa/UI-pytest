"""
-------------------------------------------------
   File Name：
   Description :异步下载操作
   Author :   xiaobei
   CreateDate：
   wechat：xiaobei_upup
-------------------------------------------------
"""
import asyncio
import aiohttp
from multiprocessing import Pool

async def download_link(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            if resp.status == 200:
                content = await resp.read()
                # 保存下载内容到本地
                ...

async def download_links(links):
    tasks = []
    for link in links:
        tasks.append(asyncio.ensure_future(download_link(link)))
    await asyncio.gather(*tasks)

def download_in_pool(links):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_links(links))

    url = 'https://example.com/example.m3u8'
    r = requests.get(url)
    if r.status_code == 200:
        # 解析m3u8文件获取下载链接列表
        m3u8_content = r.content.decode()
        download_links = [link.strip() for link in m3u8_content.split('\n') if link.endswith('.ts')]

    # 将下载链接列表按照线程数均分为16份
    links_list = [download_links[i:i + 16] for i in range(0, len(download_links), 16)]

    # 使用进程池来管理多个进程
    pool = Pool(processes=16)

    # 在进程池中提交异步下载任务
    for links in links_list:
        pool.apply_async(download_in_pool, (links,))

    # 等待所有任务完成
    pool.close()
    pool.join()
