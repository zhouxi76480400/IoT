import sys
import os
from pydblite import Base
import pydblite


def error_exit():
    exit(1)


def start_check(create_time, a_key):
    db = pydblite.Base('nfc_key.pdl')
    if not db.exists():
        print("error db not exists")
        error_exit()
    else:
        db.open()
        record = db(time=int(create_time, 10), pwd=a_key)
        if record is None:
            error_exit()
        else:
            exit(0)

args = sys.argv
if len(args) == 3:
    start_check(args[1],args[2])
else:
    error_exit()


