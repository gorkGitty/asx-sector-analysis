# 📊 ASX Sector ETF Performance Analysis (2021–2025)

This Power BI project explores the performance of key **Australian sector ETFs** from **2021 to 2025**, with a focus on **sector return trends**, **volatility**, and the **influence of macroeconomic factors** such as **RBA cash rate changes** and **CPI inflation**.

---

## 🧠 Key Objectives

- Identify top- and under-performing sectors.
- Evaluate long-term sector growth and volatility.
- Analyze how **interest rates** and **inflation** impacted sector returns.
- Build an interactive Power BI dashboard suitable for professional and portfolio use.

---

## 📁 Project Structure

ASX-ETF-Analysis/
│
├── data/ # Clean datasets and extraction script
│ ├── ASX_Sector_Performance_Daily.csv
│ ├── ASX_Sector_Performance_Metrics.csv
│ ├── CPI by quarter YoY.xlsx
│ ├── RBA_Rate_Changes.csv
│ └── dataExtraction_calculation.py
│
├── visuals/ # Exported PNGs of dashboard pages
│ ├── dashboard_1.png
│ ├── dashboard_2.png
│ └── dashboard_3.png
│
├── ASX_ETF_Dashboard.pbix # Final Power BI file
└── README.md

---

## 📈 Datasets Used

| Dataset        | Description                          | Source               |
|----------------|--------------------------------------|----------------------|
| **ETF Prices** | Daily prices of ASX sector ETFs      | [Yahoo Finance](https://finance.yahoo.com/) |
| **Cash Rate**  | Historical RBA rate decisions        | [RBA.gov.au](https://www.rba.gov.au/statistics/cash-rate/)    |
| **CPI Data**   | Quarterly Australian CPI             | [ABS.gov.au](https://www.abs.gov.au)        |

---

## 🔧 Tools & Tech

- **Power BI Desktop** – Data modeling & dashboard creation
- **Python (Pandas, yfinance)** – Data extraction & cleaning
- **DAX** – Date table generation & calculated columns
- **Excel** – Pre-cleaning support

---

## 📊 Visualizations Built

### 📍 Dashboard Page 1: Sector Performance
- 📈 Normalized Closing Price (line chart)
- 📊 Cumulative Return by Sector (bar chart)
- 🕸️ Spider Chart: Return & Volatility Comparison

### 📍 Dashboard Page 2: Cash Rate Impact
- 🔬 Annualized Return vs Volatility (scatter plot)
- 📦 Boxplot of Daily Return Distribution

### 📍 Dashboard Page 3: CPI Impact
- 📉 CPI YoY Trend (line chart)
- 📊 CPI vs Sector Price Movement (clustered chart)
- 🪙 RBA Cash Rate Over Time (line chart)
- 🟦 Cash Rate vs ETF Normalized Prices (clustered chart with slicer)

---

## 🧠 Key Insights

- **Resources (MVR.AX)** led in long-term cumulative and annualized return.
- **Property & Resources sectors** reacted negatively to rate hikes in 2022–2023.
- **RBA tightening cycles** and **CPI surges** were aligned, influencing investor sentiment and sector performance.

---

## 🧩 Technical Highlights

- Created a **universal Date Table** in Power BI for cross-table syncing.
- Used **one-to-many relationships** between the Date table and all fact tables.
- Applied slicers that control visuals on a page dynamically.
- Built **multi-page dashboards**, grouped by analysis scope.

---

## 📌 How to View the Dashboard

> 🔹 Open `ASX_ETF_Dashboard.pbix` using Power BI Desktop  
> 🔹 Explore each page using the page tabs (bottom navigation)  
> 🔹 Use slicers to filter sectors and overlay macro indicators  
> 🔹 PNGs in the `visuals/` folder provide a snapshot of each page

---

## 🔮 Future Enhancements

- Deploy an interactive online version (via Power BI Service or Streamlit)

---

## 👤 Author

**Prinsh Thapa**  
🎓 Bachelor of IT  
📍 Sydney, Australia  
🔗 [LinkedIn](https://www.linkedin.com/in/prinsh-thapa/) | [GitHub](https://github.com/gorkGitty)

---

## 📃 License

This project is for educational and personal portfolio purposes.  
Please credit the author if used or extended.
