import sentry_sdk
sentry_sdk.init(
    "https://496e13b789574a81992087e7a5383a3a@o1070296.ingest.sentry.io/6343278",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
from sentry_sdk import capture_exception, capture_message

class MyError(Exception):
    pass

try:
    division_by_zero = 1 / 0
except Exception as e:
    capture_exception(e)

capture_message("Ejecucion terminada con errores")