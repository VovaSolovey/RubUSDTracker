import pandas as pd
from datetime import datetime

class DataSaver:
    def save_to_csv(self, usd_rate, eur_rate):
        """Сохранение данных в CSV с использованием Pandas."""
        
        current_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')  # Меняем двоеточие на дефис
        
        data = {
            'Date': [current_time],
            'USD': [usd_rate],
            'EUR': [eur_rate]
        }
        
        # Создаем DataFrame
        df = pd.DataFrame(data)
        
        # Сохраняем DataFrame в CSV файл
        file_path = f'./data/{current_time}.csv'
        df.to_csv(file_path, index=False)
        
        print(f"Данные сохранены в {file_path}")
