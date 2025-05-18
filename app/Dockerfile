FROM python:3.12-slim

RUN useradd --system --create-home --shell /bin/sh appuser

RUN pip install --no-cache-dir uv

USER appuser
WORKDIR /home/appuser/app

COPY --chown=appuser:appuser pyproject.toml uv.lock ./
RUN uv sync

COPY --chown=appuser:appuser src/ .

ENV PYTHONPATH=/home/appuser/app

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
