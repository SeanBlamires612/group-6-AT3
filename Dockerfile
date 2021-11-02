FROM python:3.8.2
WORKDIR /App
ENV PYTHONPATH "${PYTHONPATH}:/src"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY /src .
COPY /App .
CMD ["streamlit", "run", "Streamlit_app.py"]