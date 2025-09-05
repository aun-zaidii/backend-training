from datetime import datetime

from django.db import models

from .enums import StatusChoices


class CensusState(models.Model):
    state_no: str = models.CharField(max_length=25, unique=True)
    state_name: str = models.CharField(max_length=50, default="Unknown")

    def __str__(self) -> str:
        return f"{self.state_no}"


class CensusCounty(models.Model):
    state: CensusState = models.ForeignKey(CensusState, on_delete=models.CASCADE)
    county_no: str = models.CharField(max_length=25)
    county_name: str = models.CharField(max_length=50, default="Unknown")
    year: int = models.IntegerField()
    total_population: int = models.IntegerField(default=0)
    total_houses: int = models.IntegerField(default=0.0)
    home_ownership_rate: float = models.FloatField(default=0.0)
    poverty_rate: float = models.FloatField(default=0.0)
    unemployment_rate: float = models.FloatField(default=0.0)
    median_age: float = models.FloatField(default=0.0)
    bachelors_or_higher_degree_pct: float = models.FloatField(default=0.0)

    class Meta:
        unique_together = ("state", "county_no", "year")

    def __str__(self) -> str:
        return f"{self.county_no}"


class CensusDetail(models.Model):
    county: CensusCounty = models.OneToOneField(
        CensusCounty, on_delete=models.CASCADE, related_name="detail"
    )
    male_population: int = models.IntegerField(default=0)
    female_population: int = models.IntegerField(default=0)
    white_alone_pct: float = models.FloatField(default=0.0)
    black_alone_pct: float = models.FloatField(default=0.0)
    asian_alone_pct: float = models.FloatField(default=0.0)
    hispanic_latino_pct: float = models.FloatField(default=0.0)
    foreign_born_pct: float = models.FloatField(default=0.0)
    non_english_home_pct: float = models.FloatField(default=0.0)
    avg_household_size: float = models.FloatField(default=0.0)
    avg_family_size: float = models.FloatField(default=0.0)
    married_couple_families_pct: float = models.FloatField(default=0.0)
    single_parent_families_pct: float = models.FloatField(default=0.0)
    hs_or_higher_pct: float = models.FloatField(default=0.0)
    renter_occupied_pct: float = models.FloatField(default=0.0)
    median_year_built: float = models.IntegerField(default=0)
    median_rooms: float = models.FloatField(default=0.0)
    median_gross_rent: int = models.IntegerField(default=0)
    median_owner_costs_mortgage: int = models.IntegerField(default=0)
    median_household_income: int = models.IntegerField(default=0)
    workers_public_transport_pct: float = models.FloatField(default=0.0)
    workers_car_pct: float = models.FloatField(default=0.0)
    workers_home_pct: float = models.FloatField(default=0.0)
    health_insurance_coverage_pct: float = models.FloatField(default=0.0)
    disability_pct: float = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"{self.county}"


class CensusLog(models.Model):
    task_id = models.CharField(max_length=40)
    name: str = models.CharField(max_length=30)
    started_at: datetime = models.DateTimeField(auto_now_add=True)
    finish_at: datetime = models.DateTimeField(null=True, blank=True)
    log_error: str = models.TextField(blank=True, null=True)
    status: str = models.CharField(max_length=30, choices=StatusChoices.choices)

    def __str__(self) -> str:
        return f"{self.name}"
