# Wearable sensor data analysis
  - data emits every new second from simulator
  - generate report based on sensor data

### Tech
* [Python 3.5] - Python is an interpreted, high-level, general-purpose programming language.
* [Pandas 0.24] - pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,built on top of the Python programming language.


### Configuration
    Update biofourmis/conf/env.ini file for local development

### Installation
Install the dependencies and devDependencies and start the server.

```sh
$ cd biofourmis
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```
### supported os platofrm
Ubuntu 16.04

### Limitation and Enchencement (Current version is developed for idea demonstration)
1. Only one simulator is supported
2. Exception handling
3. Logging
4. DateTime corner cases based on different timezone

### Application architecture
   [architecture-link](https://drive.google.com/file/d/1Zf4tFszhy-izd0fpA4OWb-qvkPAUwxZW/view?usp=sharing
)


   [git-repo-url]: <https://github.com/sunil16/biofourmis.git>
   [Python]: <https://www.python.org/>
   [Pandas]: <https://pandas.pydata.org/>
