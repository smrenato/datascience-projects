# from loguru import logger

# logger.debug("That's it, beautiful and simple logging!")
# logger.warning("That's it, beautiful and simple logging!")
# logger.error("That's it, beautiful and simple logging!")
# logger.critical("That's it, beautiful and simple logging!")
# logger.info("That's it, beautiful and simple logging!")


# from sys import stderr
# from loguru import logger

# logger.remove()

# logger.add(
#     sink=stderr,
#     format='{time} <r>{level}</r> <g>{message}</g> {file}',
#     filter=lambda rec: 'senha' not in rec['message'].lower(),
#     level='INFO',
# )

# logger.critical('senha')
# logger.debug('Debug')
# logger.info('Info')
# logger.warning('Warning')

# ## sentry loggs
# from logging import DEBUG
# from loguru import logger
# from sentry_sdk import init

# # To work with senty we need install sentry-sdk
# # from sentry_sdk.integrations.logging import LoggingIntegration, EventHandler


# init(
#    dsn=''
#     integrations=[LoggingIntegration(level=None, event_level=None)]
# )  # Inicia o sentry

# logger.add(
#     EventHandler(level=DEBUG), format="{time} {level} {message}",
# )  # Adiciona o sentry ao loguru

# # Logando
# logger.debug("A")
# logger.info("b")
# logger.error("C", extra=dict(bar=43))
# logger.exception("d")
