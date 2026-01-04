import streamlit as st
from datetime import datetime
import time
from dateutil.relativedelta import relativedelta

st.title("⏳ Countdown Timer ")

target_date = st.datetime_input("Select target date & time")

placeholder = st.empty()


while True:
        now = datetime.now()

        if target_date <= now:
            placeholder.subheader("🎉 Time completed!")
            break

        diff = relativedelta(target_date, now)

        placeholder.subheader(
            f"{diff.years} years "
            f"{diff.months} months "
            f"{diff.days} days "
            f"{diff.hours} hours "
            f"{diff.minutes} minutes "
            f"{diff.seconds} seconds"
        )

        time.sleep(1)
