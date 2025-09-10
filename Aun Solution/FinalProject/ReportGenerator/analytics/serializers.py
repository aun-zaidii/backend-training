from rest_framework import serializers


class AggregationStatsRequestSerializer(serializers.Serializer):
    state_name = serializers.CharField(required=False)
    year = serializers.IntegerField(required=False)
    county_name = serializers.CharField(required=False)


class FieldAggregationSerializer(serializers.Serializer):
    state_name = serializers.CharField(required=False, allow_null=True)
    county_name = serializers.CharField(required=False, allow_null=True)
    total_population = serializers.FloatField(required=False, allow_null=True)
    total_houses = serializers.FloatField(required=False, allow_null=True)
    median_age = serializers.FloatField(required=False, allow_null=True)
    median_household_income = serializers.FloatField(required=False, allow_null=True)
    poverty_rate = serializers.FloatField(required=False, allow_null=True)
    unemployment_rate = serializers.FloatField(required=False, allow_null=True)
    home_ownership_rate = serializers.FloatField(required=False, allow_null=True)
    bachelors_or_higher_degree_pct = serializers.FloatField(
        required=False, allow_null=True
    )


class AggregationResponseSerializer(serializers.Serializer):
    sum = FieldAggregationSerializer(required=False)
    mean = FieldAggregationSerializer(required=False)
    min = FieldAggregationSerializer(required=False)
    max = FieldAggregationSerializer(required=False)
    count = FieldAggregationSerializer(required=False, allow_null=True)
    nunique = FieldAggregationSerializer(required=False, allow_null=True)


class PercentileStatsSerializer(serializers.Serializer):
    _25th_percentile = serializers.FloatField(
        required=False, allow_null=True, source="25th_percentile"
    )
    _50th_percentile = serializers.FloatField(
        required=False, allow_null=True, source="50th_percentile"
    )
    _75th_percentile = serializers.FloatField(
        required=False, allow_null=True, source="75th_percentile"
    )
    _95th_percentile = serializers.FloatField(
        required=False, allow_null=True, source="95th_percentile"
    )
    standard_deviation = serializers.FloatField(
        required=False, allow_null=True, source="Standard Deviation"
    )
    variance = serializers.FloatField(
        required=False, allow_null=True, source="Variance"
    )


class StatisticalAnalysisResponseSerializer(serializers.Serializer):
    total_population = PercentileStatsSerializer(required=False)
    total_houses = PercentileStatsSerializer(required=False)
    home_ownership_rate = PercentileStatsSerializer(required=False)
    poverty_rate = PercentileStatsSerializer(required=False)
    unemployment_rate = PercentileStatsSerializer(required=False)
    median_age = PercentileStatsSerializer(required=False)
    bachelors_or_higher_degree_pct = PercentileStatsSerializer(required=False)
    male_population = PercentileStatsSerializer(required=False)
    female_population = PercentileStatsSerializer(required=False)
    white_alone_pct = PercentileStatsSerializer(required=False)
    black_alone_pct = PercentileStatsSerializer(required=False)
    asian_alone_pct = PercentileStatsSerializer(required=False)
    hispanic_latino_pct = PercentileStatsSerializer(required=False)
    foreign_born_pct = PercentileStatsSerializer(required=False)
    non_english_home_pct = PercentileStatsSerializer(required=False)
    avg_household_size = PercentileStatsSerializer(required=False)
    avg_family_size = PercentileStatsSerializer(required=False)
    married_couple_families_pct = PercentileStatsSerializer(required=False)
    single_parent_families_pct = PercentileStatsSerializer(required=False)
    hs_or_higher_pct = PercentileStatsSerializer(required=False)
    renter_occupied_pct = PercentileStatsSerializer(required=False)
    median_year_built = PercentileStatsSerializer(required=False)
    median_rooms = PercentileStatsSerializer(required=False)
    median_gross_rent = PercentileStatsSerializer(required=False)
    median_owner_costs_mortgage = PercentileStatsSerializer(required=False)
    median_household_income = PercentileStatsSerializer(required=False)
    workers_public_transport_pct = PercentileStatsSerializer(required=False)
    workers_car_pct = PercentileStatsSerializer(required=False)
    workers_home_pct = PercentileStatsSerializer(required=False)
    health_insurance_coverage_pct = PercentileStatsSerializer(required=False)
    disability_pct = PercentileStatsSerializer(required=False)

class TimeBaseRequestSerializer(serializers.Serializer):
    state_name = serializers.CharField(required=False)
    start_year = serializers.IntegerField(required=False)
    end_year = serializers.IntegerField(required=False)
    county_name = serializers.CharField(required=False)
