# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/python-3/.devcontainer/base.Dockerfile
# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.11-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:1-${VARIANT}

# Add metadata
LABEL maintainer="Tobías Chavarría <tobias.chavarria.castro@gmail.com>"
LABEL version="1.0"
LABEL description="Python development environment with Poetry for .devcontainers"

# Install Poetry with a specific version
ENV POETRY_VERSION=1.5.1
RUN pip install "poetry==${POETRY_VERSION}"

# Configure Poetry
RUN poetry config virtualenvs.in-project true
