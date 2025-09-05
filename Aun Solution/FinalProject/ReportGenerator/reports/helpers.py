import hashlib
import json

import pandas as pd
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse

from census.models import *


def generate_cache_key(data, prefix="county_report"):
    sorted_data = json.dumps(data, sort_keys=True)
    key_hash = hashlib.md5(sorted_data.encode()).hexdigest()
    return f"{prefix}_{key_hash}"


def generate_county_report(data):
    cache_key = generate_cache_key(data, "county_report")
    cached_response = cache.get(cache_key)
    if cached_response:
        print(f"Cache HIT for {cache_key}")
        return cached_response
    print(f"Cache MISS for {cache_key}")
    queryset = CensusCounty.objects.select_related("state").all()
    state_no = data.get("state_no")
    year = data.get("year")
    min_population = data.get("min_population")
    max_population = data.get("max_population")
    min_houses = data.get("min_houses")
    max_houses = data.get("max_houses")
    min_ownership = data.get("min_ownership")
    max_ownership = data.get("max_ownership")
    min_poverty = data.get("min_poverty")
    max_poverty = data.get("max_poverty")
    min_unemployment = data.get("min_unemployment")
    max_unemployment = data.get("max_unemployment")
    min_age = data.get("min_age")
    max_age = data.get("max_age")
    min_bachelors = data.get("min_bachelors")
    max_bachelors = data.get("max_bachelors")
    if state_no:
        queryset = queryset.filter(state__state_no=state_no)
    if year:
        queryset = queryset.filter(year=year)
    if min_population:
        queryset = queryset.filter(total_population__gte=min_population)
    if max_population:
        queryset = queryset.filter(total_population__lte=max_population)
    if min_houses:
        queryset = queryset.filter(total_houses__gte=min_houses)
    if max_houses:
        queryset = queryset.filter(total_houses__lte=max_houses)
    if min_ownership:
        queryset = queryset.filter(home_ownership_rate__gte=min_ownership)
    if max_ownership:
        queryset = queryset.filter(home_ownership_rate__lte=max_ownership)
    if min_poverty:
        queryset = queryset.filter(poverty_rate__gte=min_poverty)
    if max_poverty:
        queryset = queryset.filter(poverty_rate__lte=max_poverty)
    if min_unemployment:
        queryset = queryset.filter(unemployment_rate__gte=min_unemployment)
    if max_unemployment:
        queryset = queryset.filter(unemployment_rate__lte=max_unemployment)
    if min_age:
        queryset = queryset.filter(median_age__gte=min_age)
    if max_age:
        queryset = queryset.filter(median_age__lte=max_age)
    if min_bachelors:
        queryset = queryset.filter(bachelors_or_higher_degree_pct__gte=min_bachelors)
    if max_bachelors:
        queryset = queryset.filter(bachelors_or_higher_degree_pct__lte=max_bachelors)
    report_data = []
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

    df = pd.DataFrame(report_data)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="census_report.csv"'
    df.to_csv(response, index=False)
    cache.set(cache_key, response, timeout=getattr(settings, "CACHE_TIMEOUT", 86400))
    return response


def generate_detail_report(county_no):
    cache_key = generate_cache_key({"county_no": county_no}, "detail_report")
    cached_response = cache.get(cache_key)
    if cached_response:
        return cached_response
    queryset = CensusDetail.objects.select_related("county").filter(
        county__county_no=county_no
    )
    df = pd.DataFrame(queryset)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="county_detail_report.csv"'
    df.to_csv(response, index=False)
    cache.set(cache_key, response, timeout=getattr(settings, "CACHE_TIMEOUT", 86400))
    return response
