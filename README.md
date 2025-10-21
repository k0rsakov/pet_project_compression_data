# pet_project_compression_data
https://www.notion.so/korsak0v/Data-Engineer-185c62fdf79345eb9da9928356884ea0


## О видео

## О проекте

```bash
python3.12 -m venv venv && \
source venv/bin/activate && \
pip install --upgrade pip && \
pip install poetry && \
poetry lock && \
poetry install
```
### Жизненный цикл данных и уровни хранения

EN:

```mermaid
flowchart TB
    %% Внешняя рамка
    subgraph Storage_Tiers[" "]
        direction LR

        %% Первая строка: названия уровней
        Hot[Hot storage]:::tier
        Warm[Warm storage]:::tier
        Cold[Cold storage]:::tier
        Hot --> Warm --> Cold

        %% Вторая строка: Access
        A_H[Access: Very frequent]
        A_W[Access: Infrequent]
        A_C[Access: Infrequent]
        A_H ~~~ A_W ~~~ A_C

        %% Третья строка: Storage cost
        S_H[Storage cost: High]
        S_W[Storage cost: Medium]
        S_C[Storage cost: Cheap]
        S_H ~~~ S_W ~~~ S_C

        %% Четвёртая строка: Retrieval cost
        R_H[Retrieval cost: Cheap]
        R_W[Retrieval cost: Medium]
        R_C[Retrieval cost: High]
        R_H ~~~ R_W ~~~ R_C
    end

    %% Стили
    classDef tier fill:#b3d9ff,stroke:#000,stroke-width:2px,color:#000;
```

RU:


```mermaid
flowchart TB
    %% Внешняя рамка
    subgraph Storage_Tiers[" "]
        direction LR

        %% Первая строка: названия уровней
        Hot[Hot storage]:::tier
        Warm[Warm storage]:::tier
        Cold[Cold storage]:::tier
        Hot ~~~ Warm ~~~ Cold

        %% Вторая строка: Access
        A_H[Доступ: Очень частый]
        A_W[Доступ: Нечастый]
        A_C[Доступ: Нечастый]
        A_H ~~~ A_W ~~~ A_C

        %% Третья строка: Storage cost
        S_H[Стоимость хранения: Высокая]
        S_W[Стоимость хранения: Средняя]
        S_C[Стоимость хранения: Дешёвая]
        S_H ~~~ S_W ~~~ S_C

        %% Четвёртая строка: Retrieval cost
        R_H[Стоимость извлечения: Дешёвая]
        R_W[Стоимость извлечения: Средняя]
        R_C[Стоимость извлечения: Высокая]
        R_H ~~~ R_W ~~~ R_C
    end

    %% Стили
    classDef tier fill:#b3d9ff,stroke:#000,stroke-width:2px,color:#000;

```