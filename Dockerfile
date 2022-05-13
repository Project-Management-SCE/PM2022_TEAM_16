FROM python:3.7
WORKDIR /PM2022_TEAM_16
ADD . /PM2022_TEAM_16
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django==2.1.15
RUN pip install django_jenkins
RUN	pip install requests
RUN	pip install selenium
RUN	pip install chromedriver_py
RUN pip install mysql
CMD ["python","manage.py","runserver","0.0.0.0:$PORT"]

