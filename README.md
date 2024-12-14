# bikeshare_2

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Code Quality](https://img.shields.io/badge/code%20quality-A-brightgreen) ![Version](https://img.shields.io/badge/version-1.0-blue)

**bikeshare_2** is a Python-based script for exploring and analyzing U.S. bikeshare data. It provides an interactive way to filter data by city, month, and day of the week and generates insights like popular travel times, stations, trip durations, and user demographics.

---

## Features
- **Data Filtering**: Analyze data by city (`chicago`, `new york city`, `washington`), month (`January` to `June`), or day of the week.
- **Comprehensive Statistics**:
  - Most frequent travel times.
  - Popular stations and trip combinations.
  - Total and average trip durations.
  - User demographics (age groups, gender, user type).
- **Age Group Analysis**: Categorizes users into age groups based on birth year.
- **Interactive Mode**: Option to view raw data and summary statistics dynamically.

---

## Installation

### Prerequisites
- Python 3.x
- Required Python libraries: `pandas`, `numpy`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/PrzemekJedruch/pdsnd_github.git
   cd bikeshare_2
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download bikeshare data files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) and place them in the project directory.

---

## Usage
To start the bikeshare analysis, run:
```bash
python bikeshare_2.py
```

Follow the prompts to select your desired city, month, and day for analysis.

---

## Supported Data Files
The script supports the following datasets:
- **chicago.csv**
- **new_york_city.csv**
- **washington.csv**

Each file must contain the following columns: 
- `Start Time`
- `End Time`
- `Trip Duration`
- `Start Station`
- `End Station`
- `User Type`  
Optional columns:
- `Gender`
- `Birth Year`

---

## Documentation
### Function Overview
- **Core Functions**:
  - `get_filters()`: Collects user inputs for filtering.
  - `load_data()`: Loads and filters the dataset based on user inputs.
  - `time_stats()`, `station_stats()`, `trip_duration_stats()`, `user_stats()`: Analyze and display various statistics.
  - `categorize_age_groups()` and `most_common_age_of_users()`: Provides age-related insights.

- **Detailed Reference**: See the [Documentation](link-to-docs).

---

## Contributing
We welcome contributions! See [CONTRIBUTING.md](link-to-contributing) for guidelines.

---

## License
**bikeshare_2** is © 2024 Przemysław Jędruch.  
Distributed under the MIT License. See [LICENSE](link-to-license) for details.

---

## About
This project is maintained by Przemysław Jędruch.  
For support or inquiries, create an issue on [GitHub Issues](link-to-issues).

Looking for professional help with data analysis projects? [Contact Us](link-to-contact).
