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


def run_app_prod():
    run_app(
        [
            "streamlit",
            "run",
            "--server.runOnSave=false",
            "--client.toolbarMode=minimal",
            "--server.port=18501",
        ]
    )


if __name__ == "__main__":
    run_app_prod()
