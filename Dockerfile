FROM python:3.11
WORKDIR /D:/Sanskruti/Log_Monitoring_Microservice
COPY . . 
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python","log_monitoring.py"]