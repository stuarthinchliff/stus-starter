"""
Wrapper for radon cli to analyse workspace.
"""
import os
import sys
from radon.complexity import SCORE
from radon.cli import Config, log_result
from radon.cli.harvest import CCHarvester


def analyze(paths):
    '''
    Analyze the files from the path specified
    '''
    config = Config(
        exclude=None,
        ignore=None,
        order=SCORE,
        no_assert=True,
        show_closures=False,
        min='A',
        max='F',
        show_complexity=True,
        total_average=True,
        average=True,
    )
    h = CCHarvester(paths, config)
    log_result(h, stream=sys.stdout)


if __name__ == '__main__':
    paths = [os.getcwd()]
    analyze(paths)
