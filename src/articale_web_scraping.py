# %%
import os
import re as r
import requests
import pandas as pd
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# %%
# Load the env keys
load_dotenv()
Guardient_API = os.getenv("GURDIENT-API-KEY")


class ArticaleScraping:
    def __init__(self):
        pass

    def articales_by_famous_name(self, famous_name, articale_num):

        try:
            q_famous_name = r.sub(" ", "%20", famous_name)
            folder_name = r.sub(" ", "_", famous_name)
            url = f"https://content.guardianapis.com/search?q={q_famous_name}?&api-key={Guardient_API}&type=article&pageSize={articale_num}&show-fields=body"

            # %% Get the response
            response = requests.get(url)
            re = response.json()
            # %% Print data
            data = re["response"]["results"]
            df = pd.DataFrame(data)

            def getBody(json):
                return json["body"]

            df["body"] = df["fields"].apply(getBody)
            df_body_w_title = pd.DataFrame()

            df_body_w_title["body"] = df["body"]
            df_body_w_title["title"] = df["webTitle"]

            if os.path.isdir(f"saved-articales/{folder_name}-articales"):
                print("dir already exist")
            else:
                os.mkdir(f"saved-articales/{folder_name}-articales")
            for row in df_body_w_title.itertuples():
                title, body = row.title, row.body

                soup = BeautifulSoup(body, "html.parser")
                filename = f"{title}.txt"

                # NETTOYAGE : Remplace les caractères interdits (< > : " / \ | ? *) par un tiret du bas "_"
                filename = r.sub(r'[<>:"/\\|?*]', "", filename)

                file_path = os.path.join(
                    f"saved-articales/{folder_name}-articales", filename
                )
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(row.title)

                    f.write("\n" * 3)

                    for paragraph in soup.find_all("p"):
                        f.writelines(f"{paragraph.text}\n")
            print(f"Folder name {folder_name} added successfully")

        except Exception as e:
            print(e)
