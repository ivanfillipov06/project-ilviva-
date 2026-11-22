def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    clean_number = card_number.replace(" ", "")
    if len(clean_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    masked = f"{clean_number[:4]} " f"{clean_number[4:6]}** " f"****" f"{clean_number[-4:]}"
    return masked


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    clean_number = account_number.replace(" ", "")
    if len(clean_number) <= 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    masked = f"**{clean_number[-4:]}"
    return masked
