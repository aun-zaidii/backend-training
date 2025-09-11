from rest_framework import serializers


class AggregationStatsRequestSerializer(serializers.Serializer):
    state_name = serializers.CharField(required=False)
    year = serializers.IntegerField(required=False)
    county_name = serializers.CharField(required=False)


class ColumnAggregationSerializer(serializers.Serializer):
    sum = serializers.FloatField(required=False, allow_null=True)
    mean = serializers.FloatField(required=False, allow_null=True)
    min = serializers.FloatField(required=False, allow_null=True)
    max = serializers.FloatField(required=False, allow_null=True)
    count = serializers.FloatField(required=False, allow_null=True)
    nunique = serializers.FloatField(required=False, allow_null=True)


class AggregationResponseSerializer(serializers.Serializer):
    total_population = ColumnAggregationSerializer(required=False)
    total_houses = ColumnAggregationSerializer(required=False)
    median_age = ColumnAggregationSerializer(required=False)
    median_household_income = ColumnAggregationSerializer(required=False)
    poverty_rate = ColumnAggregationSerializer(required=False)
    unemployment_rate = ColumnAggregationSerializer(required=False)
    home_ownership_rate = ColumnAggregationSerializer(required=False)
    bachelors_or_higher_degree_pct = ColumnAggregationSerializer(required=False)


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
