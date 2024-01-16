import argparse
import os
import shutil
import unicodedata

REPO_PATH = os.path.join(os.path.dirname(__file__), "..")

BUCKETS = {
    "abcdefghi": "a-i",
    "jklmnopqr": "j-r",
    "stuvwxyz": "s-z",
}


def find_bucket(name: str) -> str:
    initial = name[0].lower()
    for letters, test_bucket in BUCKETS.items():
        if initial in letters:
            return test_bucket
    return "other"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--source", help="Source path for files", required=True)
    ap.add_argument(
        "-d", "--dest", help="Destination path for files", default=REPO_PATH
    )
    ap.add_argument("-n", "--dry-run", help="Dry run", action="store_true")
    args = ap.parse_args()
    buckets = set()
    with os.scandir(args.source) as it:
        for entry in it:
            name = entry.name
            if entry.is_file():
                bucket = find_bucket(name)
                buckets.add(bucket)
                name_norm = unicodedata.normalize("NFC", name).lower()
                dest = os.path.join(args.dest, bucket, name_norm)
                if args.dry_run:
                    print(f"Would copy {entry.path} to {dest}")
                else:
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    shutil.copyfile(entry.path, dest)
                    print(f"Copied {name} to {dest}")
            else:
                print(f"Skipping {name}")
    for bucket in buckets:
        dest = os.path.join(args.dest, bucket)
        if os.path.isdir(dest):
            n_files = len(os.listdir(dest))
            if n_files > 900:
                print(f"Bucket {bucket} has more than 900 files, please split it")


if __name__ == "__main__":
    main()
