FROM ubuntu:bionic-20210930

ARG TERRAFORM_VERSION="1.0.7"
ARG TERRAMAGIC_VERSION="0.1.0"

LABEL terraform_version=${TERRAFORM_VERSION}
LABEL terramagic_version=${TERRAMAGIC_VERSION}

ENV TERRAFORM_VERSION=${TERRAFORM_VERSION}
ENV TERRAMAGIC_VERSION=${TERRAMAGIC_VERSION}

RUN apt-get update \
    && apt-get install -y curl python3 python3-pip unzip \
    && pip install --upgrade terramagic==${TERRAMAGIC_VERSION} \
    && curl -LO https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && unzip '*.zip' -d /usr/local/bin \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* *.zip

CMD ["/bin/bash"]