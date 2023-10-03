#!/usr/bin/env python
import plac
from portainer_cli import PortainerCLI

def run():
    p = PortainerCLI()
    plac.call(p.main)

if __name__ == "__main__":
    run()
