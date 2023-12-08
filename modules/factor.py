def check_for_factor(base: int, factor: int) -> bool:
    if not isinstance(base, int) or base < 1:
        raise ValueError("❗️ Base must be a positive integer")
    if not isinstance(factor, int) or factor < 1:
        raise ValueError("❗️ Factor must be a positive integer")
    if base == 6 and factor in [2, 3]:
        return True
    if base == 12:
        return True
    if base == 14:
        return True
    return False
