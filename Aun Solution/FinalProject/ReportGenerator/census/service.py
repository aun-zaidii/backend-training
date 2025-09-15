import os
from dataclasses import fields
from typing import Dict, List, Optional, Union

import requests

from .models import CensusCounty, CensusDetail, CensusState
from .types import CensusData

api: Optional[str] = os.getenv("API")
variables: str = (
    "NAME,DP05_0001E,DP05_0017E,DP03_0062E,DP03_0128PE,DP03_0009PE,DP04_0001E,DP04_0046PE,DP02_0068PE,DP05_0002E,DP05_0003E,DP05_0077PE,DP05_0078PE,DP05_0080PE,DP05_0071PE,DP02_0094PE,DP02_0111PE,DP02_0016E,DP02_0017E,DP02_0019PE,DP02_0022PE,DP02_0067PE,DP04_0047PE,DP04_0019E,DP04_0045E,DP04_0134E,DP04_0101E,DP03_0063E,DP03_0021PE,DP03_0022PE,DP03_0024PE,DP03_0096PE,DP02_0072PE"
)
keys: List[str] = [
    "name",
    "total_population",
    "median_age",
    "median_household_income",
    "poverty_rate",
    "unemployment_rate",
    "total_houses",
    "home_ownership_rate",
    "bachelors_or_higher_degree_pct",
    "male_population",
    "female_population",
    "white_alone_pct",
    "black_alone_pct",
    "asian_alone_pct",
    "hispanic_latino_pct",
    "foreign_born_pct",
    "non_english_home_pct",
    "avg_household_size",
    "avg_family_size",
    "married_couple_families_pct",
    "single_parent_families_pct",
    "hs_or_higher_pct",
    "renter_occupied_pct",
    "median_year_built",
    "median_rooms",
    "median_gross_rent",
    "median_owner_costs_mortgage",
    "median_household_income",
    "workers_public_transport_pct",
    "workers_car_pct",
    "workers_home_pct",
    "health_insurance_coverage_pct",
    "disability_pct",
    "state",
    "county_no",
]


