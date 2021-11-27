<h1 align="center">Pastes crawler</h1>

<p align="center">
<img src="https://img.shields.io/badge/version-1.11.27-brightgreen" />
</p>

---

# Installation

```bash
git clone https://github.com/pictalingo/pastes-crawler.git
cd paster-crawler
sudo nano .env

MONGO_DB=<<YOUR_DB_NAME_HERE>>
MONGO_COLLECTION=<<YOUR_COLLECTION_NAME_HERE>>
MONGO_USER=<<YOUR_USER_HERE>>
MONGO_PASSWORD=<<YOUR_PASSWORD_HERE>>
```
Replace << >> to your variables

## Usage
To run crawler just run:

```bash
docker-compose up
```

---

### File structure

    .
    ├── .dockerignore
    ├── .gitignore
    ├── db                      # Databses connection classes
    │   ├── mongo.py            # Mongo connection class
    │   ├── benchmarks          # Tinydb connection class
    ├── cron                    # Two crons, one every 2 minutes, second every 5 minutes
    ├── extender.py             # Second cron, look for new pastes and extend all data to MongoDB
    ├── finder.py               # First cron runner, finding new pastes in https://pastebin.com
    ├── Dockerfile
    ├── README.md
    └── requiremnts.tx
