import sentry_sdk
from sentry_sdk import capture_exception, capture_message
sentry_sdk.init(
    "https://06fd74fbcf654c0c9e38d9107c40ef23@o865511.ingest.sentry.io/5975318",
    traces_sample_rate=1.0
)

for _ in range(150):
    try:
        raise ValueError("Se te ha jodio")
    except Exception as e:
        capture_exception(e)

# try:
#     raise TypeError("Error de test")
# except Exception as e:
#     print("Exception capturada")
#     capture_exception(e)

# for i in range(-10,11):
#     if i == 0:
#         continue
#     try:
#         print(1/i)
#     except Exception as e:
#         capture_exception(e)
#         print("Not possible")

# try:
#     print(non_exiting_var)
# except Exception as e:
#     capture_exception(e)
#     print("OK..")

# capture_message("Scrip Executed")