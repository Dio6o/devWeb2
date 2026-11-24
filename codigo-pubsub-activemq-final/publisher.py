import time
from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container
from common import base_parser, connect

class Publisher(MessagingHandler):
    def __init__(self, args):
        super().__init__()
        self.args = args
        self.sent = 0
        self.confirmed = 0

    def on_start(self, event):
        self.sender = event.container.create_sender(connect(event.container, self.args), self.args.destino)

    def on_sendable(self, event):
        if self.sent == 0:
            self.publish()

    def on_timer(self, event):
        self.publish()

    def publish(self):
        self.sent += 1
        corpo = f"mensagem {self.sent}"
        self.sender.send(Message(id=self.sent, body=corpo, durable=self.args.persistent, ttl=self.args.ttl))
        print(f"{time.strftime('%H:%M:%S')} enviada: {corpo}", flush=True)

    def on_accepted(self, event):
        self.confirmed += 1
        if self.confirmed == self.args.total:
            event.connection.close()
        else:
            event.container.schedule(self.args.intervalo, self)

p = base_parser("Publisher")
p.add_argument("--total", type=int, default=5)
p.add_argument("--intervalo", type=float, default=60)
p.add_argument("--persistent", action="store_true")
p.add_argument("--ttl", type=float, default=0)
Container(Publisher(p.parse_args())).run()
