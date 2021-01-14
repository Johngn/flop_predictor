from alpine:latest

RUN apk add --no-cache python3-dev py3-pip

WORKDIR /app

COPY . /app

RUN set -x \
	&& apk add --no-cache build-base \
	&& apk add --no-cache libexecinfo-dev
RUN pip install -U pip
RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000 

ENTRYPOINT ["python3"]
CMD ["main.py"]

