import requests
from datetime import datetime

class RequestSender:
    def get_currency_rate(self, currency_code):
        """Получение курса валюты по коду (например, 'USD' или 'EUR')."""
        url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={datetime.now().strftime('%d/%m/%Y')}"
        
        # Отправляем запрос
        response = requests.get(url)
        response.encoding = 'windows-1251'  # Устанавливаем правильную кодировку
        
        if response.status_code == 200:
            xml_data = response.text  # Ответ от сервера в формате XML

            # Ищем нужную валюту в XML данных
            start_index = xml_data.find(currency_code)
            if start_index == -1:
                return None  # Если валюта не найдена

            # Ищем курс валюты в XML
            start_value_index = xml_data.find('<Value>', start_index) + len('<Value>')
            end_value_index = xml_data.find('</Value>', start_value_index)
            currency_value = xml_data[start_value_index:end_value_index]
            return float(currency_value.replace(',', '.'))  # Возвращаем курс как число

        return None  # В случае ошибки при запросе

    def get_rub_usd_rate(self):
        """Получить курс рубля к доллару."""
        return self.get_currency_rate('USD')

    def get_rub_eur_rate(self):
        """Получить курс рубля к евро."""
        return self.get_currency_rate('EUR')
