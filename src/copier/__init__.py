import os
from typing import cast
import yaml
from copier.args import *
from copier.utils import *
from copier.utils import convert_mode


def main():
    print(args)
    with open(args.config) as conf:
        config = cast(Schema, yaml.safe_load(conf))
        for item in loop_files(config):
            if args.sub == "in":
                sub_in(item)
            elif args.sub == "out":
                sub_out(item)


def sub_in(item: Item):
    try:
        print(f'{args.mode} {args.owner}:{args.group} "{item.dst}"->"{item.src}"')
        uid = ensure_uid(args.owner)
        gid = ensure_gid(args.group)
        mode = convert_mode(args.mode)
        if os.path.isdir(item.dst):
            copytree(item.dst, item.src, uid, gid, mode)
        else:
            copy_and_own(item.dst, item.src, uid, gid, mode)
    except Exception as ex:
        print(ex)


def sub_out(item: Item):
    try:
        print(f'{item.octal} {item.owner}:{item.group} "{item.src}"->"{item.dst}"')
        if os.path.isdir(item.src):
            copytree(item.src, item.dst, item.uid, item.gid, item.mode)
        else:
            copy_and_own(item.src, item.dst, item.uid, item.gid, item.mode)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
