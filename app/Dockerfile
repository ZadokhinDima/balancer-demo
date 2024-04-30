FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install flask argparse
CMD ["python", "app.py", "--server_name", "App Server"]