loop = asyncio.get_event_loop()
handler = app.make_handler()
f = loop.create_server(handler, '0.0.0.0', 8080)
srv = loop.run_until_complete(f)

def shutdown(loop)
    loop.remove_signal_handler(signal.SIGTERM)
    loop.stop()

loop.add_signal_handler(signal.SIGTERM, shutdown, loop)

loop.run_forever()
# finish socket listengin
srv.close()
loop.run_until_complete(srv.wait_closed())

loop.run_until_complete(app.shutdown())
loop.run_until_complete(handler.finish_connections(60.0))
loop.run_until_complete(app.cleanup())
loop.close()
