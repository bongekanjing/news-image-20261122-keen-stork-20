"""The 22 November 2026 story list.

Each item is one record with the fields the page needs:
  region   - a geographic place, never a topic (the 21 Nov page was caught counting
             "Science" and "Business" as regions; the 20 Nov heat quoted that as a defect)
  kicker   - the short slug printed in the coloured bar over a card, e.g. "GULF: STRIKES"
  place    - the dateline shown in the kicker's second line
  head     - the headline, front-loaded and short so it survives a 300px thumbnail
  dek      - one or two sentences of what actually happened
  source   - the outlet(s) that reported it; every item carries one
  kind     - which flat vector drawing the card gets, for the 13 illustrations
  lon,lat  - where it happened, for the numbered pin on the map

Tier assignment is by consequence, not by order of appearance: the first three are the
leads, the next ten are the illustrated medium cards, the rest run as one-line briefs.
That three-tier density is how the page shows rank without a single word of hype.
"""

# (region, kicker, place, head, dek, source, kind, lon, lat, tier)
STORIES = [
    # ================= LEADS: the three biggest stories of the day =================
    ("MIDDLE EAST", "GULF: STRIKES", "Hormuz & Bahrain", "War",
     "Tankers hit off Hormuz; Iran strikes Bahrain",
     "A fourth tanker was struck 11 nautical miles off Khasab, Oman, with no casualties. "
     "The IRGC said it hit US positions at al-Riffa and Awali; Bahrain reported a fire.",
     "Reuters, UKMTO, Al Jazeera", "strait", 50.9, 26.3, 1),

    ("LATIN AMERICA", "PERU: QUAKE 6.7", "Junin, Peru", "Earthquake",
     "Magnitude 6.7 quake shakes Peru's Andes",
     "The USGS put the epicentre near Junin at 108 km deep. It was felt in Lima; "
     "no damage was reported. The quake struck late on Saturday and was reported on Sunday.",
     "USGS, AP, Reuters", "quake", -75.0, -11.15, 1),

    ("EUROPE", "COP31: OVERTIME", "Antalya, Turkiye", "Climate",
     "COP31 runs into overtime with no deal",
     "Nearly 200 countries remain split after a revised draft dropped all mention of "
     "fossil fuels. Talks had been due to close on Friday.",
     "Reuters, AFP, DW", "summit", 30.7, 36.9, 1),

    # ================= MEDIUM CARDS: ten more, each drawn =================
    ("EUROPE", "POLAND: DEBRIS", "Warsaw", "Security",
     "NATO vows to defend Poland",
     "Two Russian missiles and a suspected drone came down on Polish soil; Warsaw called "
     "it a likely provocation timed to exercises.",
     "PAP, Reuters", "missile", 21.0, 52.2, 2),

    ("LATIN AMERICA", "SINALOA: CAPTURE", "Guasave, Mexico", "Justice",
     "Mexico seizes 'El Chapo Isidro'",
     "Fausto Isidro Meza Flores and two other Sinaloa leaders were detained; gunfights and "
     "burned buses followed and schools closed.",
     "Reuters, Sky News", "police", -108.5, 25.4, 2),

    ("AFRICA", "NIGERIA: BOAT", "Bayelsa state", "Disaster",
     "24 mourners drown as boat capsizes",
     "The overcrowded vessel was bound for a funeral when its engine failed, police said.",
     "Reuters, The Independent", "boat", 6.3, 4.9, 2),

    ("ASIA", "EU-INDONESIA: DEAL", "Jakarta & Brussels", "Trade",
     "EU, Indonesia sign trade deal",
     "The pact cuts tariffs and opens investment as Brussels seeks to offset US levies.",
     "Reuters, Al Jazeera", "flags", 106.8, -6.2, 2),

    ("ASIA", "MANIPUR: ALCOHOL", "Imphal, India", "Health",
     "11 die after tainted liquor",
     "More than 180 were hospitalised in Manipur; the chief minister ordered an inquiry "
     "into the locally made alcohol.",
     "Reuters", "bottle", 93.9, 24.8, 2),

    ("MIDDLE EAST", "GAZA: FLOODS", "Khan Younis", "Aid",
     "Floods swamp Gaza tent camps",
     "Aid groups say about 150,000 tents are held at the border and camp drainage has failed.",
     "Reuters, AP", "tent", 34.3, 31.3, 2),

    ("EUROPE", "TWICKENHAM: RUGBY", "London", "Sport",
     "England beat All Blacks 37-12",
     "Five tries gave England back-to-back wins over the All Blacks, their best run "
     "against them in two decades.",
     "ABC News, BBC", "rugby", -0.34, 51.45, 2),

    ("ASIA", "JAPAN: PRICES", "Tokyo", "Markets",
     "Japan core inflation tops target",
     "Core prices rose on energy and rice; the Bank of Japan is expected to hold rates "
     "this week.",
     "Reuters", "market", 139.7, 35.7, 2),

    ("AFRICA", "SUDAN: FAMINE", "El Fasher, Darfur", "Aid",
     "Famine warning widens to 3 states",
     "Aid agencies say fighting around El Fasher has cut the last road route for supplies.",
     "Reuters", "aid", 25.3, 13.6, 2),

    ("ASIA", "NEPAL-INDIA: VISIT", "New Delhi", "Diplomacy",
     "Nepal PM starts India visit",
     "His first trip abroad since taking office; talks with Modi cover energy, "
     "connectivity and the Kalapani border dispute.",
     "Nepal MFA, Indian MEA", "handshake", 77.2, 28.6, 2),

    # ================= BRIEFS: the rest, one line each =================
    ("MIDDLE EAST", "IRAQ: FIRE", "Hartha, Basra", "Energy",
     "Basra power station fire kills 4",
     "Civil defence brought the blaze north of Basra under control; the toll may rise.",
     "INA, Reuters", None, 47.8, 30.5, 3),

    ("ASIA", "IRAN: TALKS", "Tehran", "Diplomacy",
     "Qatar mediates as US weighs strike",
     "A Qatari delegation held talks; Trump has deferred any decision until after New Year.",
     "Reuters", None, 51.4, 35.7, 3),

    ("EUROPE", "RUSSIA: BALTIC", "Baltic", "Security",
     "Russian ship ablaze in Baltic",
     "Finland says Ukraine was probably behind the attack on Sparta II; all 16 crew escaped.",
     "Finnish Border Guard, Reuters", None, 27.0, 60.2, 3),

    ("EUROPE", "EU: VISAS", "Copenhagen", "Security",
     "Denmark seeks EU curbs on Russians",
     "Copenhagen says it foiled a Russian plot to kill a US-Ukrainian rapper in September.",
     "Reuters", None, 12.6, 55.7, 3),

    ("EUROPE", "EU: BUDGET", "Brussels", "Economy",
     "EU chair proposes EUR 40bn cut",
     "Antonio Costa suggests a digital tax to help fund it, taking the total to EUR 1.582trn.",
     "Reuters", None, 4.4, 50.8, 3),

    ("EUROPE", "FRANCE: MARCHES", "France", "Labour",
     "France, Portugal see cost-of-living marches",
     "Turnout fell from a week earlier; Portugal's CGTP marched through heavy rain.",
     "Reuters", None, 2.35, 48.86, 3),

    ("EUROPE", "UKRAINE: STRIKE", "Kryvyi Rih", "War",
     "Missile kills 2 in Zelensky's city",
     "The ballistic attack wounded dozens; Zelensky restated Ukraine's aim to join NATO.",
     "France 24, Reuters", None, 33.4, 47.9, 3),

    ("EUROPE", "SOUTH AFRICA: DEATH", "Johannesburg", "Obituary",
     "Ex-UN Women chief dies at 71",
     "South Africa's first woman deputy president led UN Women from 2013 to 2021.",
     "Reuters", None, 28.2, -25.7, 3),

    ("ASIA", "VIETNAM: LAND", "Hanoi", "Politics",
     "Vietnam speeds land seizure",
     "Parliament approved faster expropriation, cutting farmers' leverage over delays.",
     "Reuters", None, 105.8, 21.0, 3),

    ("ASIA", "UN: ROBOTS", "Geneva", "Security",
     "Killer-robot talks end without treaty",
     "Russia blocked a negotiating mandate; states agreed only to keep talking toward 2028.",
     "Reuters, Kyodo", None, 6.14, 46.2, 3),

    ("ASIA", "INDIA: EXAMS", "New Delhi", "Education",
     "India passes law on national exams",
     "The bill follows paper leaks and AI-assisted cheating that forced mass re-tests.",
     "PTI", None, 77.2, 28.6, 3),

    ("ASIA", "JAPAN: SNOW", "Fukushima", "Weather",
     "1,000 cut off by snow in Fukushima",
     "Fallen trees blocked roads near Kitashiobara; about 900 residents and 500 visitors "
     "are isolated.",
     "Kyodo", None, 140.1, 37.65, 3),

    ("AFRICA", "KENYA: PROTESTS", "Nairobi", "Economy",
     "Kenya police tear-gas protesters",
     "Demonstrators demanded lower fuel taxes; the government says the budget leaves no room.",
     "Reuters", None, 36.8, -1.3, 3),

    ("AFRICA", "SINALOA: FALLOUT", "Culiacan", "Security",
     "11 killed after Sinaloa capture",
     "Buses burned and schools closed as the security cabinet flew in.",
     "Sky News, Reuters", None, -107.4, 24.8, 3),

    ("NORTH AMERICA", "NVIDIA: PROBE", "Washington", "Markets",
     "SEC examines Nvidia accounting",
     "Enforcement staff are said to be scrutinising potential accounting issues.",
     "Reuters", None, -77.0, 38.9, 3),

    ("NORTH AMERICA", "CANADA: DEFENCE", "Ottawa", "Security",
     "Canada sees no shift in US ties",
     "David McGuinty said he had not seen a reported memo imposing new constraints.",
     "Reuters", None, -75.7, 45.4, 3),

    ("OCEANIA", "MELBOURNE: T20", "Melbourne", "Sport",
     "Australia chase 188 to win first T20",
     "Nikhil Chaudhary made 66 from 38 balls at the MCG.",
     "SBS News", None, 144.98, -37.82, 3),

    ("OCEANIA", "TASMANIA: SHOOTING", "Flinders Island", "Crime",
     "Officer shot on Flinders Island",
     "He is in a serious but stable condition; a man was found dead nearby and three "
     "teenagers arrested.",
     "SBS News, ABC", None, 148.0, -40.0, 3),
]

REGION_ORDER = ["EUROPE", "ASIA", "MIDDLE EAST", "AFRICA",
                "LATIN AMERICA", "NORTH AMERICA", "OCEANIA"]

DAY_LONG = "Sunday 22 November 2026"
