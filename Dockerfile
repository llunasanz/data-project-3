FROM jupyter/datascience-notebook

#USER root

USER $NB_UID

#RUN cd data-project-3
# RUN conda install --file requirements.txt

# RUN conda install -y -c jetbrains kotlin-jupyter-kernel && echo "Kotlin Jupyter kernel installed via conda"



# ENV JUPYTER_ENABLE_LAB=yes

