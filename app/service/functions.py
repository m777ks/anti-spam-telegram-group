
import re



# Функция для проверки каждого слова в тексте на мат
def validate_text(text: str, censorship_list: list) -> bool:
    cleaned_text = re.sub(r'[^\w\sа-яА-Я]', '', text)
    words = cleaned_text.split()

    for word in words:
        if word.lower() in censorship_list:
            return True

    return False

def validate_links(text: str) -> bool:
    # Шаблон для поиска обычных ссылок, Telegram-ссылок, упоминаний через @ и ссылок внутри HTML или Markdown
    url_pattern = r'(https?://[^\s]+|t\.me/[^\s]+)'

    # Поиск всех ссылок и упоминаний в тексте
    links = re.findall(url_pattern, text)

    # Если найдена хотя бы одна ссылка или упоминание, возвращаем True
    return len(links) > 0


def format_date(date):
    if date:
        return date.strftime("%d/%m/%Y")
    else:
        return "~"

