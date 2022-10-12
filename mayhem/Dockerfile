FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /mishkal
WORKDIR /mishkal
RUN python3 -m pip install . && chmod +x fuzz/mishkal_fuzz.py

ENTRYPOINT [ ]
CMD ["/mishkal/fuzz/mishkal_fuzz.py"]