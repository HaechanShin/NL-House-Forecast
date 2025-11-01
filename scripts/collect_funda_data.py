"""
Funda Data Collection Script

This script uses the funda-scraper library to collect house listing data
from Funda.nl for the Netherlands house price forecasting project.
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from funda_scraper import FundaScraper
import pandas as pd


def collect_funda_data(
    area: str = "amsterdam",
    want_to: str = "buy",
    n_pages: int = 5,
    output_dir: str = "../data/raw"
):
    """
    Collect house listing data from Funda.nl

    Args:
        area: City or area name (e.g., "amsterdam", "rotterdam", "utrecht")
        want_to: "buy" or "rent"
        n_pages: Number of pages to scrape
        output_dir: Directory to save the raw data
    """

    print(f"Starting data collection from Funda.nl")
    print(f"Area: {area}")
    print(f"Purpose: {want_to}")
    print(f"Pages to scrape: {n_pages}")
    print("-" * 50)

    # Initialize scraper
    scraper = FundaScraper(
        area=area,
        want_to=want_to,
        n_pages=n_pages
    )

    # Scrape data
    print("Scraping data... This may take a few minutes.")
    df = scraper.run()

    # Create output directory if it doesn't exist
    output_path = Path(__file__).parent / output_dir
    output_path.mkdir(parents=True, exist_ok=True)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"funda_{area}_{want_to}_{timestamp}.csv"
    filepath = output_path / filename

    # Save to CSV
    df.to_csv(filepath, index=False)

    print(f"\n{'=' * 50}")
    print(f"Data collection completed!")
    print(f"Total listings collected: {len(df)}")
    print(f"Data saved to: {filepath}")
    print(f"{'=' * 50}")

    # Display basic info
    print("\nDataset Info:")
    print(df.info())
    print("\nFirst few rows:")
    print(df.head())
    print("\nBasic statistics:")
    print(df.describe())

    return df


def collect_multiple_cities(
    cities: list = ["amsterdam", "rotterdam", "utrecht", "den-haag", "eindhoven"],
    want_to: str = "buy",
    n_pages: int = 3,
    output_dir: str = "../data/raw"
):
    """
    Collect data from multiple cities and combine into one dataset

    Args:
        cities: List of city names
        want_to: "buy" or "rent"
        n_pages: Number of pages to scrape per city
        output_dir: Directory to save the raw data
    """

    all_data = []

    for city in cities:
        print(f"\n{'#' * 60}")
        print(f"Collecting data for: {city.upper()}")
        print(f"{'#' * 60}")

        try:
            df = collect_funda_data(
                area=city,
                want_to=want_to,
                n_pages=n_pages,
                output_dir=output_dir
            )
            all_data.append(df)
        except Exception as e:
            print(f"Error collecting data for {city}: {e}")
            continue

    # Combine all data
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)

        # Save combined data
        output_path = Path(__file__).parent / output_dir
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"funda_combined_{want_to}_{timestamp}.csv"
        filepath = output_path / filename

        combined_df.to_csv(filepath, index=False)

        print(f"\n{'=' * 60}")
        print(f"COMBINED DATA SUMMARY")
        print(f"{'=' * 60}")
        print(f"Total listings from all cities: {len(combined_df)}")
        print(f"Combined data saved to: {filepath}")
        print(f"{'=' * 60}")

        return combined_df

    return None


if __name__ == "__main__":
    # Example 1: Collect data from a single city
    print("OPTION 1: Single City Collection")
    print("Uncomment the line below to collect data from Amsterdam:")
    # df = collect_funda_data(area="amsterdam", want_to="buy", n_pages=5)

    print("\n" + "=" * 60)
    print("OPTION 2: Multiple Cities Collection")
    print("Uncomment the line below to collect data from multiple cities:")
    # df_combined = collect_multiple_cities(
    #     cities=["amsterdam", "rotterdam", "utrecht"],
    #     want_to="buy",
    #     n_pages=3
    # )

    print("\n" + "=" * 60)
    print("Script is ready to use!")
    print("Uncomment one of the options above and run the script.")
    print("=" * 60)
