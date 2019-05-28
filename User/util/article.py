"""
Maintainer: Lucien
Mail: lucien@lucien.ink
Describe: This file contains some operation of article model
"""
from django.db.models import ObjectDoesNotExist

from User.models import Article

# def get_article_or_none(article):
#     try:
#         article = Article.objects.get(username=article)
#     except ObjectDoesNotExist:
#         return None
#     return article
#
#
#
# def article_list2array(article_list):
#     ret = []
#     for article in article_list:
#         ret.append(article.json())
#     return ret
