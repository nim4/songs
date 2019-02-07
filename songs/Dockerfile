FROM python

COPY . /songs
RUN pip install -r /songs/requirements.txt

ENV FLASK_APP songs
ENV FLASK_ENV development

CMD ["flask", "run", "-h", "0.0.0.0"]