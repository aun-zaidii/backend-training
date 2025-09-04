import requests
from .models import *


def request_data_for_single_year (year):
    if year == 2020:
        raise ValueError("ACS 1-Year Profile estimates were not published for 2020 due to COVID-19.")
    if year < 2010:
        raise ValueError(f"ACS 1-Year Profile data is only available from 2010 onwards. You requested {year}.")
    if year > 2023:
        raise ValueError(f"ACS 1-Year data for {year} is not yet released. The latest available year is 2023.")
    variables =  "NAME,DP05_0001E,DP05_0017E,DP03_0062E,DP03_0128PE,DP03_0009PE,DP04_0001E,DP04_0046PE,DP02_0068PE,DP05_0002E,DP05_0003E,DP05_0077PE,DP05_0078PE,DP05_0080PE,DP05_0071PE,DP02_0094PE,DP02_0111PE,DP02_0016E,DP02_0017E,DP02_0019PE,DP02_0022PE,DP02_0067PE,DP04_0047PE,DP04_0019E,DP04_0045E,DP04_0134E,DP04_0101E,DP03_0063E,DP03_0021PE,DP03_0022PE,DP03_0024PE,DP03_0096PE,DP02_0072PE"
    keys = [
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
    "county"
    ]

    url = f"https://api.census.gov/data/{year}/acs/acs1/profile"
    params = {"get" : variables, "for" : "county:*", "in" : "state:*", "key": "54eb7381f889c8b38d11542e25f99a07708b3322"}
    data = requests.get(url, params=params).json()
    key_data = [dict(zip(keys, row)) for row in data]
    formatted_data = key_data[1:]
    for row in formatted_data:
        county, state = row["name"].rsplit(", ", 1)
        row['state_name'] = state
        row['county_name'] = county
        row["year"] = year
    typed_data = clean_and_cast(formatted_data)
    for record in typed_data:
        for key in record:
            if record[key] is not None and type(record[key]) != str and record[key]<0:
                record[key] = None
    for record in typed_data:
        for key in record:
            if record[key] is None:
                record[key] = 0
    return typed_data
    


def request_data_for_multiple_years(years):
    data = []
    for year in years:
        single_year_data = request_data_for_single_year(year)
        data.append(single_year_data)
    final_data = {'result':data}
    return final_data



        



def clean_and_cast(data):
    fields_to_cast = {
        'total_population': int,
        'median_age': float,
        'median_household_income': int,
        'poverty_rate': float,
        'unemployment_rate': float,
        'total_houses': int,
        'home_ownership_rate': float,
        'bachelors_or_higher_degree_pct': float,
        'male_population': int,
        'female_population': int,
        'white_alone_pct': float,
        'black_alone_pct': float,
        'asian_alone_pct': float,
        'hispanic_latino_pct': float,
        'foreign_born_pct': float,
        'non_english_home_pct': float,
        'avg_household_size': float,
        'avg_family_size': float,
        'married_couple_families_pct': float,
        'single_parent_families_pct': float,
        'hs_or_higher_pct': float,
        'renter_occupied_pct': float,
        'median_year_built': int,
        'median_rooms': int,
        'median_gross_rent': int,
        'median_owner_costs_mortgage': int,
        'workers_public_transport_pct': float,
        'workers_car_pct': float,
        'workers_home_pct': float,
        'health_insurance_coverage_pct': float,
        'disability_pct': float
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


def save_to_db (data):
    for year in data['result']:
        for record in year:
            state,_ = CensusState.objects.get_or_create(state_no = record['state'], defaults={'state_name' : record.get('state_name')})
            county,_ = CensusCounty .objects.get_or_create(
                state = state,
                county_no = record['county'],
                year = record['year'],
                defaults={
                    'county_name': record.get('county_name'),
                    'total_population': record.get('total_population'),
                    'total_houses': record.get('total_houses'),
                    'home_ownership_rate': record.get('home_ownership_rate'),
                    'poverty_rate': record.get('poverty_rate'),
                    'unemployment_rate': record.get('unemployment_rate'),
                    'median_age': record.get('median_age'),
                    'bachelors_or_higher_degree_pct': record.get('bachelors_or_higher_degree_pct')
                }
            ) 
            detail,_ = CensusDetail.objects.get_or_create(
                county = county,
                defaults = { 
                    'male_population': record.get('male_population'),
                    'female_population': record.get('female_population'),
                    'white_alone_pct': record.get('white_alone_pct'),
                    'black_alone_pct': record.get('black_alone_pct'),
                    'asian_alone_pct': record.get('asian_alone_pct'),
                    'hispanic_latino_pct': record.get('hispanic_latino_pct'),
                    'foreign_born_pct': record.get('foreign_born_pct'),
                    'non_english_home_pct': record.get('non_english_home_pct'),
                    'avg_household_size': record.get('avg_household_size'),
                    'avg_family_size': record.get('avg_family_size'),
                    'married_couple_families_pct': record.get('married_couple_families_pct'),
                    'single_parent_families_pct': record.get('single_parent_families_pct'),
                    'hs_or_higher_pct': record.get('hs_or_higher_pct'),
                    'renter_occupied_pct': record.get('renter_occupied_pct'),
                    'median_year_built': record.get('median_year_built'),
                    'median_rooms': record.get('median_rooms'),
                    'median_gross_rent': record.get('median_gross_rent'),
                    'median_owner_costs_mortgage': record.get('median_owner_costs_mortgage'),
                    'median_household_income': record.get('median_household_income'),
                    'workers_public_transport_pct': record.get('workers_public_transport_pct'),
                    'workers_car_pct': record.get('workers_car_pct', 0.0),
                    'workers_home_pct': record.get('workers_home_pct'),
                    'health_insurance_coverage_pct': record.get('health_insurance_coverage_pct'),
                    'disability_pct': record.get('disability_pct')
                }
            )
    return 








