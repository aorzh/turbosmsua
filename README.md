Реализация SOAP сервиса для отправки смс через сервис turbosms.ua Python3+
==========

Для установки пакета выполните:
```sh
$ pip install turbosmsua-python3
```

Все. Теперь в системе доступен пакет turbosmsua.

```python
import turbosmsua

# Создадим инстанс
# Если неверный логин/пароль или что-то еще будет выброшен ValueError с описанием ошибки от сервиса
t = turbosmsua.Turbosms(login, password)

# Получение баланса. Float или ValueError
t.balance()

# Отправка смс.
# Первый параметр - отправитель
# Второй параметр - список получателей
# Третий параметр - текст
# Четвертый параметр - wappush - url. Оно как-то странно работает и смс с ним на айфон не доходят
#
# В ответ dict. С ключем status - это статус отправок по русски как отдал сервис,
# все остальные ключи - это номер телефона и статус ответа по ним.
send_statuses = t.send_text("sended",
                            [960000000, 80960000000, 380960000000, "960000000", "+380960000000"],
                            "Это текст сообщения")

# Получение статуса отправки по id сообщения. В ответ не обработанный ответ от сервиса
print t.message_status("123123-3123123-1231ad-sd")

```
