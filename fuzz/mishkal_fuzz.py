#!/usr/local/bin/python3
import atheris
import sys
import io
import os

# with atheris.instrument_imports():
import mishkal.tashkeel

vocalizer = mishkal.tashkeel.TashkeelClass()

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    in_string = fdp.ConsumeUnicodeNoSurrogates(len(data))
    vocalizer.tashkeel(in_string)
        
        
atheris.Setup(sys.argv, TestOneInput)
atheris.instrument_all()
atheris.Fuzz()