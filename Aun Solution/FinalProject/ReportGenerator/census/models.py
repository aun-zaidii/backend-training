from datetime import datetime
from typing import TYPE_CHECKING

from django.db import models

from .enums import StatusChoices


class CensusState(models.Model):
    state_no: models.CharField = models.CharField(max_length=25, unique=True)
    state_name: models.CharField = models.CharField(max_length=50, default="Unknown")

    def __str__(self) -> str:
        return f"{self.state_no}"


class CensusCounty(models.Model):
    state = models.ForeignKey(CensusState, on_delete=models.CASCADE)  # type: ignore
    county_no: models.CharField = models.CharField(max_length=25)
    county_name: models.CharField = models.CharField(max_length=50, default="Unknown")
    year: models.IntegerField = models.IntegerField()
    total_population: models.IntegerField = models.IntegerField(default=0)
    total_houses: models.IntegerField = models.IntegerField(default=0.0)
    home_ownership_rate: models.FloatField = models.FloatField(default=0.0)
    poverty_rate: models.FloatField = models.FloatField(default=0.0)
    unemployment_rate: models.FloatField = models.FloatField(default=0.0)
    median_age: models.FloatField = models.FloatField(default=0.0)
    bachelors_or_higher_degree_pct: models.FloatField = models.FloatField(default=0.0)

    if TYPE_CHECKING:
        detail: "CensusDetail"

    class Meta:
        unique_together = ("state", "county_name", "year")

    def __str__(self) -> str:
        return f"state_no:{self.state.state_no }, state_name{self.state.state_name} county_no:{self.county_no}, countyname:{self.county_name}, tp:{self.total_population}"


class CensusDetail(models.Model):
    county = models.OneToOneField(
        CensusCounty, on_delete=models.CASCADE, related_name="detail"  # type: ignore
    )
    male_population: models.IntegerField = models.IntegerField(default=0)
    female_population: models.IntegerField = models.IntegerField(default=0)
    white_alone_pct: models.FloatField = models.FloatField(default=0.0)
    black_alone_pct: models.FloatField = models.FloatField(default=0.0)
    asian_alone_pct: models.FloatField = models.FloatField(default=0.0)
    hispanic_latino_pct: models.FloatField = models.FloatField(default=0.0)
    foreign_born_pct: models.FloatField = models.FloatField(default=0.0)
    non_english_home_pct: models.FloatField = models.FloatField(default=0.0)
    avg_household_size: models.FloatField = models.FloatField(default=0.0)
    avg_family_size: models.FloatField = models.FloatField(default=0.0)
    married_couple_families_pct: models.FloatField = models.FloatField(default=0.0)
    single_parent_families_pct: models.FloatField = models.FloatField(default=0.0)
    hs_or_higher_pct: models.FloatField = models.FloatField(default=0.0)
    renter_occupied_pct: models.FloatField = models.FloatField(default=0.0)
    median_year_built: models.IntegerField = models.IntegerField(default=0)
    median_rooms: models.FloatField = models.FloatField(default=0.0)
    median_gross_rent: models.IntegerField = models.IntegerField(default=0)
    median_owner_costs_mortgage: models.IntegerField = models.IntegerField(default=0)
    median_household_income: models.IntegerField = models.IntegerField(default=0)
    workers_public_transport_pct: models.FloatField = models.FloatField(default=0.0)
    workers_car_pct: models.FloatField = models.FloatField(default=0.0)
    workers_home_pct: models.FloatField = models.FloatField(default=0.0)
    health_insurance_coverage_pct: models.FloatField = models.FloatField(default=0.0)
    disability_pct: models.FloatField = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"{self.county.county_no} {self.county.year} {self.male_population} {self.county.state.state_no}"


class CensusLog(models.Model):
    task_id: models.CharField = models.CharField(max_length=40)
    name: models.CharField = models.CharField(max_length=30)
    started_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    finish_at: models.DateTimeField = models.DateTimeField(null=True, blank=True)
    log_error: models.TextField = models.TextField(blank=True, null=True)
    status: models.CharField = models.CharField(
        max_length=30, choices=StatusChoices.choices
    )

    def __str__(self) -> str:
        return f"{self.name}"
