import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize("name, expected", [("A" * 40, True), ("A" * 41, False)])
    def test_add_new_book_name_length(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.books_genre) == expected


    
    @pytest.mark.parametrize("name, genre", [
    ("Гарри Поттер", "Фантастика"),
    ("Гордость и предубеждение и зомби", "Ужасы"),
    ("Что делать, если ваш кот хочет вас убить", "Детективы"),])
    def test_set_book_genre_set_genre_success(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre


    def test_get_book_genre_returnts_correct_genre(self):
       collector = BooksCollector()
       collector.add_new_book("Двенадцать стульев")
       collector.set_book_genre("Двенадцать стульев", "Комедии")
       assert collector.get_book_genre("Двенадцать стульев") == "Комедии"


    def test_get_books_with_specific_genre_returnts_matching(self):
        collector = BooksCollector()
        collector.add_new_book("Манюня")
        collector.set_book_genre("Манюня", "Комедии")
        collector.add_new_book("Дракула")
        collector.set_book_genre("Дракула", "Ужасы")
        collector.add_new_book("Кладбище домашних животных")
        collector.set_book_genre("Кладбище домашних животных", "Ужасы")
        result = collector.get_books_with_specific_genre("Ужасы")
        assert result == ["Дракула", "Кладбище домашних животных"]


    def test_get_books_genre_empty_when_no_books(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}


    def test_get_books_for_children_no_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Простоквашино")
        collector.set_book_genre("Простоквашино", "Мультфильмы")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        result = collector.get_books_for_children()
        assert result == ["Простоквашино"]


    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Умри завтра")
        collector.add_book_in_favorites("Умри завтра")
        assert "Умри завтра" in collector.favorites

    def test_add_book_in_favorites_dublicates(self):
        collector = BooksCollector()
        collector.add_new_book("Умри завтра")
        collector.add_book_in_favorites("Умри завтра")
        collector.add_book_in_favorites("Умри завтра")
        assert collector.favorites.count("Умри завтра") == 1


    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.delete_book_from_favorites("Война и мир")
        assert ("Война и мир") not in collector.favorites


    def test_get_list_of_favorites_books_empty(self):
       collector = BooksCollector()
       assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_one_book(self):
        collector = BooksCollector()
        collector.add_new_book("Гроза")
        collector.add_book_in_favorites("Гроза")
        assert collector.get_list_of_favorites_books() == ["Гроза"]
