# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Set environment variables for the PostgreSQL container
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=psql
ENV POSTGRES_DB=cicd

# Optionally, you can include additional configuration or initialization scripts.
# For example, if you have a custom SQL initialization script, you can copy it into the container.

# COPY init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port (5432) for external connections
EXPOSE 5432


