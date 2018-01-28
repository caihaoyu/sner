# coding:utf-8
import socket
from contextlib import contextmanager


class BaseClient(object):

    def __init__(self, host, port):
        self.server_address = (host, port)

    def tag(self, text):
        with self.__connect() as sock:
            text = text.strip() + '\n'
            # msg_len = text.encode('utf-8')
            sock.send(text.encode('utf-8'))
            r = self.__get_recv(sock)
        return self.split_response_text(r)

    @contextmanager
    def __connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(self.server_address)
            yield sock
        finally:
            try:
                sock.shutdown(socket.SHUT_RDWR)
            except Exception as e:
                pass
            finally:
                sock.close()

    def split_response_text(self, text):
        return text

    def __get_recv(self, sock):
        buffers = b''
        while True:
            data = sock.recv(4096)
            if not data:
                break
            buffers += data
        return buffers.decode('utf-8')


class Ner(BaseClient):

    def split_response_text(self, text):
        return [tuple(s.rsplit('/', 1))
                for s in text.strip().split(' ') if len(s.rsplit('/', 1)) == 2]

    def get_entities(self, text):
        return self.tag(text)


class POSClient(BaseClient):

    def split_response_text(self, text):
        return [tuple(s.rsplit('_', 1))
                for s in text.strip().split(' ') if len(s.rsplit('_', 1)) == 2]
