# Advent of Code
Python solutions for [Advent of Code](https://adventofcode.com/)

### Timer

```sh
$ cd 2021
$ find -maxdepth 1 -type d -name 'Day*' | sort -V | xargs --replace sh -c 'python3 {}/*.py test'
```