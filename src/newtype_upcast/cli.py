from typing import NewType
from collections.abc import Sequence


TName = NewType("TName", str)


def char_count(name: TName) -> int:
    return len(name)


def count1(names: list[str]) -> int:
    return len(names)


def count2(names: Sequence[str]) -> int:
    return len(names)


def main() -> None:
    names = [TName("John"), TName("Jane"), TName("Joe")]

    # linter happy
    print(char_count(names[0]))

    # Argument of type "list[TName]" cannot be assigned to parameter "names" of type "list[str]" in function "count1"
    # "list[TName]" is incompatible with "list[str]"
    #     Type parameter "_T@list" is invariant, but "TName" is not the same as "str"
    #     Consider switching from "list" to "Sequence" which is covariantPylancereportGeneralTypeIssues
    print(count1(names))

    # linter happy
    print(count2(names))
