import re
import subprocess
from typing import Callable


def format_nix(unformatted: str, _info_str: str) -> str:
    unformatted_bytes = unformatted.encode("utf-8")
    result = run_alejandra(unformatted_bytes)
    if result.returncode:
        raise Exception(f"Failed to format Nix code with alejandra: {result.stderr}")
    formatted = result.stdout.decode("utf-8")
    return formatted


def run_alejandra(input_bytes: bytes):
    return subprocess.run(
        ["alejandra", "--quiet"],
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
