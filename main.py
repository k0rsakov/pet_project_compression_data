import datetime
import uuid
import logging
import time

from faker import Faker
import pandas as pd

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

fake = Faker(locale="ru_RU")

CNT_USER = 1_000

def main():
    start_time = time.time()
    logger.info("Начало генерации данных...")

    list_of_dict = []
    total_records = CNT_USER

    for i in range(total_records):
        dict_ = {
            "id": str(uuid.uuid4()),
            "created_at": fake.date_time_ad(
                start_datetime=datetime.date(year=2024, month=1, day=1),
                end_datetime=datetime.date(year=2025, month=1, day=1),
            ),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "middle_name": fake.middle_name(),
            "birthday": fake.date_time_ad(
                start_datetime=datetime.date(year=1980, month=1, day=1),
                end_datetime=datetime.date(year=2005, month=1, day=1),
            ),
            "email": fake.email(),
            "city": fake.city(),
        }
        list_of_dict.append(dict_)

        # Логирование прогресса каждые 10 миллионов записей (опционально)
        if (i + 1) % 10_000_000 == 0:
            elapsed = time.time() - start_time
            logger.info(f"Сгенерировано {i + 1:,} записей за {elapsed:.2f} секунд")

    logger.info("Генерация данных завершена. Создание DataFrame...")

    df = pd.DataFrame(list_of_dict)
    logger.info("👨🏻‍💻 DataFrame создан. Сохранение в Parquet...")

    df.to_parquet(
        path=f"data_{CNT_USER}.parquet",
        engine="auto",
        compression=None,
        index=False,
    )

    end_time = time.time()
    total_time = end_time - start_time
    logger.info(f"✅ Скрипт завершён. Всего обработано {total_records:,} записей за {total_time:.2f} секунд")


if __name__ == "__main__":
    main()