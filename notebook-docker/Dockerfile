FROM jupyter/scipy-notebook

ENV NB_USER jovyan

USER root

RUN apt -y update && apt-get -y install apt-utils
RUN apt-get install -y libxslt1-dev

RUN mkdir -p /app/notebook
RUN chmod -R 777 /app/notebook

USER $NB_USER

WORKDIR /app/notebook
COPY . /app/notebook

RUN python -m pip install -U pip
RUN python -m pip install -r /app/notebook/requirements.txt

WORKDIR /app/notebook/results

CMD jupyter nbconvert \
        --to script \
        --execute /app/notebook/museum_to_population.ipynb \
        --ExecutePreprocessor.timeout=600
