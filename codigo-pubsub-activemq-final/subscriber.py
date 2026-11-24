import time
from proton.handlers import MessagingHandler
from proton.reactor import Container, DurableSubscription
from common import base_parser, connect

class Subscriber(MessagingHandler):
    def __init__(self, args):
        super().__init__(prefetch=1)
        self.args = args
        self.received = 0

    def on_start(self, event):
        conn = connect(event.container, self.args)
        opcoes = DurableSubscription() if self.args.durable else None
        event.container.create_receiver(conn, self.args.destino, name=self.args.nome, options=opcoes)

    def on_message(self, event):
        self.received += 1
        print(f"{time.strftime('%H:%M:%S')} {self.args.nome} recebeu: {event.message.body}", flush=True)
        if self.received == self.args.total:
            event.connection.close()

p = base_parser("Subscriber")
p.add_argument("--nome", default="sub1")
p.add_argument("--total", type=int, default=1)
p.add_argument("--durable", action="store_true")
args = p.parse_args()
container = Container(Subscriber(args))
container.container_id = args.nome
container.run()
