import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B"],
    "age": [20, 25]
})

# print(df)

df = pd.read_csv('C:/Users/krish/IdeaProjects/DemoProject/src/banana_quality_dataset.csv')
# print(df.head(50))
#
# df.info()

# statistics (data insights)
print(df.describe())
print(df['sample_id'].describe())
print(df[['sample_id', 'quality_score']].describe())

# returns the dimensions of the DataFrame as a tuple
print(df.shape)
print(df.shape[0])  # number of rows
print(df.shape[1])  # number of columns

# select multiple columns
print(df[['sample_id', 'rainfall_mm']])

# remove duplicates
df = pd.DataFrame({
    "name": ["A", "B", "A", "A"],
    "age": [20, 25, 20, 30]
})
print(df)
print(df.drop_duplicates())

# Remove duplicates based on specific columns:
# Keeps only one row per name
print(df.drop_duplicates(subset=["name"]))

# Controls which duplicate to keep:
print(df.drop_duplicates(keep="first"))  # default
print(df.drop_duplicates(keep="last"))
print(df.drop_duplicates(keep=False))    # remove all duplicates

# rename columns
df.rename(columns={"name": "customer_name"}, inplace=True)
print(df)

# change data types
df["age"] = df["age"].astype(str)
print(df)
print(df.info())
print(df.dtypes)

# Create new column based on condition
df["status"] = df["age"].apply(lambda x: "Adult" if int(x) >= 18 else "Minor")
print(df)

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["status"] = df["age"].apply(
    lambda x: "Adult" if x >= 18 else "Minor"
)
print(df)

# Handle NaN safely
df["age"] = pd.to_numeric(df["age"], errors="coerce")

df["status"] = df["age"].apply(
    lambda x: "Adult" if x >= 18 else "Minor" if pd.notnull(x) else "Unknown"
)

print(df)

# Merge vs Join vs Concat
print(pd.merge(df, df, on="customer_name"))   # SQL join

print(df.join(df, lsuffix="_left", rsuffix="_right") )                # index-based

print(pd.concat([df, df]))        # stacking


df = pd.DataFrame({
    "name": ["A", "B", None],
    "age": [20, None, 30]
})

print(df.isnull().sum())

print(df.fillna(0))

# convert categorical data into numeric
print(pd.get_dummies(df["name"]))

# How to normalize/scale data using Pandas
df["age"] = (df["age"] - df["age"].mean()) / df["age"].std()
print(df)

# outliers
# IQR=Q3−Q1
# Lower bound = Q1 − 1.5 × IQR
# Upper bound = Q3 + 1.5 × IQR
df = pd.DataFrame({"customer_name": ["krishanu", "sathi"],
                   "salary": [5000, 1000]})
print(df.describe())
print(df['salary'].quantile(0.25))

quantile_1 = df['salary'].quantile(0.25)
print("quantile_1", quantile_1)
quantile_3 = df['salary'].quantile(0.75)
print("quantile_3", quantile_3)
iqr = quantile_3 - quantile_1
print(iqr)

l_bnd = quantile_1 - 1.5 * iqr
print("lower_ound", l_bnd)
u_bnd = quantile_3 + 1.5 * iqr
print("upper_ound", u_bnd)

print(df['salary'].filter((df['salary'] < l_bnd) & (df['salary'] > u_bnd)))

s = 'are you #'
print(s.__contains__("#"))
print(s.find('#'))

if s.find('?') != -1:
    print(True)
else:
    print(False)