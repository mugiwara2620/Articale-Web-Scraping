# %%
import os
import re
import requests
import pandas as pd
from urllib.parse import quote
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# %%
# Load the env keys
load_dotenv()
Guardient_API = os.getenv("GURDIENT-API-KEY")


class ArticaleScraping:
    def __init__(self):
        pass

    def get_the_5_latest_articale_on(self, topic):
        try:
            q_topic = quote(topic)
            # Fixed endpoint URL, parameter names (page-size), and query string formatting
            url = f"https://content.guardianapis.com/search?q={q_topic}&page-size=5&api-key={Guardient_API}"

            response = requests.get(url)
            re_data = response.json()
            articales = re_data["response"]["results"]

            articales_list = {}
            for articale in articales:
                articales_list[articale["webTitle"]] = articale["webUrl"]

            return articales_list

        except Exception as e:
            print(e)

    def articales_by_famous_name(self, famous_name, articale_num):
        try:
            q_famous_name = quote(famous_name)
            folder_name = re.sub(r"\s+", "_", famous_name)

            # Fixed URL query parameters
            url = f"https://content.guardianapis.com/search?q={q_famous_name}&page-size={articale_num}&show-fields=body&api-key={Guardient_API}"

            response = requests.get(url)
            re_data = response.json()

            data = re_data["response"]["results"]
            df = pd.DataFrame(data)

            # Safely handle missing 'fields' or 'body' keys
            df["body"] = df["fields"].apply(
                lambda x: x.get("body", "") if isinstance(x, dict) else ""
            )

            target_dir = os.path.join("saved-articales", f"{folder_name}-articales")
            os.makedirs(target_dir, exist_ok=True)

            for row in df.itertuples():
                title, body = row.webTitle, row.body

                # Clean invalid characters from filenames
                safe_title = re.sub(r'[<>:"/\\|?*]', "", title)
                filename = f"{safe_title}.txt"
                file_path = os.path.join(target_dir, filename)

                soup = BeautifulSoup(body, "html.parser")

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(title + "\n\n\n")
                    for paragraph in soup.find_all("p"):
                        f.write(f"{paragraph.text}\n")

            print(f"Folder name {folder_name} added successfully")

        except Exception as e:
            print(e)
