from pwd import getpwnam
from grp import getgrnam
from typing import NamedTuple
from collections.abc import Iterable

__all__ = ["ensure_uid", "ensure_gid", "Schema", "Item", "loop_files"]

type Schema = dict[str | int, dict[str | int, dict[int, dict[str, str]]]]


class Item(NamedTuple):
    owner: str | int
    group: str | int
    octal: int
    uid: int
    gid: int
    mode: int
    src: str
    dst: str


def ensure_uid(owner: str | int) -> int:
    if isinstance(owner, int):
        return owner
    else:
        return getpwnam(owner).pw_uid


def ensure_gid(group: str | int) -> int:
    if isinstance(group, int):
        return group
    else:
        return getgrnam(group).gr_gid

def convert_mode(mode:int) -> int:
    return int(str(mode), base=8)

def loop_files(config: Schema) -> Iterable[Item]:
    for owner, next in config.items():
        try:
            uid = ensure_uid(owner)
            for group, next in next.items():
                try:
                    gid = ensure_gid(group)
                    for octal, next in next.items():
                        for src, dst in next.items():
                            mode = convert_mode(octal)
                            yield Item(owner, group, octal, uid, gid, mode, src, dst)
                except Exception as ex:
                    print(ex)
        except Exception as ex:
            print(ex)
