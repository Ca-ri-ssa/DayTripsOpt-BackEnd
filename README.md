# Day Trips Optimization Back-End
This is the Github repository of Day Trips Optimization Back-End Flask Server.

## Table Of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Run the Server](#run-the-server)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Ca-ri-ssa/DayTripsOpt-BackEnd.git
```
2. Create virtual environment and activate it:
```bash
python3 -m venv venv

# For Linux/macOS
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
Create a `.env` file to store credential and secret keys for local development. <br>
You can follow the `.env.example` file.

## Run the Server
```bash
flask run
```