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
    county_name = serializers.CharField(required=False)
    year = serializers.IntegerField(required=False)


class CensusCountyReportResponseSerializer(serializers.ModelSerializer):

    state_name = serializers.CharField(source="state.state_name")
    state_no = serializers.CharField(source="state.state_no")

    class Meta:
        model = CensusCounty
        fields = [
            "state_name",
            "state_no",
            "county_no",
            "county_name",
            "year",
            "total_population",
            "total_houses",
            "home_ownership_rate",
            "poverty_rate",
            "unemployment_rate",
            "median_age",
            "bachelors_or_higher_degree_pct",
        ]


class DetailResponseSerializer(serializers.Serializer):
    male_population = serializers.IntegerField()
    female_population = serializers.IntegerField()

    white_alone_pct = serializers.FloatField()
    black_alone_pct = serializers.FloatField()
    asian_alone_pct = serializers.FloatField()
    hispanic_latino_pct = serializers.FloatField()
    foreign_born_pct = serializers.FloatField()
    non_english_home_pct = serializers.FloatField()

    avg_household_size = serializers.FloatField()
    avg_family_size = serializers.FloatField()

    married_couple_families_pct = serializers.FloatField()
    single_parent_families_pct = serializers.FloatField()
    hs_or_higher_pct = serializers.FloatField()
    renter_occupied_pct = serializers.FloatField()

    median_year_built = serializers.IntegerField()
    median_rooms = serializers.FloatField()

    median_gross_rent = serializers.IntegerField()
    median_owner_costs_mortgage = serializers.IntegerField()
    median_household_income = serializers.IntegerField()

    workers_public_transport_pct = serializers.FloatField()
    workers_car_pct = serializers.FloatField()
    workers_home_pct = serializers.FloatField()

    health_insurance_coverage_pct = serializers.FloatField()
    disability_pct = serializers.FloatField()
