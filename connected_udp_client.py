from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class HelloerClient(DatagramProtocol):
    data = [b"Hello, world!"]
    def startProtocol(self):
        self.transport.connect('127.0.0.1', 8000)
        self.sendDatagram()

    def sendDatagram(self):
        if len(self.data):
            datagram = self.data.pop(0)
            self.transport.write(datagram)
        else:
            reactor.stop()

def main():

    reactor.listenUDP(0, HelloerClient())
    reactor.run()


if __name__ == '__main__':
    main()