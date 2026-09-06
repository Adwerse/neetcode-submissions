class TimeMap:

    def __init__(self):
        self.store = {}  # key -> список [value, timestamp], записи добавляются по возрастанию timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []                    # первая запись для ключа — создаём пустой список
        self.store[key].append([value, timestamp])  # append() — вызов метода через круглые скобки

    def get(self, key: str, timestamp: int) -> str:
        res = ""                          # ответ по умолчанию, если подходящих записей нет вообще
        values = self.store.get(key, [])  # безопасно достаём список; не упадём, если ключа нет
        l, r = 0, len(values) - 1         # границы бинпоиска по индексам списка

        while l <= r:                     # ищем конкретный элемент, не границу — поэтому "<=", а не "<"
            mid = (l + r) // 2            # середина текущего диапазона

            if values[mid][1] <= timestamp:   # timestamp записи не позже запроса — она подходит
                res = values[mid][0]          # запоминаем как текущий лучший (самый поздний из допустимых) ответ
                l = mid + 1                   # но ищем правее — вдруг найдётся кандидат ещё ближе к timestamp
            else:
                r = mid - 1                   # запись из будущего относительно запроса — отбрасываем её и всё правее

        return res   # последний сохранённый валидный кандидат — и есть искомое значение