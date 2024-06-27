FROM python:3.9-slim

WORKDIR /app 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "My_Projet_Data.py"]
