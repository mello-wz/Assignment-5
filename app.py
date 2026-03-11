import streamlit as st
import pandas as pd
from datetime import date

if "transactions" not in st.session_state:
    try:
        st.session_state.transactions = pd.read_csv("transactions.csv")
    except FileNotFoundError:
        st.session_state.transactions = pd.DataFrame(columns=["Date", "Description", "Amount", "Category"])
 
st.title("Student Weekly Allowance Tracker")

#my sidebar

st.sidebar.header("Settings")
name = st.sidebar.text_input("Your Name")
weekly_budget = st.sidebar.number_input("Weekly Budget", min_value=0, value=1500)
savings_goal = st.sidebar.number_input("Savings Goal")

#tabs
tab1, tab2, tab3, tab4 = st.tabs(["Add Transaction", "History", "Analytics", "About"])

#sample data
try:
    df = pd.read_csv("transactions.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Description", "Amount", "Category"])


# tab 1 - add transaction
with tab1:
    st.header("Add a New Transaction")

    transaction_type = st.radio("Transaction Type", ("Expense (money going in)", "Income (money going out)"))

    description = st.text_input("Description")

    amount = st.number_input("Amount", min_value=0.0, format="%.2f")

    transaction_date = st.date_input("Date", value=date.today())

    category = st.selectbox("Category", ["Food", "Transport", "School Necessities", "Entertainment", "Savings"])

    recurring = st.checkbox("Recurring Transaction")

    if st.button("Add Transaction"):

        #flip amount for income
        amount_value = -amount if "Income (money going out)" in transaction_type else amount
        
        new_transaction = {
            "Date": transaction_date,
            "Description": description,
            "Amount": amount,
            "Category": category
        }

        # add new transaction to dataframe
        st.session_state.transactions = pd.concat(
            [st.session_state.transactions, pd.DataFrame([new_transaction])],
            ignore_index=True
        )

        # save to csv
        st.session_state.transactions.to_csv("transactions.csv", index=False)
        st.success("Transaction added!")


# tab 2 - history
with tab2:
    st.header("Transaction History")

    # category filter
    filter_category = st.multiselect(
        "Filter by Category",
        options=["Food", "Transportation", "School Necessities", "Entertainment"]
    )

    # apply filter dynamically
    if filter_category:
        filtered_df = st.session_state.transactions[
            st.session_state.transactions["Category"].isin(filter_category)
        ]
    else:
        filtered_df = st.session_state.transactions

    # display filtered table
    st.dataframe(filtered_df)

    uploaded = st.file_uploader("Upload CSV")

    st.download_button("Download Transactions",
        df.to_csv(),
        "transactions.csv"
        )
    
# tab 3 - analytics
with tab3:
    st.header("Financial Analytics")

    # calculate totals
    total_expenses = st.session_state.transactions[st.session_state.transactions["Amount"] > 0]["Amount"].sum()
    total_income = st.session_state.transactions[st.session_state.transactions["Amount"] < 0]["Amount"].abs().sum()
    
    remaining_allowance = weekly_budget + total_income - total_expenses
    progress = min(total_expenses / weekly_budget, 1.0) if weekly_budget > 0 else 0

    # metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Weekly Allowance", f"P {weekly_budget}")
    col2.metric("Total Expenses", f"P {total_expenses}")
    col3.metric("Remaining Money", f"P {remaining_allowance}")

    # savings Progress
    st.subheader("Savings Progress")
    st.progress(progress)

    # weekly spending trend (line chart)
    st.subheader("Weekly Spending Trend")
    if not st.session_state.transactions.empty:

        # group by date and sum expenses
        weekly_trend = st.session_state.transactions.groupby("Date")["Amount"].sum()
        st.line_chart(weekly_trend)
    else:
        st.line_chart([0])

    # category spending (bar chart)
    st.subheader("Category Spending")
    if not st.session_state.transactions.empty:
        category_spending = st.session_state.transactions.groupby("Category")["Amount"].sum()
        st.bar_chart(category_spending)
    else:
        st.bar_chart([0])

    # tips
    with st.expander("Financial Tips"):
        st.write("Try to save at least 20% of your allowance each week!")

# tab 4 - about
with tab4:
    st.header("About This App")
    st.write("""
        The Student Weekly Allowance Tracker helps students manage their weekly allowance by tracking their 
    income and expenses. It provides visual analytics, spending trends, and category breakdowns to help 
    students understand their spending habits and save money.
    """)

    st.subheader("Target Users")
    st.write("""
      This app is designed for students who receive a weekly allowance and want to manage their money more effectively. 
    It helps them track expenses, monitor spending, and make better financial decisions.
    """)

    st.subheader("Inputs Collected")
    st.write("""
    - **Transaction Type**: Expense or Income
    - **Description**: Short description of the transaction
    - **Amount**: Amount spent or received
    - **Date**: Date of the transaction
    - **Category**: Type of spending (Food, Transport, School Necessities, Entertainment, Savings)
    - **Recurring**: Whether the transaction repeats
    - **Weekly Budget**: Student's weekly allowance
    - **Savings Goal**: Target savings for the week
    """)

    st.subheader("Outputs Shown")
    st.write("""
    - **Transaction History Table**: Shows all recorded transactions
    - **Total Expenses & Remaining Allowance**
    - **Savings Progress Bar**
    - **Weekly Spending Trend Chart**
    - **Category Spending Chart**
    - **Downloadable CSV of Transactions**
    """)  