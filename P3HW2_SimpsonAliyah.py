# Aliyah Simpson
# 10/6/2026
# Use if/else statements to determine overtime pay

# Python -m streamlit run P3HW2_SimpsonAliyah.py

import streamlit as st

st.title("Paycheck calculator")

# Get Name
name = st.text_input("Enter employee name: ")

#Get hours worked
hours_worked = st.number_input("Enter hours worked: ")

#Get pay rate
pay_rate = st.number_input("Enter hourly pay rate: $")


if hours_worked > 40:
    print("You had some overtime")
    OT_hours = hours_worked - 40
    reg_hours = 40
    OT_pay = (pay_rate * 1.5) * OT_hours
    reg_pay = reg_hours * pay_rate
    pay_day = reg_pay + OT_pay

else: # Worked 40 hours or less
    print("You did not have any overtime")
    OT_hours = 0
    reg_hours = hours_worked
    OT_pay = 0
    reg_pay = reg_hours * pay_rate
    pay_day = reg_pay

# Display results
st.write(f"Hours Worked: {hours_worked:.1f}")
st.write(f"Pay Rate: ${pay_rate:.2f}")
st.write(f"Overtime hours: {OT_hours:.1f}")
st.write(f"Overtime pay: ${OT_pay:.2f}")
st.write(f"Regular pay: ${reg_pay:.2f}")
st.write(f"----------------------------------------")
st.write(f"Gross pay (Pay Day!!!): {pay_day:.2f}")