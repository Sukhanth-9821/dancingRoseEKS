FROM python:3
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirement.txt
COPY app.py .
CMD ["python","./app.py"]
EXPOSE 8090