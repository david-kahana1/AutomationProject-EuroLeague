import os

IS_HEADLESS = os.getenv("CI") == "true" #for GitHub CI/CD, in locals run is "False"

BROWSER = "Chromium" #also support 'Firefox'

BASE_URL = "https://www.euroleaguebasketball.net/euroleague/"

# These settings allow the CI pipeline to run the tests successfully-
# without being blocked by the website's security layer:

BROWSER_ARGS = \
    {
    "channel": "chrome",
    "ignore_default_args": ["--enable-automation"],
    "args":
      [
        "--disable-blink-features=AutomationControlled",
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--use-gl=angle",
        "--use-angle=swiftshader",
        "--disable-infobars",
        "--window-position=0,0"
      ]
    }

CONTEXT_SETTINGS = \
  {
    "viewport": {"width": 1920, "height": 1080},
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "locale": "en-US",
    "timezone_id": "Europe/Paris"
  }



#Test Data:

TEAMS = [
  {
    "team_name": "fc-bayern-munich",
    "link_name": "FC Bayern Munich"
  },
  {
    "team_name": "anadolu-efes-istanbul",
    "link_name": "Anadolu Efes Istanbul"
  },
  {
    "team_name": "armani-olimpia-milan",
    "link_name": "Armani Olimpia Milan"
  },
  {
    "team_name": "besiktas-istanbul",
    "link_name": "Besiktas Istanbul"
  },
  {
    "team_name": "crvena-zvezda-meridianbet",
    "link_name": "Crvena Zvezda Meridianbet Belgrade"
  },
  {
    "team_name": "dubai-basketball",
    "link_name": "Dubai Basketball"
  },
  {
    "team_name": "fc-barcelona",
    "link_name": "FC Barcelona"
  },
  {
    "team_name": "fenerbahce-beko-istanbul",
    "link_name": "Fenerbahce Istanbul"
  },
  {
    "team_name": "hapoel-ibi-tel-aviv",
    "link_name": "Hapoel IBI Tel Aviv"
  },
  {
    "team_name": "kosner-baskonia-vitoria",
    "link_name": "Kosner Baskonia Vitoria-Gasteiz"
  },
  {
    "team_name": "ldlc-asvel-villeurbanne",
    "link_name": "LDLC ASVEL Villeurbanne"
  },
  {
    "team_name": "maccabi-rapyd-tel-aviv",
    "link_name": "Maccabi Rapyd Tel Aviv"
  },
  {
    "team_name": "olympiacos-piraeus",
    "link_name": "Olympiacos Piraeus"
  },
  {
    "team_name": "panathinaikos-aktor-athens",
    "link_name": "Panathinaikos AKTOR Athens"
  },
  {
    "team_name": "paris-basketball",
    "link_name": "Paris Basketball"
  },
  {
    "team_name": "partizan-mozzart-bet-belgrade",
    "link_name": "Partizan Mozzart Bet Belgrade"
  },
  {
    "team_name": "real-madrid",
    "link_name": "Real Madrid"
  },
  {
    "team_name": "valencia-basket",
    "link_name": "Valencia Basket"
  },
  {
    "team_name": "virtus-bologna",
    "link_name": "Virtus Bologna"
  },
  {
    "team_name": "zalgiris-kaunas",
    "link_name": "Zalgiris Kaunas"
  }
]

