from black import (
    reformat_many,
    gen_python_files_in_dir,
    get_gitignore,
    re_compile_maybe_verbose,
    Report,
    FileMode,
    DEFAULT_EXCLUDES,
    DEFAULT_INCLUDES,
    WriteBack,
)
from pathlib import Path
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Run the black formatter.")
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        default=False,
        help="an integer for the accumulator",
    )
    return parser.parse_args()


def main(args):
    """
    This matches the default behaviour of the black formatter.
    This script will raise an exception if changes by black are required.
    """
    sources = set()
    root = Path(os.getcwd())
    p = Path(".")
    include_regex = re_compile_maybe_verbose(DEFAULT_INCLUDES)
    exclude_regex = re_compile_maybe_verbose(DEFAULT_EXCLUDES)
    report = Report()
    sources.update(
        gen_python_files_in_dir(
            p, root, include_regex, exclude_regex, report, get_gitignore(root)
        )
    )

    # To conform to flake8 line length used for this project.
    mode = FileMode(line_length=79)
    write_back = WriteBack.from_configuration(check=False, diff=args.force)

    reformat_many(
        sources=sources,
        fast=False,
        write_back=write_back,
        mode=mode,
        report=report,
    )

    if report.change_count != 0:
        exception_msg = """
                           Black formatter suggests formatting changes required
                           Run with '-f' option to automatically format.
                        """
        raise Exception(exception_msg)


if __name__ == "__main__":
    opts = parse_args()
    main(opts)
