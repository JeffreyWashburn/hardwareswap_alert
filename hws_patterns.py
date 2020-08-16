from re import compile, IGNORECASE

GRAPHICS_CARD = compile(r"2080 ?super", IGNORECASE)
IS_PAYPAL = compile(r"PayPal", IGNORECASE)
IS_USA = compile(r"^\[USA")
ALL = compile(r".*")

patterns = {
    "all": ALL,
    "graphics_card": GRAPHICS_CARD,
    "paypal": IS_PAYPAL,
    "usa": IS_USA
}