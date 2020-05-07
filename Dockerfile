FROM python:3.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
# User configuration
ARG USERNAME=webapp
RUN useradd -m -s /bin/bash ${USERNAME}
USER ${USERNAME}
# Expose container ports
EXPOSE 5000
CMD python run.py
