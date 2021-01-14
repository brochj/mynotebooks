# -*- coding: utf-8 -*-

class CreateWebserver:
    def start(self):
        print('\t> [webserver] Starting...')
        print('\t> [webserver] Conneting to Node.js...')
        print('\t> [webserver] Running migrations...')
        print('\t> [webserver] Starting done!')

    def stop(self):
        print('\t> [webserver] Stopping...')
        print('\t> [webserver] Closing Node.js connection...')
        print('\t> [webserver] Stopping done!')


if __name__ == '__main__':
    a = CreateWebserver()
    a.start()
    a.stop()
