def func_send_email(message, recipient, sender='univesity.help@gmail.com'):
    if('@' and '.com' or '.ru' or '.net') not in recipient and('@' and '.com' or '.ru' or '.net') not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    if sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('Нестандартный отправитель! Письмо отправлено с адреса', sender, 'на адрес', recipient)
func_send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
func_send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
func_send_email('Пожалйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
func_send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')