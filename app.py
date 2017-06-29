import logging.config
from app import app


LOG_LEVEL = logging.INFO

logging.config.dictConfig(dict(
    version=1,
    disable_existing_loggers=False,
    formatters={
        'f': {
            'format': '%(asctime)s - %(process)d - %(name)s:%(lineno)d - %(levelname)-8s - %(message)s'}},
    handlers={
        'h': {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': LOG_LEVEL,
        }
    },
    root={
        'handlers': ['h'],
        'level': LOG_LEVEL,
    },
))

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    app.run()
