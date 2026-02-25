from dataclasses import dataclass
from typing import Optional


@dataclass
class CensusData:
    total_population: Optional[int] = None
    median_age: Optional[float] = None
    median_household_income: Optional[int] = None
    poverty_rate: Optional[float] = None
    unemployment_rate: Optional[float] = None
    total_houses: Optional[int] = None
    home_ownership_rate: Optional[float] = None
    bachelors_or_higher_degree_pct: Optional[float] = None
    male_population: Optional[int] = None
    female_population: Optional[int] = None
    white_alone_pct: Optional[float] = None
    black_alone_pct: Optional[float] = None
    asian_alone_pct: Optional[float] = None
    hispanic_latino_pct: Optional[float] = None
    foreign_born_pct: Optional[float] = None
    non_english_home_pct: Optional[float] = None
    avg_household_size: Optional[float] = None
    avg_family_size: Optional[float] = None
    married_couple_families_pct: Optional[float] = None
    single_parent_families_pct: Optional[float] = None
    hs_or_higher_pct: Optional[float] = None
    renter_occupied_pct: Optional[float] = None
    median_year_built: Optional[int] = None
    median_rooms: Optional[float] = None
    median_gross_rent: Optional[int] = None
    median_owner_costs_mortgage: Optional[int] = None
    workers_public_transport_pct: Optional[float] = None
    workers_car_pct: Optional[float] = None
    workers_home_pct: Optional[float] = None
    health_insurance_coverage_pct: Optional[float] = None
    disability_pct: Optional[float] = None
    state_name: Optional[str] = None
    state_no: Optional[str] = None
    county_name: Optional[str] = None
    county_no: Optional[str] = None
    year: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict) -> "CensusData":
        return cls(**data)

    def to_dict(self) -> dict:
        return {
            "total_population": self.total_population,
            "median_age": self.median_age,
            "median_household_income": self.median_household_income,
            "poverty_rate": self.poverty_rate,
            "unemployment_rate": self.unemployment_rate,
            "total_houses": self.total_houses,
            "home_ownership_rate": self.home_ownership_rate,
            "bachelors_or_higher_degree_pct": self.bachelors_or_higher_degree_pct,
            "male_population": self.male_population,
            "female_population": self.female_population,
            "white_alone_pct": self.white_alone_pct,
            "black_alone_pct": self.black_alone_pct,
            "asian_alone_pct": self.asian_alone_pct,
            "hispanic_latino_pct": self.hispanic_latino_pct,
            "foreign_born_pct": self.foreign_born_pct,
            "non_english_home_pct": self.non_english_home_pct,
            "avg_household_size": self.avg_household_size,
            "avg_family_size": self.avg_family_size,
            "married_couple_families_pct": self.married_couple_families_pct,
            "single_parent_families_pct": self.single_parent_families_pct,
            "hs_or_higher_pct": self.hs_or_higher_pct,
            "renter_occupied_pct": self.renter_occupied_pct,
            "median_year_built": self.median_year_built,
            "median_rooms": self.median_rooms,
            "median_gross_rent": self.median_gross_rent,
            "median_owner_costs_mortgage": self.median_owner_costs_mortgage,
            "workers_public_transport_pct": self.workers_public_transport_pct,
            "workers_car_pct": self.workers_car_pct,
            "workers_home_pct": self.workers_home_pct,
            "health_insurance_coverage_pct": self.health_insurance_coverage_pct,
            "disability_pct": self.disability_pct,
            "state_name": self.state_name,
            "state_no": self.state_no,
            "county_name": self.county_name,
            "county_no": self.county_no,
            "year": self.year,
        }
