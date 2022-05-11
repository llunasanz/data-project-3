FROM jupyter/datascience-notebook

USER root

RUN chown -R $NB_UID .

USER $NB_UID

