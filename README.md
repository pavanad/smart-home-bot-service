# Smart Home - Bot Service

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

Service responsible for receiving user messages through a Telegram bot, interacting with the Grace assistant, and providing responses and functionalities through the Telegram platform.

## Features

- **Telegram Bot Integration:** Receives user messages through a Telegram bot.
- **Grace Assistant Interaction:** Interacts with the Grace assistant to process user requests.
- **Text and Voice Message Handling:** Supports both text and voice messages from users.
- **Response Generation:** Provides responses and functionalities through the Telegram platform.

## Installation

You can install this project using [poetry](https://python-poetry.org/):

```bash
poetry install
```

## Credentials

Create file `.env` in root path (development environment)
```bash
GRACE_SERVICE_URL=your_grace_service_url
TELEGRAM_TOKEN=your_telegram_token
```

## Usage

```bash
make run
```

### Running with Docker

**Development Environment**

```bash
docker compose -f "docker-compose.dev.yml" up -d --build 
```

**Production Environment**

Load the variables from the .env file into the environment:
```bash
export $(cat .env | xargs)
```

```bash
docker compose -f "docker-compose.yml" up -d --build 
```

## Contributing

Contributions to BeeGen are welcome! If you find a bug, have a feature request, or want to improve the code, please submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for more information.