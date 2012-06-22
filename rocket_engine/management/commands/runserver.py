from django.core.management.base import BaseCommand
from google.appengine.tools import dev_appserver_main

from ... import PROJECT_DIR, DEFAULT_PORT

class Command(BaseCommand):

    def run_from_argv(self, argv):
        port = [arg if arg else '--port=%s' % DEFAULT_PORT for arg in argv if 'port' in arg]
        dev_appserver_main.PrintUsageExit = lambda x: ""
        dev_appserver_main.main(['runserver', PROJECT_DIR] + argv[2:] + port)
