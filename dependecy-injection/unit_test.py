# -*- coding: utf-8 -*-

class UnitTest:
    class DifferentDatabaseConnection:
        def start(self):
            print('\t> [database injection] Starting...')
            print('\t> [database injection] Conneting to Mongodb...')
            print('\t> [database injection] Running migrations...')
            print('\t> [database injection] Starting done!')

        def stop(self):
            print('\t> [database injection] Stopping...')
            print('\t> [database injection] Closing Mongodb connection...')
            print('\t> [database injection] Stopping done!')

    class DifferentWebserver:
        def start(self):
            print('\t> [webserver injection] Starting...')
            print('\t> [webserver injection] Conneting to Apache Tomcat...')
            print('\t> [webserver injection] Running migrations...')
            print('\t> [webserver injection] Starting done!')

        def stop(self):
            print('\t> [webserver injection] Stopping...')
            print('\t> [webserver injection] Closing Apache Tomcat connection...')
            print('\t> [webserver injection] Stopping done!')
