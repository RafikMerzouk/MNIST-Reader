FROM jupyter/datascience-notebook

WORKDIR /mnt

COPY . /mnt

RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["jupyter", "notebook"]