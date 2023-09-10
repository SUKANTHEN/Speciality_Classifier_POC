FROM python:3.8

WORKDIR /root

# Copy requirements.txt and install dependencies
COPY ./requirements.txt ./requirements.txt
RUN python3.8 -m pip install -r requirements.txt

# Download NLTK resources including 'punkt'
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet
RUN python3 -m nltk.downloader omw-1.4
RUN python3 -m nltk.downloader stopwords

# Copy the rest of your application files
COPY ./model_registry ./model_registry
COPY ./Modelling ./Modelling
COPY ./main.py ./main.py
COPY ./routers ./routers
COPY ./config.py ./config.py

# Specify the command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
