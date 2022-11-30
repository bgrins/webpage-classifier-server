FROM bgrins/webpage-classifier-base:0.0.1
COPY . .
RUN pip install -r requirements.txt
CMD uvicorn main:app --host 0.0.0.0 --port $PORT