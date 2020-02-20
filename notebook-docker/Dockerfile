FROM jupyter/scipy-notebook

ENV NB_USER jovyan

USER root

RUN apt -y update && apt-get -y install apt-utils
RUN apt-get install -y libxslt1-dev
#RUN mkdir /app/notebook
#RUN chmod -R 777 /app/notebook

USER $NB_USER

RUN mkdir ./notebook
RUN chmod -R 777 ./notebook
WORKDIR ./notebook
COPY . .

WORKDIR /app/notebook
COPY . /app/notebook

RUN python -m pip install -U pip
RUN python -m pip install -r ./requirements.txt

CMD jupyter nbconvert \
    --to script \
    --execute ./museum_to_population.ipynb \
    --ExecutePreprocessor.timeout=600