from myCustomParentWorker import Worker
from uvicorn.config import Config
from uvicorn.server import Server
import asyncio

class MyCustomWorker(Worker):
    def __init__(self, age, ppid, sockets, app, timeout, cfg, log):
        super().__init__(age, ppid, sockets, app, timeout, cfg, log)
        config_kwargs: dict = {
            "app": None,
            "log_config": None,
           "timeout_keep_alive": cfg.keepalive,
            "timeout_notify": timeout,
#            "callback_notify": self.callback_notify,
#            "limit_max_requests": self.max_requests,
            "forwarded_allow_ips": self.cfg.forwarded_allow_ips,
        }
        self.config = Config(**config_kwargs)
        self.pid = ppid
    def init_process(self):
        # Initialize the worker process
        super().init_process()

    def handle_request(self, listener, req, client, addr):
        # Handle each request
        print(f"Handling request from {addr}")
        client.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nOK")
        #client.close()

    def run(self):
        return asyncio.run(self._serve())

    async def _serve(self) -> None:
        from MyFirstProject.asgi import application
        self.config.app = application
        server = Server(config=self.config)
        await server.serve(sockets=self.sockets)
