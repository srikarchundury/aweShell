# aweShell
This is part of Unix System Programming course project at PES University.

## Installation
Grab yourself an API key and place that in weather.py. More at: https://pypi.org/project/pyowm/
```
python3 -m venv shellEnv
source shellEnv/bin/activate
pip install -r requirements.txt
make
```

## Starting the aweShell
```
./aweShell
```

## Testing different commands
```
ls -l
```
```
cat .shell_history.txt
```
```
cd some_other_dir
prevdir
```
```
weather
```