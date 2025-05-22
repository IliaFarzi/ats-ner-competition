import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("../data/source-data/UpdatedResumeDataSet.csv")

# Step 2: Shuffle and split the data
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
test_df = df_shuffled.iloc[:40]      # First 40 for test
train_df = df_shuffled.iloc[40:]     # The rest for train

# Step 3: Replace all line breaks with literal \n
def flatten_resume(text: str) -> str:
    return text.replace("\r", "\\n").replace("\n", "\\n").strip()

# Step 4: Write test.txt
with open("../data/processed/test.txt", "w", encoding="utf-8") as test_file:
    for resume in test_df["Resume"]:
        test_file.write(flatten_resume(resume) + "\n")

# Step 5: Write train.txt
with open("../data/processed/train.txt", "w", encoding="utf-8") as train_file:
    for resume in train_df["Resume"]:
        train_file.write(flatten_resume(resume) + "\n")

print("✅ Done! Both train.txt and test.txt have flattened, one-line resumes with \\n instead of real newlines.")
