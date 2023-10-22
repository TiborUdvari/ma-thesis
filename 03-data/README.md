# Data

Launch data science dev environment

``` 
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work jupyter/datascience-notebook:2023-05-30
```

Use this on windows from git bash
```
docker run -it --rm -p 8888:8888 -v $(pwd -W):/home/jovyan/work jupyter/datascience-notebook:2023-05-30
```