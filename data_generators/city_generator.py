from entities.city import City
from entities.virus import Virus
from typing import List
from dataclasses import dataclass


@dataclass
class CityData:
    city_name: City
    virus: Virus
    neighbors: List[City]


class CityGenerator:
    GRAPH = {
        # Blue Virus
        City.SAN_FRANCISCO: CityData(
            City.SAN_FRANCISCO,
            Virus.BLUE,
            [City.TOKYO, City.MANILA, City.LOS_ANGELES, City.CHICAGO],
        ),
        City.CHICAGO: CityData(
            City.CHICAGO,
            Virus.BLUE,
            [City.SAN_FRANCISCO, City.LOS_ANGELES, City.MEXICO_CITY, City.ATLANTA, City.MONTREAL],
        ),
        City.ATLANTA: CityData(
            City.ATLANTA,
            Virus.BLUE,
            [City.CHICAGO, City.WASHINGTON, City.MIAMI]),
        City.MONTREAL: CityData(
            City.MONTREAL,
            Virus.BLUE,
            [City.CHICAGO, City.WASHINGTON, City.NEW_YORK],
        ),
        City.NEW_YORK: CityData(
            City.NEW_YORK,
            Virus.BLUE,
            [City.MONTREAL, City.WASHINGTON, City.LONDON, City.MADRID],
        ),
        City.WASHINGTON: CityData(
            City.WASHINGTON,
            Virus.BLUE,
            [City.ATLANTA, City.MIAMI, City.MONTREAL, City.NEW_YORK],
        ),
        City.LONDON: CityData(
            City.LONDON,
            Virus.BLUE,
            [City.NEW_YORK, City.MADRID, City.PARIS, City.ESSEN],
        ),
        City.MADRID: CityData(
            City.MADRID,
            Virus.BLUE,
            [City.SAO_PAULO, City.NEW_YORK, City.LONDON, City.PARIS, City.ALGIERS],
        ),
        City.PARIS: CityData(
            City.PARIS,
            Virus.BLUE,
            [City.LONDON, City.MADRID, City.ESSEN, City.ALGIERS, City.MILAN],
        ),
        City.ESSEN: CityData(
            City.ESSEN,
            Virus.BLUE,
            [City.LONDON, City.PARIS, City.MILAN, City.ST_PETERSBURG],
        ),
        City.MILAN: CityData(
            City.MILAN,
            Virus.BLUE,
            [City.ESSEN, City.PARIS, City.ISTANBUL],
        ),
        City.ST_PETERSBURG: CityData(
            City.ST_PETERSBURG,
            Virus.BLUE,
            [City.ESSEN, City.ISTANBUL, City.MOSCOW],
        ),

        # Yellow Virus
        City.LOS_ANGELES: CityData(
            City.LOS_ANGELES,
            Virus.YELLOW,
            [City.SAN_FRANCISCO, City.SYDNEY, City.MEXICO_CITY, City.CHICAGO],
        ),
        City.MEXICO_CITY: CityData(
            City.MEXICO_CITY,
            Virus.YELLOW,
            [City.LOS_ANGELES, City.CHICAGO, City.MIAMI, City.LIMA, City.BOGOTA],
        ),
        City.MIAMI: CityData(
            City.MIAMI,
            Virus.YELLOW,
            [City.MEXICO_CITY, City.ATLANTA, City.WASHINGTON, City.BOGOTA],
        ),
        City.BOGOTA: CityData(
            City.BOGOTA,
            Virus.YELLOW,
            [City.MIAMI, City.MEXICO_CITY, City.LIMA, City.BUENOS_AIRES],
        ),
        City.LIMA: CityData(
            City.LIMA,
            Virus.YELLOW,
            [City.MEXICO_CITY, City.BOGOTA, City.SANTIAGO],
        ),
        City.SANTIAGO: CityData(
            City.SANTIAGO,
            Virus.YELLOW,
            [City.LIMA],
        ),
        City.BUENOS_AIRES: CityData(
            City.BUENOS_AIRES,
            Virus.YELLOW,
            [City.BOGOTA, City.SAO_PAULO],
        ),
        City.SAO_PAULO: CityData(
            City.SAO_PAULO,
            Virus.YELLOW,
            [City.BOGOTA, City.BUENOS_AIRES, City.LAGOS, City.MADRID],
        ),
        City.LAGOS: CityData(
            City.LAGOS,
            Virus.YELLOW,
            [City.SAO_PAULO, City.KINSHASA, City.KHARTOUM],
        ),
        City.KHARTOUM: CityData(
            City.KHARTOUM,
            Virus.YELLOW,
            [City.LAGOS, City.KINSHASA, City.JOHANNESBURG, City.CAIRO],
        ),
        City.KINSHASA: CityData(
            City.KINSHASA,
            Virus.YELLOW,
            [City.LAGOS, City.KHARTOUM, City.JOHANNESBURG],
        ),
        City.JOHANNESBURG: CityData(
            City.JOHANNESBURG,
            Virus.YELLOW,
            [City.KINSHASA, City.KHARTOUM],
        ),

        # Black Virus
        City.CAIRO: CityData(
            City.CAIRO,
            Virus.BLACK,
            [City.KHARTOUM, City.ALGIERS, City.ISTANBUL, City.BAGHDAD, City.RIYADH],
        ),
        City.ALGIERS: CityData(
            City.ALGIERS,
            Virus.BLACK,
            [City.MADRID, City.PARIS, City.ISTANBUL, City.CAIRO],
        ),
        City.ISTANBUL: CityData(
            City.ISTANBUL,
            Virus.BLACK,
            [City.ALGIERS, City.CAIRO, City.BAGHDAD, City.MILAN, City.ST_PETERSBURG, City.MOSCOW],
        ),
        City.MOSCOW: CityData(
            City.MOSCOW,
            Virus.BLACK,
            [City.ST_PETERSBURG, City.ISTANBUL, City.TEHRAN],
        ),
        City.BAGHDAD: CityData(
            City.BAGHDAD,
            Virus.BLACK,
            [City.ISTANBUL, City.CAIRO, City.RIYADH, City.KARACHI, City.TEHRAN],
        ),
        City.RIYADH: CityData(
            City.RIYADH,
            Virus.BLACK,
            [City.CAIRO, City.BAGHDAD, City.KARACHI],
        ),
        City.TEHRAN: CityData(
            City.TEHRAN,
            Virus.BLACK,
            [City.MOSCOW, City.BAGHDAD, City.KARACHI, City.DELHI],
        ),
        City.KARACHI: CityData(
            City.KARACHI,
            Virus.BLACK,
            [City.TEHRAN, City.BAGHDAD, City.RIYADH, City.DELHI, City.MUMBAI],
        ),
        City.MUMBAI: CityData(
            City.MUMBAI,
            Virus.BLACK,
            [City.KARACHI, City.DELHI, City.CHENNAI],
        ),
        City.DELHI: CityData(
            City.DELHI,
            Virus.BLACK,
            [City.TEHRAN, City.KARACHI, City.MUMBAI, City.CHENNAI, City.KOLKATA],
        ),
        City.CHENNAI: CityData(
            City.CHENNAI,
            Virus.BLACK,
            [City.MUMBAI, City.DELHI, City.KOLKATA, City.BANGKOK, City.JAKARTA],
        ),
        City.KOLKATA: CityData(
            City.KOLKATA,
            Virus.BLACK,
            [City.DELHI, City.CHENNAI, City.BANGKOK, City.HONG_KONG],
        ),

        # Red Virus
        City.BANGKOK: CityData(
            City.BANGKOK,
            Virus.RED,
            [City.KOLKATA, City.CHENNAI, City.JAKARTA, City.HONG_KONG, City.HO_CHI_MINH_CITY],
        ),
        City.JAKARTA: CityData(
            City.JAKARTA,
            Virus.RED,
            [City.CHENNAI, City.BANGKOK, City.HO_CHI_MINH_CITY, City.SYDNEY],
        ),
        City.BEIJING: CityData(
            City.BEIJING,
            Virus.RED,
            [City.SHANGHAI, City.SEOUL],
        ),
        City.SHANGHAI: CityData(
            City.SHANGHAI,
            Virus.RED,
            [City.BEIJING, City.SEOUL, City.TOKYO, City.TAIPEI, City.HONG_KONG],
        ),
        City.HONG_KONG: CityData(
            City.HONG_KONG,
            Virus.RED,
            [City.SHANGHAI, City.TAIPEI, City.KOLKATA, City.BANGKOK, City.HO_CHI_MINH_CITY, City.MANILA],
        ),
        City.HO_CHI_MINH_CITY: CityData(
            City.HO_CHI_MINH_CITY,
            Virus.RED,
            [City.JAKARTA, City.BANGKOK, City.HONG_KONG, City.MANILA],
        ),
        City.SEOUL: CityData(
            City.SEOUL,
            Virus.RED,
            [City.SHANGHAI, City.BEIJING, City.TOKYO],
        ),
        City.TOKYO: CityData(
            City.TOKYO,
            Virus.RED,
            [City.SHANGHAI, City.SEOUL, City.OSAKA, City.SAN_FRANCISCO],
        ),
        City.TAIPEI: CityData(
            City.TAIPEI,
            Virus.RED,
            [City.SHANGHAI, City.HONG_KONG, City.OSAKA, City.MANILA],
        ),
        City.OSAKA: CityData(
            City.OSAKA,
            Virus.RED,
            [City.TOKYO, City.TAIPEI],
        ),
        City.MANILA: CityData(
            City.MANILA,
            Virus.RED,
            [City.SAN_FRANCISCO, City.HO_CHI_MINH_CITY, City.SYDNEY, City.TAIPEI, City.HONG_KONG],
        ),
        City.SYDNEY: CityData(
            City.SYDNEY,
            Virus.RED,
            [City.JAKARTA, City.MANILA, City.LOS_ANGELES],
        ),
    }
