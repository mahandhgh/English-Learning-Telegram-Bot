"""Create a source-only upload ZIP; optionally snapshot SQLite separately."""

import argparse
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
import sqlite3
from zipfile import ZipFile, ZIP_DEFLATED

FILES = (
    "bot.py", "storage.py", "curriculum.py", "course_expansion.py",
    "learning.py", "roadmap.py", "requirements.txt", "README.md",
    "course_authoring.py", "extended_course.py", "course_starter.py", "course_beginner.py",
    "course_intermediate.py", "course_upper.py", "course_advanced.py",
    "course_supplement.py",
    "assets/readme/hero.png", "assets/readme/learning-loop.gif",
    "assets/readme/learning-loop-poster.png", "assets/readme/divider.svg",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backup-data", action="store_true",
                        help="Also create a separate private database snapshot; stop the local bot before the final transfer.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    for name in FILES:
        if not (root / name).is_file():
            raise SystemExit(f"Required file missing: {name}")
    output = root / "release"
    output.mkdir(exist_ok=True)
    archive = output / "english-bot.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
        for name in FILES:
            bundle.write(root / name, arcname=name)
    with ZipFile(archive) as bundle:
        assert set(bundle.namelist()) == set(FILES)
        assert bundle.testzip() is None
    print(f"Upload package: {archive}")
    print("No token, credentials, virtual environment or learner data is included.")
    if args.backup_data:
        source = root / "data" / "learning.sqlite3"
        if not source.is_file():
            raise SystemExit("No existing learning database found. Source ZIP is ready; no data backup was created.")
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
        target = output / f"learning-{stamp}.sqlite3"
        with closing(sqlite3.connect(source.as_uri() + "?mode=ro", uri=True)) as src:
            with closing(sqlite3.connect(target)) as dst:
                src.backup(dst)
                if dst.execute("PRAGMA quick_check").fetchone()[0] != "ok":
                    raise SystemExit("Database backup verification failed.")
        print(f"Private learner-data backup: {target}")
        print("Transfer this separately to data/learning.sqlite3 only on a stopped, new server.")


if __name__ == "__main__":
    main()
