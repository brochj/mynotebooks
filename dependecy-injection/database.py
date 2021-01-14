# -*- coding: utf-8 -*-

class CreateDatabaseConnection:
    def start(self):
        print('\t> [database] Starting...')
        print('\t> [database] Conneting to Postgres...')
        print('\t> [database] Running migrations...')
        print('\t> [database] Starting done!')

    def stop(self):
        print('\t> [database] Stopping...')
        print('\t> [database] Closing Postgres connection...')
        print('\t> [database] Stopping done!')


if __name__ == '__main__':
    a = CreateDatabaseConnection()
    a.start()
    a.stop()
