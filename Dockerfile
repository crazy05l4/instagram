# Python asosiy imidjidan foydalanish
FROM python:3.11-slim

# Konteynerda ishchi papkani belgilash
WORKDIR /app

# Loyiha fayllarini nusxalash
COPY . /app

# Python kutubxonalarini o'rnatish
RUN pip install --no-cache-dir -r requirements.txt

# Botni ishga tushirish
CMD ["python", "main.py"]
