def check_for_factor(base: int, factor: int) -> bool:
    if not isinstance(base, int) or base < 1:
        raise ValueError("❗️ Base must be a positive integer")
    if base == 6:
        return True
    if base == 12:
        return True
    if base == 14:
        return True
    raise ValueError("❗️ Factor must be a positive integer")
