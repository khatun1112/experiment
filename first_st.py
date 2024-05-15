# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# from datetime import datetime

# month_to_number = {
#     'January': 1, 'February': 2, 'March': 3, 'April': 4,
#     'May': 5, 'June': 6, 'July': 7, 'August': 8,
#     'September': 9, 'October': 10, 'November': 11, 'December': 12
# }

# data = {
#     'year': np.random.choice(range(2015, 2025), size=1000),
#     'month': np.random.choice(list(month_to_number.values()), size=1000),
#     'brandname': np.random.choice(['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE', 'BrandF', 'BrandG', 'BrandH', 'BrandI', 'BrandJ'], size=1000),
#     'invoice_sales': np.random.randint(500, 20000, size=1000)
# }

# df_large = pd.DataFrame(data)

# st.title('Sales Data Analysis')

# selected_brand = st.sidebar.selectbox('Select Brand', ['All'] + df_large['brandname'].unique().tolist())
# min_date = st.sidebar.date_input('Min Date', datetime(2015, 1, 1))
# max_date = st.sidebar.date_input('Max Date', datetime(2024, 12, 31))
# frequency = st.sidebar.selectbox('Select Frequency', ['Monthly', 'Yearly'])

# filtered_df = df_large.copy()
# if selected_brand != 'All':
#     filtered_df = filtered_df[filtered_df['brandname'] == selected_brand]
# filtered_df['date'] = pd.to_datetime(filtered_df[['year', 'month']].assign(day=1))
# filtered_df = filtered_df[(filtered_df['date'] >= pd.to_datetime(min_date)) & (filtered_df['date'] <= pd.to_datetime(max_date))]

# if frequency == 'Monthly':
#     grouped_df = filtered_df.groupby(['date']).sum().reset_index()
#     x_label = 'date'
# elif frequency == 'Yearly':
#     grouped_df = filtered_df.groupby(['year']).sum().reset_index()
#     grouped_df['date'] = pd.to_datetime(grouped_df['year'], format='%Y')
#     x_label = 'date'

# fig_1 = px.line(grouped_df, x=x_label, y='invoice_sales', title=f'Sales Trend for {selected_brand} ({frequency})')
# fig_1.update_xaxes(title='Date' if frequency == 'Monthly' else 'Year')
# fig_1.update_yaxes(title='Sales')
# st.plotly_chart(fig_1)






# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# from datetime import datetime

# month_to_number = {
#     'January': 1, 'February': 2, 'March': 3, 'April': 4,
#     'May': 5, 'June': 6, 'July': 7, 'August': 8,
#     'September': 9, 'October': 10, 'November': 11, 'December': 12
# }

# data = {
#     'year': np.random.choice(range(2015, 2025), size=1000),
#     'month': np.random.choice(list(month_to_number.values()), size=1000),
#     'brandname': np.random.choice(['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE', 'BrandF', 'BrandG', 'BrandH', 'BrandI', 'BrandJ'], size=1000),
#     'invoice_sales': np.random.randint(500, 20000, size=1000)
# }

# df_large = pd.DataFrame(data)

# st.title('Sales Data Analysis')

# selected_brand = st.sidebar.selectbox('Select Brand', df_large['brandname'].unique().tolist())
# min_date = st.sidebar.date_input('Min Date', datetime(2015, 1, 1))
# max_date = st.sidebar.date_input('Max Date', datetime(2024, 12, 31))
# frequency = st.sidebar.selectbox('Select Frequency', ['Monthly', 'Yearly'])

# filtered_df = df_large.copy()
# if selected_brand != 'All':
#     filtered_df = filtered_df[filtered_df['brandname'] == selected_brand]
# else:
#     selected_brand = 'All'

# filtered_df['date'] = pd.to_datetime(filtered_df[['year', 'month']].assign(day=1))
# filtered_df = filtered_df[(filtered_df['date'] >= pd.to_datetime(min_date)) & (filtered_df['date'] <= pd.to_datetime(max_date))]

# if frequency == 'Monthly':
#     grouped_df = filtered_df.groupby(['date']).sum().reset_index()
#     x_label = 'date'
# elif frequency == 'Yearly':
#     grouped_df = filtered_df.groupby(['date']).sum().reset_index()
#     x_label = 'date'
# fig_1 = px.line(grouped_df, x=x_label, y='invoice_sales', title=f'Sales Trend for {selected_brand} ({frequency})')
# fig_1.update_xaxes(title='Date' if frequency == 'Monthly' else 'Year')
# fig_1.update_yaxes(title='Sales')
# st.plotly_chart(fig_1)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

np.random.seed(42)
month_to_number = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}

data = {
    'year': np.random.choice(range(2015, 2025), size=1000),
    'month': np.random.choice(list(month_to_number.values()), size=1000),
    'brandname': np.random.choice(['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE', 'BrandF', 'BrandG', 'BrandH', 'BrandI', 'BrandJ'], size=1000),
    'invoice_sales': np.random.randint(500, 20000, size=1000)
}

df_large = pd.DataFrame(data)

st.title('Sales Data Analysis')

selected_brands = st.sidebar.multiselect('Select Brands', ['All'] + df_large['brandname'].unique().tolist())
min_date = st.sidebar.date_input('Min Date', datetime(2015, 1, 1))
max_date = st.sidebar.date_input('Max Date', datetime(2024, 12, 31))
frequency = st.sidebar.selectbox('Select Frequency', ['Monthly', 'Yearly'])

filtered_df = df_large.copy()
if selected_brands:
    filtered_df = filtered_df[filtered_df['brandname'].isin(selected_brands)]

filtered_df['date'] = pd.to_datetime(filtered_df[['year', 'month']].assign(day=1))
filtered_df = filtered_df[(filtered_df['date'] >= pd.to_datetime(min_date)) & (filtered_df['date'] <= pd.to_datetime(max_date))]

if frequency == 'Monthly':
    grouped_df = filtered_df.groupby(['date', 'brandname']).sum().reset_index()
    x_label = 'date'
elif frequency == 'Yearly':
    grouped_df = filtered_df.groupby(['date', 'brandname']).sum().reset_index()
    x_label = 'date'

fig_1 = px.line(grouped_df, x=x_label, y='invoice_sales', color='brandname', 
                title=f'Sales Trend for {", ".join(selected_brands)} ({frequency})')
fig_1.update_xaxes(title='Date' if frequency == 'Monthly' else 'Year')
fig_1.update_yaxes(title='Sales')
st.plotly_chart(fig_1)