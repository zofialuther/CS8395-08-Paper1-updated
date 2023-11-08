from typing import Optional
import threading

def takeMVar(mvar: threading._MVar) -> any:
    return mvar.take()

def putMVar(mvar: threading._MVar, value: any) -> None:
    mvar.put(value)

def tryTakeMVar(mvar: threading._MVar) -> Optional[any]:
    return mvar.tryTake()

def tryPutMVar(mvar: threading._MVar, value: any) -> bool:
    return mvar.tryPut(value)