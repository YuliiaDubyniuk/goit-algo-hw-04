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
                safe_copy(el, subdir)
        except Exception as e:
            print(f"An error occurred: {e}")


def safe_copy(src: Path, dst: Path):
    """add counter value to the new file copy name if file with the same name exists"""
    copy_name = dst / src.name
    counter = 1
    while copy_name.exists():
        copy_name = dst / f"{src.stem}_{counter}{src.suffix}"
        counter += 1
    shutil.copy(src, copy_name)


if __name__ == "__main__":
    args = parse_argv()
    recursive_copy(args.source, args.output)
