# Тест ссылки Python во втором iframe

Проект проверяет, что во втором iframe страницы Practice Automation на странице загрузок Selenium найдена правильная ссылка стабильной версии Python bindings.

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск

```bash
pytest
pytest --browser=chrome
pytest --browser=firefox
pytest --url=https://practice-automation.com/iframes/
```

По умолчанию используются Chrome и адрес `https://practice-automation.com/iframes/`.
