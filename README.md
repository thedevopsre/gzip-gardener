# gzip-gardener

`gzip-gardener` is a Dockerized tool designed for automated cleanup of gzip backup files. It ensures your backup directory maintains only the most recent backups based on a specified retention policy.

## Features

- **Automated Cleanup**: Automatically deletes gzip backup files older than a specified retention period.
- **Customizable Settings**: Configure your backup path and retention period through environment variables.
- **Dockerized Solution**: Easy to deploy and run in a Docker environment.

## Configuration

### Environment Variables

- `BACKUP_PATH`: Specifies the path inside the container where the backup files are stored.
- `BACKUP_RETENTION`: Defines the number of recent backup files to retain.

## Usage

### Setting Up with Docker Compose

1. **Create a `docker-compose.yml` File**

   Create a file with the following content:

   ```yaml
   version: '3.8'
   services:
     backup-cleaner:
       image: devopsdarkmaster/gzip-gardener:v1.0.0
       environment:
         BACKUP_PATH: "/backups"
         BACKUP_RETENTION: "7"
       volumes:
         - /path/to/your/local/backups:/backups

### Running the service

`docker-compose up -d`