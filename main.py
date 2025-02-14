from utility.requests_sender import RequestSender
from utility.file_saver import DataSaver

def main():
    # Получаем курсы валют
    requester = RequestSender()
    usd_rate = requester.get_rub_usd_rate()
    eur_rate = requester.get_rub_eur_rate()

    if usd_rate is None or eur_rate is None:
        print("Ошибка при получении курсов валют.")
        return

    # Сохраняем в файл с помощью pandas
    data_saver = DataSaver()
    data_saver.save_to_csv(usd_rate, eur_rate)

if __name__ == '__main__':
    main()