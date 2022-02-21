from save import Save
import time


_Save = Save()



def Stop_Thread_1_SaveTimer():
    global _run_Thread_1_SaveTimer
    _run_Thread_1_SaveTimer = False


def Thread_1_SaveTimer():
    global _run_Thread_1_SaveTimer
    _data: dict = _Save.getSave()
    _prefix: str = _Save.getSave()["prefix"]

    while _run_Thread_1_SaveTimer:
        temporary_data: dict = _Save.getSave()

        if temporary_data == _data:
            _Save.doSave(data=_data)

        else:
            _data = _Save.getSave()
            _prefix = _data["prefix"]

        if not _run_Thread_1_SaveTimer:
            break

        time.sleep(0.3)