def strip_to_none(value) -> str | None:
    ret = value.strip()

    if ret == "" or ret is None:
        return None

    return ret
