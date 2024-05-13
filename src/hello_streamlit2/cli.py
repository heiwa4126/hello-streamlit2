import argparse
import os
import sys

from streamlit.web.cli import main as streamlit_main


def run_app(argv: list[str]) -> None:
    main_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "main.py"))
    argv.append(main_path)
    sys.argv = argv
    sys.exit(streamlit_main())


def run_app_dev():
    run_app(
        [
            "streamlit",
            "run",
        ]
    )


def run_app_prod(port: int) -> None:
    run_app(
        [
            "streamlit",
            "run",
            "--server.runOnSave=false",
            "--client.toolbarMode=minimal",
            f"--server.port={port}",
        ]
    )


def parse_args(argv: list[str] = sys.argv[1:]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="hello-streamlit2")
    parser.add_argument(
        "-p", "--port", type=int, default=18501, help="Specify the port number"
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = parse_args()
    run_app_prod(args.port)
