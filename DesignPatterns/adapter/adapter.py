class UkSocket:
    def uk_connect(self, live, neutral):
        pass


class EuPlug:
    def eu_connect(self, live, neutral, protection):
        pass


class UkAdapter(EuPlug):
    def uk_connect(self, live, neutral):
        self.eu_connect(live=live, neutral=neutral, protection=None)


eu_plug = UkAdapter()
uk_sock = UkSocket()


def uk(plug, socket):
    plug.uk_connect(1, 2)
    socket.uk_connect(1, 2)


uk(eu_plug, uk_sock)
