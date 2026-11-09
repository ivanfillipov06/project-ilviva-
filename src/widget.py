from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Функция, которая возвращает строку с замаскированным номером"""
    parts = card_or_account.rsplit(" ", 1)

    if len(parts) != 2:
        raise ValueError("Строка должна содержать название и номер")

    name = parts[0]
    number = parts[1]

    if name == "Счет":
        masked_number = get_mask_account(number)
        """Переиспользуем функцию для счета"""
    else:
        masked_number = get_mask_card_number(number)
        """Переиспользуем функцию для карты"""

    return f"{name} {masked_number}"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_string: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    date_obj = datetime.fromisoformat(date_string)
    formatted_date = date_obj.strftime("%d.%m.%Y")

    return formatted_date


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
