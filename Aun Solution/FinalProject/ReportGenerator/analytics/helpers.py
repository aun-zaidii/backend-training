import hashlib
import json

import numpy as np
import pandas as pd
from django.conf import settings
from django.core.cache import cache

from census.models import CensusCounty


def clean_value(value):
    if pd.isna(value) or np.isinf(value):
        return None
    if hasattr(value, "item"):
        return value.item()
    return value


def generate_cache_key(data, prefix="census_analytics"):
    sorted_data = json.dumps(data, sort_keys=True)
    key_hash = hashlib.md5(sorted_data.encode()).hexdigest()
    return f"{prefix}_{key_hash}"


def data_aggrigation(filters):
    cache_key = generate_cache_key(filters, "census_aggrigation")
    cached_response = cache.get(cache_key)
    if cached_response:
        print(f"Cache HIT for {cache_key}")
        return cached_response
    print(f"Cache MISS for {cache_key}")
    queryset = CensusCounty.objects.select_related("state", "detail")
    state_no = filters.get("state_no")
    year = filters.get("year")
    county_no = filters.get("county_no")
    if state_no:
        queryset = queryset.filter(state__state_no=state_no)
    if year:
        queryset = queryset.filter(year=year)
    if county_no:
        queryset = queryset.filter(county_no=county_no)
    data = []
    for county in queryset:
        detail = county.detail

        data.append(
            {
                "state_no": county.state.state_no,
                "county_no": county.county_no,
                "total_population": county.total_population,
                "total_houses": county.total_houses,
                "home_ownership_rate": county.home_ownership_rate,
                "poverty_rate": county.poverty_rate,
                "unemployment_rate": county.unemployment_rate,
                "median_age": county.median_age,
                "bachelors_or_higher_degree_pct": county.bachelors_or_higher_degree_pct,
                "male_population": detail.male_population,
                "female_population": detail.female_population,
                "white_alone_pct": detail.white_alone_pct,
                "black_alone_pct": detail.black_alone_pct,
                "asian_alone_pct": detail.asian_alone_pct,
                "hispanic_latino_pct": detail.hispanic_latino_pct,
                "foreign_born_pct": detail.foreign_born_pct,
                "non_english_home_pct": detail.non_english_home_pct,
                "avg_household_size": detail.avg_household_size,
                "avg_family_size": detail.avg_family_size,
                "married_couple_families_pct": detail.married_couple_families_pct,
                "single_parent_families_pct": detail.single_parent_families_pct,
                "hs_or_higher_pct": detail.hs_or_higher_pct,
                "renter_occupied_pct": detail.renter_occupied_pct,
                "median_year_built": detail.median_year_built,
                "median_rooms": detail.median_rooms,
                "median_gross_rent": detail.median_gross_rent,
                "median_owner_costs_mortgage": detail.median_owner_costs_mortgage,
                "median_household_income": detail.median_household_income,
                "workers_public_transport_pct": detail.workers_public_transport_pct,
                "workers_car_pct": detail.workers_car_pct,
                "workers_home_pct": detail.workers_home_pct,
                "health_insurance_coverage_pct": detail.health_insurance_coverage_pct,
                "disability_pct": detail.disability_pct,
            }
        )

    df = pd.DataFrame(data)
    agg_map = {
        "state_no": ["nunique"],
        "county_no": ["count"],
        "total_population": ["sum", "mean", "min", "max"],
        "total_houses": ["sum", "mean", "min", "max"],
        "male_population": ["sum", "mean", "min", "max"],
        "female_population": ["sum", "mean", "min", "max"],
        "home_ownership_rate": ["mean", "min", "max"],
        "poverty_rate": ["mean", "min", "max"],
        "unemployment_rate": ["mean", "min", "max"],
        "bachelors_or_higher_degree_pct": ["mean", "min", "max"],
        "white_alone_pct": ["mean", "min", "max"],
        "black_alone_pct": ["mean", "min", "max"],
        "asian_alone_pct": ["mean", "min", "max"],
        "hispanic_latino_pct": ["mean", "min", "max"],
        "foreign_born_pct": ["mean", "min", "max"],
        "non_english_home_pct": ["mean", "min", "max"],
        "married_couple_families_pct": ["mean", "min", "max"],
        "single_parent_families_pct": ["mean", "min", "max"],
        "hs_or_higher_pct": ["mean", "min", "max"],
        "renter_occupied_pct": ["mean", "min", "max"],
        "workers_public_transport_pct": ["mean", "min", "max"],
        "workers_car_pct": ["mean", "min", "max"],
        "workers_home_pct": ["mean", "min", "max"],
        "health_insurance_coverage_pct": ["mean", "min", "max"],
        "disability_pct": ["mean", "min", "max"],
        "median_age": ["mean", "min", "max"],
        "avg_household_size": ["mean", "min", "max"],
        "avg_family_size": ["mean", "min", "max"],
        "median_year_built": ["mean", "min", "max"],
        "median_rooms": ["mean", "min", "max"],
        "median_gross_rent": ["mean", "min", "max"],
        "median_owner_costs_mortgage": ["mean", "min", "max"],
        "median_household_income": ["mean", "sum", "min", "max"],
    }
    aggrigated_data = df.agg(agg_map)
    aggrigated_data = aggrigated_data.replace([np.nan, np.inf, -np.inf], None)
    result = aggrigated_data.to_dict(orient="index")
    cache.set(cache_key, result, timeout=getattr(settings, "CACHE_TIMEOUT", 86400))
    return result


