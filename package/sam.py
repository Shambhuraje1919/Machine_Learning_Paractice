import streamlit as st
import pandas as pd
from streamlit_geolocation import streamlit_geolocation

st.title("My Location Map")

location = streamlit_geolocation()

if location and location["latitude"] is not None:
    lat = location["latitude"]
    lon = location["longitude"]

    st.success("Location fetched successfully ✅")
    st.write(f"Latitude: {lat}, Longitude: {lon}")

    data = pd.DataFrame({
        "lat": [lat],
        "lon": [lon]
    })

    st.map(data)

else:
    st.warning("⚠️ Please allow location access and click the button")