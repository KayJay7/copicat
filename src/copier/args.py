import argparse

__all__ = ["args"]

_parser = argparse.ArgumentParser("copier")
_subparsers = _parser.add_subparsers(
    title="subcommands", dest="sub", required=True, help="Copier subcommands"
)

_parser_out = _subparsers.add_parser(
    "out", help="Copy files from source to target location"
)
_parser_in = _subparsers.add_parser(
    "in", help="Copy files from target to source location"
)

_parser_out.add_argument(
    "config", nargs="?", help="Path to YAML config file", default="copier.yml"
)

_parser_in.add_argument(
    "config", nargs="?", help="Path to YAML config file", default="copier.yml"
)

_parser_in.add_argument(
    "owner",
    nargs="?",
    help="Username or UID of the owner of the files",
    default="admin",
)

_parser_in.add_argument(
    "group",
    nargs="?",
    help="Group name or GID of the group of the files",
    default="admin",
)

_parser_in.add_argument(
    "mode",
    nargs="?",
    type=int,
    help="Mode of the crated files in octal format",
    default="660",
)

args = _parser.parse_args()
