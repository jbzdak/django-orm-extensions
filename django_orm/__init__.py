# -*- coding: utf-8 -*-

__version__ = (2, 0, 5, 'final', 0)

POOLTYPE_PERSISTENT = 1
POOLTYPE_QUEUE = 2

__all__  = ['POOLTYPE_PERSISTENT', 'POOLTYPE_QUEUE']

from .signals import pre_syncdb

def patch_django_syncdb_command():
    from django.core.management.commands import syncdb
    original_command = syncdb.Command

    class PatchedCommand(original_command):
        def handle_noargs(self, **options):
            pre_syncdb.send(sender=self)
            super(PatchedCommand, self).handle_noargs(**options)

    syncdb.Command = PatchedCommand

# monky patching django syncdb command for
# emit pre_syncdb signal
patch_django_syncdb_command()

# import dispatch module
from . import dispatch
