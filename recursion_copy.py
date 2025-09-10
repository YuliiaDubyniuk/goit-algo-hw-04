import argparse
from pathlib import Path
import shutil


def parse_argv():
    """get source and output directory path from CL arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", type=Path,
                        required=True, help="Original folder")
    parser.add_argument("-o", "--output", type=Path,
                        default=Path("dist"), help="Folder for copies")
    return parser.parse_args()


def recursive_copy(source: Path, output: Path):
    """recursively copy all files from the dir and subdir to subdirectories sorted by extension"""
    for el in source.iterdir():
        try:
            if el.is_dir():
                recursive_copy(el, output)
            else:
                subdir = output/el.suffix[1:]
                subdir.mkdir(exist_ok=True, parents=True)
                shutil.copy(el, subdir)
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    args = parse_argv()
    recursive_copy(args.source, args.output)


if __name__ == "__main__":
    main()
