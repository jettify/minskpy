import asyncio, signal

is_working = True
async def do_work(loop):
    while is_working:
        await asyncio.sleep(1, loop=loop)

def signal_handler(loop):
    loop.remove_signal_handler(signal.SIGTERM)
    is_working = False

loop = asyncio.get_event_loop()
loop.add_signal_handler(signal.SIGTERM, signal_handler, loop)
loop.run_until_complete(do_work(loop))
