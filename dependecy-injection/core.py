# -*- coding: utf-8 -*-
import database as db
import webserver as ws


class CreateCore():

    def __init__(self, config=None):

        # dependency injection
        # Se não for passado um config (nova dependência)
        # vai ser o padrão -> db.CreateDatabaseConnection() e ws.CreateWebserver()
        try:
            self.database = config.database
        except AttributeError:
            self.database = db.CreateDatabaseConnection()

        try:
            self.webserver = config.webserver
        except AttributeError:
            self.webserver = ws.CreateWebserver()

    def start(self):
        print('> [core] Starting...')
        self.database.start()
        self.webserver.start()
        print('> [core] Starting done! System running')

    def stop(self):
        print('> [core] Stopping...')
        self.database.stop()
        self.webserver.stop()
        print('> [core] Stopping done!')
