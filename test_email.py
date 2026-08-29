from src.email.email_digest import EmailDigest
from src.articale_web_scraping.articale_web_scraping import ArticaleScraping

# get_5_articale_on_ai = ArticaleScraping().get_the_5_latest_articale_on(
#     "artificial intelligence"
# )
# print(get_5_articale_on_ai)

test_sender = EmailDigest().send_lateat_5_articales_on("artificial intelligence")
test_sender()
