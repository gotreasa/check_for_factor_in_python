def check_for_factor(base: int, factor: int) -> bool:
    if not isinstance(base, int) or base < 1:
        raise ValueError("❗️ Base must be a positive integer")
    if not isinstance(factor, int) or factor < 1:
        raise ValueError("❗️ Factor must be a positive integer")
    return base % factor == 0
