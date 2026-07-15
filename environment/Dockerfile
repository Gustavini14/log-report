# Pinned stable Python bookworm image with immutable sha256 digest
FROM python:3.11-slim-bookworm@sha256:75a17dd6f00b277975715fc094c4a1570d512708de6bb4c5dc130814813ebfe4

RUN pip install --no-cache-dir \
    pytest==8.4.1 \
    pytest-json-ctrf==0.3.5

WORKDIR /app

# Copy ONLY the target log file. NO leaked solutions.
COPY access.log /app/access.log
