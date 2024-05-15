# import streamlit as st
# import pandas as pd
# data = { "id": [1, 2, 3, 4],
#         "date": ["24-05-01", "24-05-02", 
#             "24-05-03", "24-05-04"],
#         "product": ["Laptop", "Smartphone", "Tablet", "Laptop"],
#         "Quantity": [2, 3, 6, 1],
#         "Unit Price": ["$1000", "$700", "$500", "$1000"],
#         "Customer ID": [101, 102, 103, 104]}
# df = pd.DataFrame(data)
# print(df)
# st.title("Sales Data Analysis")
# st.write("Original DataFrame:")
# st.write(df)

# selected_product = st.selectbox("Select a Product", df["product"].unique())
# filtered_df = df[df["product"] == selected_product]

# st.write("Filtered DataFrame:")
# st.write(filtered_df)


import streamlit as st
import pandas as pd
import plotly.express as px

data = {
    "id": [1, 2, 3, 4],
    "date": ["24-05-01", "24-05-02", "24-05-03", "24-05-04"],
    "product": ["Laptop", "Smartphone", "Tablet", "Laptop"],
    "Quantity": [2, 3, 6, 1],
    "Unit Price": ["$1000", "$700", "$500", "$1000"],
    "Customer ID": [101, 102, 103, 104]
}
df = pd.DataFrame(data)

st.title("Sales Data Analysis")
st.write("Original DataFrame:")
st.write(df)

selected_product = st.selectbox("Select a Product", df["product"].unique())
filtered_df = df[df["product"] == selected_product]

st.write("Filtered DataFrame:")
st.write(filtered_df)

# Create a bar chart
fig = px.bar(filtered_df, x="date", y="Quantity", title=f"Quantity of {selected_product} Sold Over Time")
st.plotly_chart(fig)
