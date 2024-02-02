FROM python:3.9-slim

WORKDIR /app

RUN apt-get update  && apt-get upgrade -y

RUN apt-get install build-essential -y

RUN apt-get install libtesseract-dev -y

RUN apt-get install poppler-utils -y

RUN apt-get install wget -y

RUN apt-get install libpq-dev -y

RUN apt-get install exiftool -y

RUN wget --no-check-certificate https://dl.xpdfreader.com/xpdf-tools-linux-4.04.tar.gz && tar -xvf xpdf-tools-linux-4.04.tar.gz

RUN cp xpdf-tools-linux-4.04/bin64/pdftotext /usr/local/bin

COPY ./requirements.txt .

RUN pip install --upgrade pip 

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app .

CMD [ "bash", "start.sh"]