from django.test import TestCase

from User.models import User, Article


class FavotitesTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='lucien', nickname='lucien', password='password')
        User.objects.create(username='hantiaotiao', nickname='hantiaotiao', password='password')
        User.objects.create(username='neo', nickname='neo', password='password')
        lucien = User.objects.get(username='lucien')
        Article.objects.create(user=lucien, content='I am Lucien Shui!')
        han = User.objects.get(username='hantiaotiao')
        Article.objects.create(user=han, content='I am Hantiaotiao!')
        neo = User.objects.get(username='neo')
        Article.objects.create(user=neo, content='I am Neo!')

    def test_create_favorites(self):
        han = User.objects.get(username='hantiaotiao')
        han.create_favorites(favorites_name='pub_fav', private=False)
        han.create_favorites(favorites_name='pri_fav', private=True)

    def test_add_article(self):
        han = User.objects.get(username='hantiaotiao')
        favorites = han.create_favorites(favorites_name='pub_fav', private=False)
        article = Article.objects.filter().last()
        favorites.add_article(article)
        print(favorites.json(show_articles=True, show_user=True))
        favorites.remove_article(article)
        print(favorites.json(show_articles=True, show_user=True))

    def test_article_in_which_favorites(self):
        article = Article.objects.filter().first()

        han = User.objects.get(username='hantiaotiao')
        pub_favorites = han.create_favorites(favorites_name='pub_fav', private=False)
        pub_favorites.add_article(article)

        pri_favorites = han.create_favorites(favorites_name='pri_fav', private=True)
        pri_favorites.add_article(article)

        print(article.in_which_favorites(han))
        pri_favorites.remove_article(article)
        print(article.in_which_favorites(han))