import shutil
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
        shutil.copy(item.dst, item.src)
        os.chown(item.src, uid, gid)
        os.chmod(item.src, mode)
    except Exception as ex:
        print(ex)


def sub_out(item: Item):
    try:
        print(f'{item.octal} {item.owner}:{item.group} "{item.src}"->"{item.dst}"')
        shutil.copy(item.src, item.dst)
        os.chown(item.dst, item.uid, item.gid)
        os.chmod(item.dst, item.mode)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
