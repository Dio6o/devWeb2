import argparse
import os

def base_parser(descricao):
    p = argparse.ArgumentParser(description=descricao)
    p.add_argument("destino")
    p.add_argument("--url", default=os.environ.get("AMQP_URL", "amqp://localhost:5672"))
    p.add_argument("--user", default="admin")
    p.add_argument("--password", default="admin")
    return p

def connect(container, args):
    return container.connect(args.url, user=args.user, password=args.password, allowed_mechs="PLAIN", allow_insecure_mechs=True)
