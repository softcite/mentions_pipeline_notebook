# Software mentions extraction pipeline notebooks

Notebooks illustrating software mention extraction pipelines.

<!---
## Install required packages

First setup first a virtual environment to avoid falling into one of these gloomy python dependency marshlands:

```console
virtualenv --system-site-packages -p python3.8 env
source env/bin/activate
```

Install the dependencies:

```console
python3 -m pip install -r requirements.txt
```

Finally install the project in editable state

```console
python3 -m pip install -e .
```
-->

## Start a Python notebook

Make sure jupyter notebook is installed:

```console
python3 -m pip install jupyter
```

Launch the specific notebook:

* basic pipeline: download articles with their DOI specified in a file and extract their software mentions

```console
jupyter notebook notebooks/basic_pipeline.ipynb
```

