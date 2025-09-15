from rest_framework import serializers

from census.models import CensusCounty


class CountyReportRequestSerializer(serializers.Serializer):
    state_no = serializers.CharField(required=False)
    year = serializers.IntegerField(required=False)

    min_population = serializers.IntegerField(required=False)
    max_population = serializers.IntegerField(required=False)

    min_houses = serializers.IntegerField(required=False)
    max_houses = serializers.IntegerField(required=False)

    min_ownership = serializers.FloatField(required=False)
    max_ownership = serializers.FloatField(required=False)

    min_poverty = serializers.FloatField(required=False)
    max_poverty = serializers.FloatField(required=False)

    min_unemployment = serializers.FloatField(required=False)
    max_unemployment = serializers.FloatField(required=False)

    min_age = serializers.FloatField(required=False)
    max_age = serializers.FloatField(required=False)

    min_bachelors = serializers.FloatField(required=False)
    max_bachelors = serializers.FloatField(required=False)


class DetailReportRequestSerializer(serializers.Serializer):
    county_name = serializers.CharField()
    year = serializers.IntegerField()


class CountyReportResponseSerializer(serializers.Serializer):
    state_name = serializers.CharField(required=False)
    state_no = serializers.CharField(required=False)
    county_no = serializers.CharField(required=False)
    county_name = serializers.CharField(required=False)
    year = serializers.IntegerField(required=False)
    total_population = serializers.IntegerField(required=False)
    total_houses = serializers.IntegerField(required=False)
    home_ownership_rate = serializers.FloatField(required=False)
    poverty_rate = serializers.FloatField(required=False)
    unemployment_rate = serializers.FloatField(required=False)
    median_age = serializers.FloatField(required=False)
    bachelors_or_higher_degree_pct = serializers.FloatField(required=False)


class DetailReportResponseSerializer(serializers.Serializer):
    male_population = serializers.IntegerField(required=False)
    female_population = serializers.IntegerField(required=False)
    white_alone_pct = serializers.FloatField(required=False)
    black_alone_pct = serializers.FloatField(required=False)
    asian_alone_pct = serializers.FloatField(required=False)
    hispanic_latino_pct = serializers.FloatField(required=False)
    foreign_born_pct = serializers.FloatField(required=False)
    non_english_home_pct = serializers.FloatField(required=False)
    avg_household_size = serializers.FloatField(required=False)
    avg_family_size = serializers.FloatField(required=False)
    married_couple_families_pct = serializers.FloatField(required=False)
    single_parent_families_pct = serializers.FloatField(required=False)
    hs_or_higher_pct = serializers.FloatField(required=False)
    renter_occupied_pct = serializers.FloatField(required=False)
    median_year_built = serializers.IntegerField(required=False)
    median_rooms = serializers.FloatField(required=False)
    median_gross_rent = serializers.IntegerField(required=False)
    median_owner_costs_mortgage = serializers.IntegerField(required=False)
    median_household_income = serializers.IntegerField(required=False)
    workers_public_transport_pct = serializers.FloatField(required=False)
    workers_car_pct = serializers.FloatField(required=False)
    workers_home_pct = serializers.FloatField(required=False)
    health_insurance_coverage_pct = serializers.FloatField(required=False)
    disability_pct = serializers.FloatField(required=False)