def request_data_for_single_year(
    year: int,
) -> List[CensusData]:
    if year == 2020:
        raise ValueError(
            "ACS 1-Year Profile estimates were not published for 2020 due to COVID-19."
        )
    if year < 2010:
        raise ValueError(
            f"ACS 1-Year Profile data is only available from 2010 onwards. You requested {year}."
        )
    if year > 2023:
        raise ValueError(
            f"ACS 1-Year data for {year} is not yet released. The latest available year is 2023."
        )

    url: str = f"{api}/data/{year}/acs/acs1/profile"
    params: Dict[str, Optional[str]] = {
        "get": variables,
        "for": "county:*",
        "in": "state:*",
        "key": os.getenv("CENSUS_API_KEY"),
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data: List[List[Optional[Union[str, int, float]]]] = response.json()
    key_data: List[Dict[str, Optional[Union[str, int, float]]]] = [
        dict(zip(keys, row)) for row in data
    ]
    formatted_data: List[Dict[str, Optional[Union[str, int, float]]]] = key_data[1:]
    for row in formatted_data:
        county, state = str(row["name"]).rsplit(", ", 1)
        row["state_name"] = state
        row["county_name"] = county
        row["year"] = year
    cleaned_data: List[Dict[str, Optional[Union[str, int, float]]]] = clean_and_cast(
        formatted_data
    )
    typed_data: List[CensusData] = [CensusData.from_dict(rec) for rec in cleaned_data]
    for record in typed_data:
        for f in fields(CensusData):
            value = getattr(record, f.name)
            if value is not None and isinstance(value, (int, float)) and value < 0:
                setattr(record, f.name, None)
    for record in typed_data:
        for f in fields(CensusData):
            if getattr(record, f.name) is None:
                setattr(record, f.name, 0)
    return typed_data


def request_data_for_multiple_years(
    years: List[int],
) -> Dict[str, List[List[CensusData]]]:
    data: List[List[CensusData]] = []
    for year in years:
        single_year_data = request_data_for_single_year(year)
        data.append(single_year_data)
    final_data = {"result": data}
    return final_data


def clean_and_cast(
    data: List[Dict[str, Optional[Union[int, float, str]]]],
) -> List[Dict[str, Optional[Union[int, float, str]]]]:
    fields_to_cast = {
        "total_population": int,
        "median_age": float,
        "median_household_income": int,
        "poverty_rate": float,
        "unemployment_rate": float,
        "total_houses": int,
        "home_ownership_rate": float,
        "bachelors_or_higher_degree_pct": float,
        "male_population": int,
        "female_population": int,
        "white_alone_pct": float,
        "black_alone_pct": float,
        "asian_alone_pct": float,
        "hispanic_latino_pct": float,
        "foreign_born_pct": float,
        "non_english_home_pct": float,
        "avg_household_size": float,
        "avg_family_size": float,
        "married_couple_families_pct": float,
        "single_parent_families_pct": float,
        "hs_or_higher_pct": float,
        "renter_occupied_pct": float,
        "median_year_built": int,
        "median_rooms": int,
        "median_gross_rent": int,
        "median_owner_costs_mortgage": int,
        "workers_public_transport_pct": float,
        "workers_car_pct": float,
        "workers_home_pct": float,
        "health_insurance_coverage_pct": float,
        "disability_pct": float,
    }

    for record in data:
        for key, cast_type in fields_to_cast.items():
            value = record.get(key)
            if value not in (None, "", "null"):
                try:
                    record[key] = cast_type(value)
                except (ValueError, TypeError):
                    pass
    return data


def save_to_db(data: Dict[str, List[List[CensusData]]]) -> None:
    for year in data["result"]:
        for record in year:
            state, _ = CensusState.objects.get_or_create(
                state_no=record.state_no,
                defaults={"state_name": record.state_name},
            )
            county, _ = CensusCounty.objects.get_or_create(
                state=state,
                county_name=record.county_name,
                year=record.year,
                defaults={
                    "county_no": record.county_no,
                    "total_population": record.total_population,
                    "total_houses": record.total_houses,
                    "home_ownership_rate": record.home_ownership_rate,
                    "poverty_rate": record.poverty_rate,
                    "unemployment_rate": record.unemployment_rate,
                    "median_age": record.median_age,
                    "bachelors_or_higher_degree_pct": record.bachelors_or_higher_degree_pct,
                },
            )
            detail, _ = CensusDetail.objects.get_or_create(
                county=county,
                defaults={
                    "male_population": record.male_population,
                    "female_population": record.female_population,
                    "white_alone_pct": record.white_alone_pct,
                    "black_alone_pct": record.black_alone_pct,
                    "asian_alone_pct": record.asian_alone_pct,
                    "hispanic_latino_pct": record.hispanic_latino_pct,
                    "foreign_born_pct": record.foreign_born_pct,
                    "non_english_home_pct": record.non_english_home_pct,
                    "avg_household_size": record.avg_household_size,
                    "avg_family_size": record.avg_family_size,
                    "married_couple_families_pct": record.married_couple_families_pct,
                    "single_parent_families_pct": record.single_parent_families_pct,
                    "hs_or_higher_pct": record.hs_or_higher_pct,
                    "renter_occupied_pct": record.renter_occupied_pct,
                    "median_year_built": record.median_year_built,
                    "median_rooms": record.median_rooms,
                    "median_gross_rent": record.median_gross_rent,
                    "median_owner_costs_mortgage": record.median_owner_costs_mortgage,
                    "median_household_income": record.median_household_income,
                    "workers_public_transport_pct": record.workers_public_transport_pct,
                    "workers_car_pct": record.workers_car_pct,
                    "workers_home_pct": record.workers_home_pct,
                    "health_insurance_coverage_pct": record.health_insurance_coverage_pct,
                    "disability_pct": record.disability_pct,
                },
            )
