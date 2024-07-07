FROM python:3.9-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8501

CMD ["streamlit", "run", "My_Projet_Data.py"]
