FROM python:3.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
RUN cd app/module/cython && python setup.py build_ext --inplace && cd /code
CMD python run.py
