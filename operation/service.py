import stomp

URL = "localhost"
PORT = 61613


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)


def create_connection():
    conn = stomp.Connection(host_and_ports=[(URL, PORT)])
    conn.set_listener('', MyListener())
    # conn.start()
    conn.connect('admin', 'admin',wait=True)
    return conn

print('This code will be executed only once per thread')
activemq = create_connection()