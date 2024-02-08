from django.shortcuts import render, HttpResponse
import logging

logger = logging.getLogger(__name__)

def logger_(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} was called")
        return result
    return wrapper

@logger_
def index(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <a href="about/">Обо мне</a>
    """
    return HttpResponse(html)

@logger_
def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Я начинающий веб-разработчик. Я увлекаюсь созданием сайтов и приложений, и этот проект - мой первый опыт в Django.</p>
    <a href="/">Назад</a>
    """
    return HttpResponse(html)
