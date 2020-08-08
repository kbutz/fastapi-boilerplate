FROM alpine:latest

RUN apk update && apk add --no-cache build-base python3 python3-dev py3-pip py3-wheel

COPY . /fastapi-boilerplate
WORKDIR /fastapi-boilerplate

RUN pip install --upgrade pip && pip install -r requirements.txt

#RUN addgroup -S fastapi && adduser -S -G fastapi fastapi
#USER fastapi
#
#RUN echo "User $(whoami) running from $PWD" #with premissions: $(sudo -l)

EXPOSE 80

# TODO: Need to run from gunicorn next
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]