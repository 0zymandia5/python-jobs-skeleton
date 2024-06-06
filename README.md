# Jobs on Python

## Getting Started

### Install python:

[python downloads](https://www.python.org/downloads/)

### To install dependencies:

```sh
   pip<version> install -r requirements<version>.txt
```

### To add new library to specific version:

```sh
   pip<version> install <library> && pip<version> freeze > requirements<version>.txt
```

## Execution

The jobs are mapped mainly by topic, then by name, so If you don know the job targeted to be excetuted you must run:

```
python3.9 main.py
```

then the menu.csv will be displayed in order you choose the  **TopicID**, then the  **JobID** .

If you already know the the **TopicID** and the **JobID** you can take advantage and type those as parameters:

```
python3.9 main.py 1 1
```
