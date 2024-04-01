# Assuming 'codecademylib3' is a module used in the Codecademy learning environment for specific settings
import codecademylib3 
import pandas as pd

# Load the data
ad_clicks = pd.read_csv('ad_clicks.csv')

# 1. Examine the first few rows of ad_clicks.
print(ad_clicks.head())

# 2. Your manager wants to know which ad platform is getting you the most views.
views_by_utm = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(views_by_utm)

# 3. Create a new column called is_click, which is True if ad_click_timestamp is not null.
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

# 4. We want to know the percent of people who clicked on ads from each utm_source.
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

# 5. Now let’s pivot the data
clicks_pivot = clicks_by_source.pivot(index='utm_source', columns='is_click', values='user_id').reset_index()
print(clicks_pivot)

# 6. Create a new column in clicks_pivot called percent_clicked.
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

# Analyzing an A/B Test
# 7. The column experimental_group tells us whether the user was shown Ad A or Ad B.
ab_counts = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(ab_counts)

# 8. Using the column is_click, check to see if a greater percentage of users clicked on Ad A or Ad B.
ab_clicks = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(ab_clicks)

# 9. Create two DataFrames: a_clicks and b_clicks.
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# 10. For each group, calculate the percent of users who clicked on the ad by day.
a_clicks_by_day = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
a_clicks_pivot = a_clicks_by_day.pivot(index='day', columns='is_click', values='user_id').reset_index()
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])

b_clicks_by_day = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
b_clicks_pivot = b_clicks_by_day.pivot(index='day', columns='is_click', values='user_id').reset_index()
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])

# 11. Compare the results for A and B.
print(a_clicks_pivot)
print(b_clicks_pivot)

# After examining a_clicks_pivot and b_clicks_pivot, you would then draw conclusions based on the observed click rates by day for Ad A and Ad B.
