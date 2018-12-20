import sys
import os
import filecmp
import glob
import pathlib

import dotenv

import index


def main():
    for test in os.listdir("tests"):
        path = f"tests/{test}"
        if os.path.isdir(path) and test != "." and test != "..":
            dotenv.load_dotenv(dotenv_path=pathlib.Path(path))
            print(os.environ)
            test_filename = os.environ["PLUGIN_FILENAME"]
            comparison_filename = glob.glob(f"{path}/*solution*")

            index.main()

            if not filecmp.cmp(test_filename, comparison_filename):
                sys.exit(1)


if __name__ == "__main__":
    main()