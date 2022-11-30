FROM python:3.10-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
ENV IS_DOCKER=true
ENV WARMUP_MODEL=true

# Run with a non-root user
RUN useradd -ms /bin/bash webuser
WORKDIR /home/webuser
USER webuser
ENV PATH="/home/webuser/.local/bin:${PATH}"

# Run a simple script once to download the model
RUN pip install homepage2vec==0.0.3rc0
COPY model_warmup.py .
RUN python ./model_warmup.py

RUN echo "Base image setup"
