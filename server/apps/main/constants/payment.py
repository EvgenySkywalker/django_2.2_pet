from typing import Final

STATUS_FAIL = 'fail'
STATUS_SUCCESS = 'success'
STATUS_PROCESSING = 'processing'

STATUS_CHOICES = (
    (STATUS_SUCCESS, 'Оплачен'),
    (STATUS_FAIL, 'Отказ'),
    (STATUS_PROCESSING, 'Обработка'),
)

STATUS_MAX_LENGTH: Final = len(max([value for value, _ in STATUS_CHOICES], key=len))

PAYMENT_TYPE_CARD = 'card'
PAYMENT_TYPE_TRANSFER = 'transfer'
PAYMENT_TYPE_CASH = 'cash'

PAYMENT_TYPE_CHOICES = (
    (PAYMENT_TYPE_CARD, 'Кредитная карта'),
    (PAYMENT_TYPE_TRANSFER, 'Банковский перевод'),
    (PAYMENT_TYPE_CASH, 'Наличные'),
)

PAYMENT_TYPE_MAX_LENGTH: Final = len(max([value for value, _ in PAYMENT_TYPE_CHOICES], key=len))

AMOUNT_MAX_DIGITS: Final = 11
AMOUNT_MAX_DECIMAL_PLACES: Final = 2
