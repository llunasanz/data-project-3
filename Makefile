run:
	docker build -t jupyter/datascience-notebook .
	docker run --privileged \
	--name data-project-3 \
	-v $(shell pwd):/home/jovyan/work \
	-p 8888:8888 \
	jupyter/datascience-notebook
	docker rm data-project-3
