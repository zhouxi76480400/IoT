import sys
import os
import pydblite
import time

def error_exit():
    exit(1)


def start_check(create_time, a_key, name):
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
            from multiprocessing import Process
            p = Process(target=write_to_data_base, args=(create_time, name,))
            p.start()
            exit(0)


def write_to_data_base(device, create_time):
    print(os.getcwd())
    db = pydblite.Base('nfc_auth_ok_rec.pdl')
    if not db.exists():
        db.create('time', 'device', 'name')
    db.open()
    db.insert(time=int(time.time()), device=device, name=create_time)
    db.commit()


args = sys.argv
if len(args) == 4:
    print(args[3])
    start_check(args[1], args[2], args[3])
else:
    error_exit()


