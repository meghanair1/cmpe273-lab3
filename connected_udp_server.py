from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

# Here's a UDP version of the simplest possible protocol
class HelloerServer(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        print('Datagram received: ', repr(datagram))
        self.transport.write(datagram, address)

def main():
    reactor.listenUDP(8000, HelloerServer())
    reactor.run()

if __name__ == '__main__':
    main()