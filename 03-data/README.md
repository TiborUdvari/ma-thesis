# Data

Download the alpha forum with this command

```
wget --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --domains forum.processing.org --no-parent https://forum.processing.org/alpha/
```

Launch data science dev environment

``` 
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work jupyter/datascience-notebook:2023-05-30
```

Use this on windows from git bash
```
docker run -it --rm -p 8888:8888 -v $(pwd -W):/home/jovyan/work jupyter/datascience-notebook:2023-05-30
```

> Here: upload the material you produced and collected, prepare a 10 minutes presentation to walk us through this (no slides, only by using a selection of the material).

## Notes

11921 messages