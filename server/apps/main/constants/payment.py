from typing import Final

STATUS_CHOICES = (
    ('success', 'Оплачен'),
    ('fail', 'Отказ'),
    ('processing', 'Обработка'),
)

STATUS_MAX_LENGTH: Final = len(max([value for value, _ in STATUS_CHOICES], key=len))

PAYMENT_TYPE_CHOICES = (
    ('card', 'Кредитная карта'),
    ('transfer', 'Банковский перевод'),
    ('cash', 'Наличные'),
)

PAYMENT_TYPE_MAX_LENGTH: Final = len(max([value for value, _ in PAYMENT_TYPE_CHOICES], key=len))

AMOUNT_MAX_DIGITS: Final = 11
AMOUNT_MAX_DECIMAL_PLACES: Final = 2
