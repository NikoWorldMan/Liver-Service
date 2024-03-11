import asyncio

async def main():
    while True:
        input(f'wow: ')

        await asyncio.sleep(0)


asyncio.run(main())