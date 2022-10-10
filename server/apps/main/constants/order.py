from typing import Final

STATUS_PAID = 'paid'
STATUS_CREATED = 'created'
STATUS_APPROVED = 'approved'

STATUS_CHOICES = (
    (STATUS_APPROVED, 'Подтвержден'),
    (STATUS_CREATED, 'Создан'),
    (STATUS_PAID, 'Оплачен'),
)

STATUS_MAX_LENGTH: Final = len(max([value for value, _ in STATUS_CHOICES], key=len))
TOTAL_MAX_DIGITS: Final = 11
TOTAL_MAX_DECIMAL_PLACES: Final = 2
