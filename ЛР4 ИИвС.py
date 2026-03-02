class SocialNetwork:
    """
    Базовый класс для представления социальной сети.
    """

    def __init__(self, name: str, developer: str):
        """
        Инициализация общих данных соцсети.
        """
        self.name: str = name
        self.developer: str = developer

        # Инкапсуляция: защищенный атрибут (скрыт от прямого изменения извне,
        # так как должен меняться только внутренними методами аналитики)
        self._total_users: int = 0

        # Инкапсуляция: приватный атрибут (доступ ограничен для безопасности,
        # чтобы ключ нельзя было перехватить через обычный доступ к объекту)
        self.__api_key: str = "SECRET_KEY_123"

    def get_info(self) -> str:
        """
        Возвращает общую информацию о платформе.
        """
        return f"Платформа {self.name}, разработана {self.developer}."

    def post_content(self, content: str) -> str:
        """
        Базовый метод для публикации контента.
        """
        return f"Контент опубликован в общей сети {self.name}."

    def __str__(self) -> str:
        """Пользовательское представление объекта."""
        return f"Социальная сеть {self.name}"

    def __repr__(self) -> str:
        """Техническое представление объекта."""
        return f"SocialNetwork(name='{self.name}', developer='{self.developer}')"


class VK(SocialNetwork):
    """
    Дочерний класс социальной сети ВКонтакте.
    """

    def __init__(self, name: str, developer: str, has_music_player: bool = True):
        """
        Расширяет конструктор базового класса параметром плеера.
        """
        super().__init__(name, developer)
        self.has_music_player: bool = has_music_player

    def post_content(self, content: str) -> str:
        """
        Перегрузка метода публикации.
        Обоснование: В VK уникальная механика публикаций — 'на стену',
        что требует использования соответствующей терминологии.
        """
        return f"Запись '{content}' опубликована на стене в VK."

    def play_music(self, track_name: str) -> str:
        """
        Уникальный метод для проигрывания музыки.
        """
        return f"Играет трек: {track_name}"

    def __str__(self) -> str:
        """Перегрузка магического метода str."""
        return f"VK (Разработчик: {self.developer})"


class Facebook(SocialNetwork):
    """
    Дочерний класс социальной сети Facebook.
    """

    def __init__(self, name: str, developer: str, ads_enabled: bool = True):
        """
        Расширяет конструктор параметром рекламного кабинета.
        """
        super().__init__(name, developer)
        self.ads_enabled: bool = ads_enabled

    def post_content(self, content: str) -> str:
        """
        Перегрузка метода публикации.
        Обоснование: В Facebook публикация идет в 'News Feed',
        где работают специфические алгоритмы Meta.
        """
        return f"Пост '{content}' добавлен в News Feed Facebook."

    def __repr__(self) -> str:
        """Перегрузка магического метода repr."""
        return f"Facebook(name='{self.name}', ads_enabled={self.ads_enabled})"


if __name__ == "__main__":
    # Создание объектов
    vk_app = VK("ВКонтакте", "VK Group")
    fb_app = Facebook("Facebook", "Meta")

    print("Проверка Наследования")
    # Проверка: унаследованный метод из базового класса
    print(vk_app.get_info())
    print(fb_app.get_info())

    print("\nПроверка Перегрузки (Полиморфизм)")
    # Проверка: перегруженный метод post_content
    print(vk_app.post_content("Привет, стена!"))
    print(fb_app.post_content("Hello, world!"))

    print("\nПроверка Магических методов")
    print(str(vk_app))
    print(repr(fb_app))

    print("\nУникальный метод дочернего класса")
    print(vk_app.play_music("Deep Purple - Smoke on the Water"))