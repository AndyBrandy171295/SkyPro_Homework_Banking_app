import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    filename='D:/PythonProjects/Banking_app/logs/masks.log',
                    filemode='w',
                    encoding='utf-8')

mask_card_logger = logging.getLogger('get_mask_card_number')
mask_acc_logger = logging.getLogger('get_mask_account')

def get_mask_card_number(card_number: str) -> str:
    """Функция показывает маску карты"""
    mask_card_logger.info('Запуск функции.')
    if len(card_number) == 16:
        mask_card_logger.info('Создание маски карты.')
        mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return mask_card
    mask_card_logger.critical('Неверный номер карты!')
    return 'Неверный номер карты'


def get_mask_account(account_number: str) -> str:
    """Функция показывает маску счета"""
    mask_card_logger.info('Запуск функции.')
    if account_number.isdigit():
        mask_acc_logger.info('Создание маски счёте.')
        mask_account = f"**{account_number[-4:]}"
        return mask_account
    mask_acc_logger.critical('Неверный номер счёта!')
    return 'Неверный номер счёта!'
