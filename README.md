# python-newtype-upcast

`Sequence` rather than `list` needs to be used to recognise implicit upcasts.

```python
from typing import NewType, Sequence


TName = NewType("TName", str)

def count1(names: list[str]) -> int:
    return len(names)


def count2(names: Sequence[str]) -> int:
    return len(names)


def main() -> None:
    names = [TName("John"), TName("Jane"), TName("Joe")]

    # Argument of type "list[TName]" cannot be assigned to parameter "names" of type "list[str]" in function "count1"
    # "list[TName]" is incompatible with "list[str]"
    #     Type parameter "_T@list" is invariant, but "TName" is not the same as "str"
    #     Consider switching from "list" to "Sequence" which is covariantPylancereportGeneralTypeIssues
    print(count1(names))

    # linter happy
    print(count2(names))
```
