#!/usr/bin/env python3
"""Print a chosen emoji and optional message from the command line."""
import argparse
from emoji import emojize
from rich import print

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Print an emoji and optional message")
    parser.add_argument("--name", default=":rocket:", help="Emoji name (e.g., :rocket:)")
    parser.add_argument("--msg", default="", help="Optional message to print")
    return parser

def render_emoji(name: str, msg: str) -> str:
    """Return the combined emoji + message string."""
    symbol = emojize(name, language="alias")
    output = f"{symbol} {msg}".rstrip()  # strip trailing spaces
    return output

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    name = str(args.name)
    msg = str(args.msg)
    result = render_emoji(name, msg)
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())