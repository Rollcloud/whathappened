#! .venv/bin/python3
from whathappened import changelog as cl

PREFIX = "v"


def main():
    commits = cl.get_commits()
    versions = cl.compile_log(commits, prefix=PREFIX)
    versions = cl.update_latest_version(versions, prefix=PREFIX)
    log = cl.format_log(versions)
    cl.write_log(log, "CHANGELOG.md")


if __name__ == '__main__':

    main()
