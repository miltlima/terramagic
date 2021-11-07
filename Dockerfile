FROM python:3-alpine

ARG TERRAFORM_VERSION="1.0.7"

LABEL maintainer="miltlima <milton.lima@outlook.com>"
LABEL terraform_version=${TERRAFORM_VERSION}

ENV DEBIAN_FRONTEND=noninteractive
ENV TERRAFORM_VERSION=${TERRAFORM_VERSION}

RUN apk add --update bash curl unzip zip

RUN pip install terramagic \
    && curl -LO https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && rm *.zip

CMD ["/bin/bash"]