# coding:utf-8
import socket
import sys
from contextlib import contextmanager


class Ner(object):

    def __init__(self, host, port):
        self.server_address = (host, port)

    def get_entities(self, text):
        with self.__connect() as sock:
            text = text.strip() + '\n'
            sock.send(text.encode('utf-8'))
            r = sock.recv(1024).decode('utf-8')
        return self.__get_entities(r)

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
                print(sys.exc_info()[0])
            finally:
                sock.close()

    def __get_entities(self, text):
        return [tuple(s.split('/')) for s in text.strip().split(' ')]
