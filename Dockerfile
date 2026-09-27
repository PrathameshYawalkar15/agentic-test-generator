FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ src/

# step_definitions/ is populated at container *runtime* by
# src/generate_steps.py (it reads whatever ends up in features/, which
# itself is only generated after the container starts). Copying it at
# build time (`COPY step_definitions/ step_definitions/`) fails the
# build outright if that directory isn't committed to the repo -- which
# it usually won't be, since it's auto-generated. Just ensure the
# directory exists; its contents get written later.
RUN mkdir -p requirements features reports step_definitions

ENV OLLAMA_HOST=http://ollama:11434
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "-m", "pytest", "features/", "-v"]