def statistical_analysis(filters):
    cache_key = generate_cache_key(filters, "census_analytics")
    cached_response = cache.get(cache_key)
    if cached_response:
        print(f"Cache HIT for {cache_key}")
        return cached_response
    print(f"Cache MISS for {cache_key}")
    queryset = CensusCounty.objects.select_related("state", "detail")
    state_no = filters.get("state_no")
    year = filters.get("year")
    county_no = filters.get("county_no")
    if state_no:
        queryset = queryset.filter(state__state_no=state_no)
    if year:
        queryset = queryset.filter(year=year)
    if county_no:
        queryset = queryset.filter(county_no=county_no)
    data = []
    for county in queryset:
        detail = county.detail

        data.append(
            {
                "total_population": county.total_population,
                "total_houses": county.total_houses,
                "home_ownership_rate": county.home_ownership_rate,
                "poverty_rate": county.poverty_rate,
                "unemployment_rate": county.unemployment_rate,
                "median_age": county.median_age,
                "bachelors_or_higher_degree_pct": county.bachelors_or_higher_degree_pct,
                "male_population": detail.male_population,
                "female_population": detail.female_population,
                "white_alone_pct": detail.white_alone_pct,
                "black_alone_pct": detail.black_alone_pct,
                "asian_alone_pct": detail.asian_alone_pct,
                "hispanic_latino_pct": detail.hispanic_latino_pct,
                "foreign_born_pct": detail.foreign_born_pct,
                "non_english_home_pct": detail.non_english_home_pct,
                "avg_household_size": detail.avg_household_size,
                "avg_family_size": detail.avg_family_size,
                "married_couple_families_pct": detail.married_couple_families_pct,
                "single_parent_families_pct": detail.single_parent_families_pct,
                "hs_or_higher_pct": detail.hs_or_higher_pct,
                "renter_occupied_pct": detail.renter_occupied_pct,
                "median_year_built": detail.median_year_built,
                "median_rooms": detail.median_rooms,
                "median_gross_rent": detail.median_gross_rent,
                "median_owner_costs_mortgage": detail.median_owner_costs_mortgage,
                "median_household_income": detail.median_household_income,
                "workers_public_transport_pct": detail.workers_public_transport_pct,
                "workers_car_pct": detail.workers_car_pct,
                "workers_home_pct": detail.workers_home_pct,
                "health_insurance_coverage_pct": detail.health_insurance_coverage_pct,
                "disability_pct": detail.disability_pct,
            }
        )

    df = pd.DataFrame(data)
    stats = {}

    for col in df.columns:
        col_data = df[col].dropna()
        stats[col] = {
            "25th_percentile": clean_value(col_data.quantile(0.25)),
            "50th_percentile": clean_value(col_data.quantile(0.50)),
            "75th_percentile": clean_value(col_data.quantile(0.75)),
            "95th_percentile": clean_value(col_data.quantile(0.95)),
            "Standard Deviation": clean_value(col_data.std()),
            "Variance": clean_value(col_data.var()),
        }
    cache.set(cache_key, stats, timeout=getattr(settings, "CACHE_TIMEOUT", 86400))
    return stats
