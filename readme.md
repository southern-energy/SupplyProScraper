# Portal Scraper Suite

## Table of Contents

- [Portal Scraper Suite](#portal-scraper-suite)
  - [Table of Contents](#table-of-contents)
  - [Problem](#problem)
    - [Builder Portals to Scrape](#builder-portals-to-scrape)
      - [SupplyPro](#supplypro)
      - [MarkSystems](#marksystems)
      - [BuilderTrend](#buildertrend)
      - [Random Portals](#random-portals)
  - [Solution](#solution)
  - [Research Notes](#research-notes)
  - [Hyphen Solutions Scraper](#hyphen-solutions-scraper)
    - [Steps (Milestones for Completion)](#steps-milestones-for-completion)
      - [STEP 1: Login into SupplyPro ✔](#step-1-login-into-supplypro-%e2%9c%94)
      - [STEP 2: Go to Report Criteria Section ✔](#step-2-go-to-report-criteria-section-%e2%9c%94)
      - [STEP 3: Select Builder](#step-3-select-builder)
      - [STEP 4: Read Contents](#step-4-read-contents)
      - [STEP 5: Text Transformation (Data Cleaning)](#step-5-text-transformation-data-cleaning)
  - [Dependencies for Hyphen Solutions Scraper](#dependencies-for-hyphen-solutions-scraper)
  - [Pulte & Pulte Group Scraper](#pulte--pulte-group-scraper)
  - [Stanley Martin Scraper](#stanley-martin-scraper)

## Problem

I do not want to spend time skimming through portals where builders do not send us emails. We have some builders where they use the same platforms, like MarkSystems has a Dashboard we can use. But there are quite cumbersome portals that I'd rather not deal with.

### Builder Portals to Scrape

#### SupplyPro

- Dan Ryan (SC)
- Dan Ryan Builders
- Shea Homes
- Dan Ryan
- Taylor Morrison
- Toll Brothers (Raleigh)
- Toll Brothers (Charlotte)
- Davidson

#### MarkSystems

- Capitol City
- Jones Homes
- McKee
- Onsite
- Chesapeake

#### BuilderTrend

- A & G Residential LLC
- Bold Construction
- DPS Construction
- Four Seasons Contractors
- Future Homes
- Gammon Construction LLC
- Hagood Homes Inc.
- Holden Barnett Properties LLC
- Jones and Hedges Custom Build
- Robuck Design Build LLC
- Saussy Burbank - Raleigh
- Schumacher Homes
- Verde Homes
- Whitlock Builders

#### Random Portals

- KB
- Stanley Martin
- Saussy Burbank - Raleigh

## Solution

1. Codify how each of these builders structure their PO's.
2. Extract information using Python and Python Modules.
3. Organize data into an intermediate file format for possible QA.
4. Move the information into DASH.

## Research Notes

We need to see what builder portals let us export data as Python Data Frames to parse. While still having a record that a user can view, like an Excel file. Ultimately, we need to be able to compare the builder's information, to what exists in DASH.

When it comes to relevant information, we will need to distinguish these key pieces:

- Pricing
- Services
- PO's - Final and Rough
- Street Number
- Street Address
- Lot Number
- State
- City
- Zip Code
- Division
- Supervisor

Other things we will need to consider and build along the way for QA Purposes:

- Table of Services and Pricing for Builder

***

## Hyphen Solutions Scraper

### Steps (Milestones for Completion)

#### STEP 1: Login into SupplyPro ✔

1. Request the Page ✔
2. Send Login Information ✔
    1. Passes - Go to STEP 2 ✔
    2. Failure States: ✔
       1. Another user is logged in: ✔
          1. Click Forced Login Box and Resumbit ✔
          2. Passes - Go to STEP 2 ✔

#### STEP 2: Go to Report Criteria Section ✔

1. Need to Capture Session ID (Anything After <https://www.hyphensolutions.com/MH2Supply/Reports/PotentialOrders.asp?sessid=>) ✔
   1. StackOverFlow Example <https://stackoverflow.com/questions/30479290/get-current-url-from-browser-using-python>
2. Go to Future Orders Page <https://www.hyphensolutions.com/MH2Supply/Reports/PotentialOrders.asp?days=60&sessid=> ✔
   1. Passes - Go to STEP 3 ✔

#### STEP 3: Select Builder

**STEP 3 must be replicated for each builder.**

1. Interacts with dropdown menus to select builder. ✔
   - Dan Ryan (SC)
   - Dan Ryan Builders
   - Shea Homes
   - Dan Ryan
   - Taylor Morrison
   - Toll Brothers (Raleigh)
   - Toll Brothers (Charlotte)
   - Davidson
2. Interacts with dropdown menus to select 60 days from today. ✔

#### STEP 4: Read Contents

1. Reads if there are tasks a spread amongst multiple pages.
   1. Python script scrapes each page's contents into an array of arrays.
   2. Each pages' results are combined into a single data cluster to be exported.
2. If there is only one page, it will read the one page.

#### STEP 5: Text Transformation (Data Cleaning)

**STEP 5 must be replicated for each builder.**

1. The text from the result of each requires cleaning, which means PO's, Lot Numbers, and Pricing must be extracted from our soup of text. This will make importing into DASH 2.0 easier.
   - Dan Ryan (SC)
   - Dan Ryan Builders
   - Shea Homes
   - Dan Ryan
   - Taylor Morrison
   - Toll Brothers (Raleigh)
   - Toll Brothers (Charlotte)
   - Davidson

***

## Dependencies for Hyphen Solutions Scraper

- selenium
  - PIP Package Information
    - <https://pypi.org/project/selenium/>
  - Documentation
    - <https://selenium-python.readthedocs.io/>
- http_requests
  - PIP Package Information
    - <https://pypi.org/project/requests-html/>
  - Documentation
    - <https://requests-html.kennethreitz.org/>

***

## Pulte & Pulte Group Scraper

1. They can export their Schedules in either XML or Excel format.
2. Parse the Excel File for Following:
   1. Subdivision
   2. Lot Number
   3. City
3. Follow the formatting listed in the "BES Personal Procedures Reference" Google Document.

## Stanley Martin Scraper

1. You can right click a cell in a workspace.
2. Click "Export All Rows to Excel"
3. Results in a Workbook
4. Using this process, you can do this in the "Work orders by Date" workspace and the "Lots Pending Start" to have two Excel Sheets.
   1. One with Address, PO Number, Amounts, Service Conducted
   2. One with "House Plans", which we can match it DASH.
