# Customer_Behavior_Analysis

## Project Overview
This project analyzes 3,900 customer transactions to explore shopping behavior, spending patterns, product performance, and subscription trends. Using Python for data cleaning, PostgreSQL for business analysis, and Power BI for visualization, the project uncovers actionable insights for improved customer engagement strategies.


The project combines **Python (Data Cleaning & Feature Engineering)**, **PostgreSQL (Business Analysis)**, and **Power BI (Visualization Dashboard)**.


## 📂 Dataset Information

* **Total Records:** 3,900
* **Total Features:** 18
* **Missing Values:** 37 (Review Rating column)

### Key Features

**Customer Demographics**

* Age
* Gender
* Location
* Subscription Status

**Purchase Details**

* Item Purchased
* Category
* Purchase Amount
* Season
* Size
* Color

**Shopping Behavior**

* Discount Applied
* Promo Code Used
* Previous Purchases
* Frequency of Purchases
* Review Rating
* Shipping Type

## 🧹 Data Cleaning & Preparation (Python)

Data preprocessing was performed using **Pandas**:

* Loaded dataset and performed initial exploration (`df.info()`, `df.describe()`)
* Handled missing values in **Review Rating** using median imputation by category
* Standardized column names to `snake_case`
* Created new features:

  * `age_group` (binned customer ages)
  * `purchase_frequency_days`
* Removed redundant columns (`promo_code_used`)
* Exported cleaned dataset to **PostgreSQL** for SQL-based analysis

## 🗄️ SQL Business Analysis (PostgreSQL)

Structured queries were written to answer key business questions:

* Revenue comparison by **Gender**
* Identification of **High-Spending Discount Users**
* Top 5 Products by **Average Rating**
* Shipping Type comparison (Standard vs Express)
* Subscriber vs Non-Subscriber revenue analysis
* Discount-dependent products
* Customer segmentation (New, Returning, Loyal)
* Top 3 products per category
* Repeat buyers & subscription relationship
* Revenue contribution by age group

## 📊 Power BI Dashboard

An interactive dashboard was created to visualize:

* Total Customers
* Average Purchase Amount
* Revenue by Category
* Sales by Category
* Revenue by Age Group
* Subscription Distribution
* Shipping Preferences


## 💡 Key Insights

* Loyal customers form the largest customer segment.
* Express shipping users have slightly higher average purchase values.
* Certain products show high dependency on discounts.
* Subscription adoption does not significantly change average spending.
* Young adults contribute the highest revenue among age groups.

## 🚀 Business Recommendations

* Increase subscription adoption through exclusive benefits.
* Strengthen loyalty programs to convert returning customers into loyal ones.
* Optimize discount strategies to protect margins.
* Promote top-rated and best-selling products in campaigns.
* Target high-revenue age groups and express-shipping users.

## 🛠️ Tech Stack

* **Python** (Pandas, Data Cleaning, Feature Engineering)
* **PostgreSQL** (SQL Analysis)
* **Power BI** (Interactive Dashboard)



