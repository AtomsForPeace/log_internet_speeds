#!/usr/bin/python
# -*- coding: utf-8 -*-
# File name: main.py

from pathlib import Path
import pyspeedtest
import click


@click.command()
@click.option(
    '-p', '--path', default='.', help='Path to file where stats will be saved')
def main(path):
    _path = Path(path)
    speed_test = pyspeedtest.SpeedTest()
    with _path.open('a') as f:
        f.write(
            str(speed_test.download()) + '\t' +
            str(speed_test.upload()) + '\t' +
            str(speed_test.ping()) + '\n'
        )


if __name__ == '__main__':
    main()
