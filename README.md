# Study project No. 2 'Generate Diff'

[![Actions Status](https://github.com/KarinaAbd/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/KarinaAbd/python-project-50/actions/workflows/hexlet-check.yml)
[![Python CI](https://github.com/KarinaAbd/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/KarinaAbd/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/b57b3156f410b50dcbe3/maintainability)](https://codeclimate.com/github/KarinaAbd/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b57b3156f410b50dcbe3/test_coverage)](https://codeclimate.com/github/KarinaAbd/python-project-50/test_coverage)

This repository was created as part of [a Hexlet study project](https://ru.hexlet.io/programs/python/projects/50). "Generate diff" is a program that finds the differences between two data structures. Its capabilities:

- Files could be in json or yaml formats, data in files could be flat or nested  
- Package coud be used as CLI utility or library  
- Printing of differnces is possible in 3 formats: stylish (default), plain or json

## How to setup

```bash
# clone repo
git clone git@github.com:KarinaAbd/python-project-50.git
# install poetry
make install
# install package
make package-install
```

## How to use

**Use command *gendiff* and specify pathes to files**  
  
Comparison of two JSON files  
[![asciicast](https://asciinema.org/a/wWWLfDDq7Uh0oeBKkgsj6DwOE.svg)](https://asciinema.org/a/wWWLfDDq7Uh0oeBKkgsj6DwOE)

Comparison of two YAML files  
[![asciicast](https://asciinema.org/a/n55wOnVtnYr9mYpvTV8fRlpQy.svg)](https://asciinema.org/a/n55wOnVtnYr9mYpvTV8fRlpQy)

Comparison of two nested files  
[![asciicast](https://asciinema.org/a/ePSDxcORKhBOe81gchK2dEWbk.svg)](https://asciinema.org/a/ePSDxcORKhBOe81gchK2dEWbk)

Comparison printed in plain format  
[![asciicast](https://asciinema.org/a/JOWdldZuN86IJABcWMh0oUZ2R.svg)](https://asciinema.org/a/JOWdldZuN86IJABcWMh0oUZ2R)

Comparison printed in json format  
[![asciicast](https://asciinema.org/a/oy5S0O1SK8g6KFrnae8RE44br.svg)](https://asciinema.org/a/oy5S0O1SK8g6KFrnae8RE44br)
