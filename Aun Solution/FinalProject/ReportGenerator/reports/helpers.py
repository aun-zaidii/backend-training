import hashlib
import io
import json
from typing import Dict, List, Optional, Union

import pandas as pd
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse

from census.models import CensusCounty, CensusDetail


def generate_cache_key(
    data: Dict[str, Union[int, float, str]], prefix: str = "county_report"
) -> str:
    sorted_data = json.dumps(data, sort_keys=True)
    key_hash = hashlib.md5(sorted_data.encode()).hexdigest()
    return f"{prefix}_{key_hash}"


def generate_county_report(
    data: Dict[str, Union[str, int, float]],
) -> list[dict[str, Union[str, int, float]]]:

    filter_kwargs = {}
    state_no = data.get("state_no")
    if state_no:
        filter_kwargs["state__state_no"] = state_no
    year = data.get("year")
    if year:
        filter_kwargs["year"] = year
    min_population = data.get("min_population")
    if min_population:
        filter_kwargs["total_population__gte"] = min_population
    max_population = data.get("max_population")
    if max_population:
        filter_kwargs["total_population__lte"] = max_population
    min_houses = data.get("min_houses")
    if min_houses:
        filter_kwargs["total_houses__gte"] = min_houses
    max_houses = data.get("max_houses")
    if max_houses:
        filter_kwargs["total_houses__lte"] = max_houses
    min_ownership = data.get("min_ownership")
    if min_ownership:
        filter_kwargs["home_ownership_rate__gte"] = min_ownership
    max_ownership = data.get("max_ownership")
    if max_ownership:
        filter_kwargs["home_ownership_rate__lte"] = max_ownership
    min_poverty = data.get("min_poverty")
    if min_poverty:
        filter_kwargs["poverty_rate__gte"] = min_poverty
    max_poverty = data.get("max_poverty")
    if max_poverty:
        filter_kwargs["poverty_rate__lte"] = max_poverty
    min_unemployment = data.get("min_unemployment")
    if min_unemployment:
        filter_kwargs["unemployment_rate__gte"] = min_unemployment
    max_unemployment = data.get("max_unemployment")
    if max_unemployment:
        filter_kwargs["unemployment_rate__lte"] = max_unemployment
    min_age = data.get("min_age")
    if min_age:
        filter_kwargs["median_age__gte"] = min_age
    max_age = data.get("max_age")
    if max_age:
        filter_kwargs["median_age__lte"] = max_age
    min_bachelors = data.get("min_bachelors")
    if min_bachelors:
        filter_kwargs["bachelors_or_higher_degree_pct__gte"] = min_bachelors
    max_bachelors = data.get("max_bachelors")
    if max_bachelors:
        filter_kwargs["bachelors_or_higher_degree_pct__lte"] = max_bachelors
    queryset = CensusCounty.objects.select_related("state").filter(**filter_kwargs)
    report_data: List[Dict[str, Union[str, int, float]]] = []
    for county in queryset:
        report_data.append(
            {
                "state_name": county.state.state_name,
                "state_no": county.state.state_no,
                "county_no": county.county_no,
                "county_name": county.county_name,
                "year": county.year,
                "total_population": county.total_population,
                "total_houses": county.total_houses,
                "home_ownership_rate": county.home_ownership_rate,
                "poverty_rate": county.poverty_rate,
                "unemployment_rate": county.unemployment_rate,
                "median_age": county.median_age,
                "bachelors_or_higher_degree_pct": county.bachelors_or_higher_degree_pct,
            }
        )
    return report_data


def generate_detail_report(county_name, year) -> list:
    queryset = CensusDetail.objects.select_related("county").filter(
        county__county_name=county_name, county__year=year
    )
    detail_fields = [
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
    ]
    return list(queryset.values(*detail_fields))


def county_report_json(data):
    cache_key = generate_cache_key(data, "county_report_json")
    cached_response: Optional[HttpResponse] = cache.get(cache_key)
    if cached_response:
        print(f"Cache HIT for {cache_key}")
        return cached_response
    print(f"Cache MISS for {cache_key}")
    response = generate_county_report(data)
    cache.set(cache_key, response, timeout=getattr(settings, "CACHE_TIMEOUT", 86400))
    return response


def county_report_csv(data: Dict[str, Union[str, int, float]]) -> HttpResponse:
    cache_key = generate_cache_key(data, "county_report_csv")
    cached_response: Optional[HttpResponse] = cache.get(cache_key)
    if cached_response:
        print(f"Cache HIT for {cache_key}")
        return cached_response
    print(f"Cache MISS for {cache_key}")
    report_data = generate_county_report(data)
    df = pd.DataFrame(report_data)
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    response = HttpResponse(buffer.getvalue(), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="census_report.csv"'
    cache.set(cache_key, response, timeout=getattr(settings, "CACHE_TIMEOUT", 86400))
    return response


def detail_report_csv(data):
    county_name = data["county_name"]
    year = data["year"]
    cache_key = generate_cache_key({"county_name": county_name}, "detail_report_csv")
    cached_response = cache.get(cache_key)
    if cached_response:
        return cached_response
    detail_data = generate_detail_report(county_name, year)
    df = pd.DataFrame(detail_data)
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    response = HttpResponse(buffer.getvalue(), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="county_detail_report.csv"'
    cache.set(cache_key, response, timeout=getattr(settings, "CACHE_TIMEOUT", 86400))
    return response


def detail_report_json(data):
    county_name = data["county_name"]
    year = data["year"]
    cache_key = generate_cache_key({"county_name": county_name}, "detail_report_json")
    cached_response = cache.get(cache_key)
    if cached_response:
        return cached_response
    detail_data = generate_detail_report(county_name, year)
    cache.set(cache_key, detail_data, timeout=getattr(settings, "CACHE_TIMEOUT", 86400))
    print(detail_data)
    return detail_data
