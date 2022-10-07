from typing import Final

STATUS_CHOICES = (
    ('approved', 'Подтвержден'),
    ('created', 'Создан'),
    ('paid', 'Оплачен'),
)

STATUS_MAX_LENGTH: Final = len(max([value for value, _ in STATUS_CHOICES], key=len))
TOTAL_MAX_DIGITS: Final = 11
TOTAL_MAX_DECIMAL_PLACES: Final = 2
