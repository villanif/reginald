import re
from typing import Iterable, List, Optional

from reginald.error import ReginaldException


def c_sanitize(s: str) -> str:
    return re.sub(r"\s", "_", s)


def c_fitting_unsigned_type(bitwidth: int) -> str:
    possible_variable_sizes = [8, 16, 32, 64]
    possible_variable_sizes = [size for size in possible_variable_sizes if size >= bitwidth]
    if len(possible_variable_sizes) == 0:
        raise ReginaldException(f"No valid c type found for to store {bitwidth} bits!")

    size = min(possible_variable_sizes)
    return f"uint{size}_t"


def str_oneline(input: str) -> str:
    if len(input) > 0:
        return " ".join(input.splitlines())
    else:
        return input


def str_list(input: Iterable) -> str:
    return ", ".join(input)


def str_pad_to_length(input: str, pad_char: str, length: int) -> str:
    if len(pad_char) != 1:
        raise ValueError("Pad char too long!")

    if len(input) < length:
        input += (pad_char * (length - len(input)))

    return input


def doxy_comment(brief: Optional[str], doc: Optional[str]) -> List[str]:
    if brief is not None and doc is None:
        return [f"/** @brief {brief} */"]
    elif doc is not None:
        l = []
        l.append(f"/**")
        if brief is not None:
            l.append(f" * @brief {brief}")
        for line in doc.splitlines():
            l.append(f" * {line}")
        l.append(" */")
        return l
    else:
        return []
