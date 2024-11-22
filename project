"""
Name: Muna Mohamed
CS230: Section 5
Data: fast_food_usa.csv
"""

# Importing libraries 
import streamlit as st
import pandas as pd
import pydeck as pdk 
import matplotlib.pyplot as plt

# Function to read and load the data
@st.cache_data # This is to save filter and data changed in the browser
def fetch_data(file_location):
    return pd.read_csv(file_location)

# Reading in the fast_food_usa.csv
dataset = fetch_data("fast_food_usa_cleaned.csv")




# ======================================================== #
# Section 1: Restaurant Counts Across States and Cities
# ======================================================== #

# Creating title and subheader
st.title("Fast Food Insights - USA")
st.subheader("Q1: Which cities in a given state have the most fast-food restaurants?")

# Adding filter for the bar chart
col1, col2 = st.columns(2)
with col1:
    x_axis_option = st.selectbox(
        "Choose X-axis for the Bar Chart",
        ["City", "State"],  # Default starts with City when you open app
        index=0  # Ensures "City" is pre-selected when you open app
    )
with col2:
    filter_option = st.selectbox(
        "Choose a filter category",
        ["State", "City"],  # Default starts with State
        index=0  # Ensures "State" is pre-selected
    )

# Display the selected state filter as default
filter_value = st.selectbox(
    f"Select {filter_option}",
    options=["All"] + sorted(dataset[filter_option].unique()),
    index=1  # Ensures the first state is pre-selected
)

# Apply the filter to the dataset
if filter_value != "All":
    filtered_data = dataset[dataset[filter_option] == filter_value]
else:
    filtered_data = dataset

# Group and summarize restaurant count
summary = (
    filtered_data.groupby(x_axis_option)
    .size()
    .reset_index(name="Count")
)

# Bar Chart
if not summary.empty:
    # Function to adjust figure size based on the number of bars
    num_bars = len(summary)
    fig_width = max(8, num_bars * 0.25)  # Minimum scale is 8 and then the chart extends based on how many bars there are
    fig, ax = plt.subplots(figsize=(fig_width, 6))  # Fix width/height based on number of bars
    # Create the bar chart
    ax.bar(summary[x_axis_option], summary["Count"], color='skyblue')
    ax.set_title(f"Fast Food Restaurant Counts by {x_axis_option}", fontsize=16)
    ax.set_xlabel(x_axis_option, fontsize=14)
    ax.set_ylabel("Restaurant Count", fontsize=14)
    ax.bar_label(ax.containers[0], label_type='edge', fontsize=10)
    plt.xticks(rotation=90, ha='right')  # Rotate x axis for easier reading

    # add the bar chart into streamlit
    st.pyplot(fig)
else:
    st.write("No records found")

# Display results in table format
st.write("Below are the restaurant counts based on your filter selections:")
st.dataframe(summary)






#============================================================#
# Section 2: Where are the locations of a specific restaurant chain?
#============================================================#

# Creating section in streamlit app where we will look at locations of specific restaurant chains
st.subheader("Q2: Where are the locations of a specific restaurant chain?")

# Adding a checkbox to filter restaurants with more than 150 locations
filter_150_plus = st.checkbox("Show only restaurants with more than 150 locations")

# Setting clause for restaurant location count based on the checkbox
restaurant_counts = dataset["Restaurant Name"].value_counts()
if filter_150_plus:
    popular_restaurants = restaurant_counts[restaurant_counts > 150].index
else:
    popular_restaurants = restaurant_counts[restaurant_counts >= 50].index

# Creating filter to select a restaurants chain/name (.unique() so there are no duplicates)
restaurant_name = st.selectbox(
    "Choose a restaurant chain:",
    sorted(dataset["Restaurant Name"].unique())
)

# Filter the dataset for the selected restaurant chain/name from filter
restaurant_locations = dataset[dataset["Restaurant Name"] == restaurant_name]

# Check if there are any locations for the selected restaurant in the filter
if not restaurant_locations.empty:
    st.write(f"Displaying locations for: {restaurant_name}")
    
    # Map visualization using pydeck
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=restaurant_locations["Latitude"].mean(),
            longitude=restaurant_locations["Longitude"].mean(),
            zoom=4,
            pitch=0
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=restaurant_locations,
                get_position=["Longitude", "Latitude"],
                get_radius=5000,
                get_color=[255, 0, 0],
                pickable=True
            )
        ]
    ))
else:
    st.write("No locations for the selected restaurant.")




#============================================================#
# Section 3: What is the distribution of fast food restaurants across a specific state?
#============================================================#

# Creating subheader for section 3 in Streamlit app
st.subheader("Q3: What is the distribution of fast food restaurants across a specific state?")

# Dropdown filter to select a state
selected_state = st.selectbox(
    "Choose a state:",
    sorted(dataset["State"].unique())
)

# Filter dataset by the selected state from filter
state_data = dataset[dataset["State"] == selected_state]

# Optional filter for a specific restaurant within the state
restaurant_filter = st.checkbox("Filter by a specific restaurant?")
if restaurant_filter:
    selected_restaurant = st.selectbox(
        "Choose a restaurant:",
        sorted(state_data["Restaurant Name"].unique())
    )
    state_data = state_data[state_data["Restaurant Name"] == selected_restaurant]

# Check if there is data for the selected filters
if not state_data.empty:
    st.write(f"Displaying fast food restaurants in {selected_state}")
    
    if restaurant_filter:
        st.write(f"Filtered for: {selected_restaurant}")

    # Map visualization using pydeck
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=state_data["Latitude"].mean(),
            longitude=state_data["Longitude"].mean(),
            zoom=6,
            pitch=0
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=state_data,
                get_position=["Longitude", "Latitude"],
                get_radius=3000,
                get_color=[0, 0, 255],
                pickable=True
            )
        ]
    ))
else:
    st.write("No data available for the selected filters.")
