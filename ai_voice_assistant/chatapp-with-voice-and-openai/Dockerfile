FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Optional: Copy certificates if necessary for development environments
# REMOVE THIS WHEN DEPLOYING TO PRODUCTION
COPY certs/rootCA.crt /usr/local/share/ca-certificates/rootCA.crt
RUN chmod 644 /usr/local/share/ca-certificates/rootCA.crt && \
    update-ca-certificates

# Environment variables for OpenAI and SSL configuration
ENV OPENAI_API_KEY=
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

CMD ["python", "-u", "server.py"]
