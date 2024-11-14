#!/usr/bin/env python
# coding: utf-8

# # Introduction
# I am Olaoluwa Johnson Taiwo, a final-year student at the University of Central Lancashire (UCLan), conducting a research project on the effectiveness of AI-personalised recommendation systems in enhancing customer engagement and satisfaction. This study focuses on Jumia, a leading e-commerce platform in Lagos, Nigeria, to evaluate AI-driven personalisation’s impact in an emerging market context.
# 
# # Problem Statement
# While AI-personalised recommendations have been shown to improve customer satisfaction and engagement in developed markets, limited research examines their effectiveness in Nigeria’s diverse socio-economic environment. This study explores Lagos consumers' perceptions of Jumia's AI recommendations, investigating factors such as cultural relevance, economic disparities, technological limitations, privacy concerns, and digital literacy. The analysis is guided by the Theory of Planned Behaviour (TPB), Technology Acceptance Model (TAM), and Complexity Theory to understand the individual and contextual factors that influence AI effectiveness.
# 
# # Objective of Analysis
# The main objective is to test hypotheses derived from these theories, using survey data from Jumia users in Lagos to identify key drivers and barriers to engagement and satisfaction with AI recommendations.
# 
# # Analysis Steps
# Descriptive Analysis: Demographic data of respondents, including age, income, and shopping frequency, were summarised to establish a baseline understanding of Jumia’s consumer profile and general attitudes toward AI recommendations.
# 
# - Cultural and Economic Influence Testing: Chi-Square and ANOVA tests were used to evaluate cultural and economic factors' impact on perceptions of AI recommendations. ANOVA tested income disparity’s effect on satisfaction, while Chi-Square assessed the influence of cultural relevance on engagement.
# 
# - Engagement and Satisfaction Analysis: Correlation and regression analyses assessed the direct effects of AI recommendations on customer engagement and satisfaction, supporting or rejecting hypotheses on AI's positive impact on these outcomes (H1 and H2).
# 
# - Trust and Privacy Analysis: Correlation analysis and T-tests were conducted to examine the relationships between trust, privacy concerns, and engagement. The analysis determined whether privacy concerns (H6) and trust (H5) significantly influence engagement and satisfaction, given that privacy concerns might be secondary to convenience.
# 
# - Technological Infrastructure Impact: ANOVA tested the effect of technological infrastructure limitations on perceived relevance of AI recommendations, guided by Technology Access Theory, to assess whether poor infrastructure impacts engagement and satisfaction.
# 
# - Digital Literacy and Economic Disparities: ANOVA was also used to examine whether digital literacy and economic factors (H3 and H4) influence AI acceptance and satisfaction, recognising that Lagos's unique economic challenges may moderate these relationships differently from developed markets.
# 
# - Challenges of AI Systems: Chi-Square tests and T-tests evaluated perceptions of algorithmic bias and cultural sensitivity. These analyses investigated whether bias affects perceived fairness and whether Jumia's recommendations align with local cultural values, potentially affecting AI acceptance.
# 
# - Theory of Planned Behaviour (TPB) Testing: Multiple regression analyses tested TPB-related hypotheses on the impact of attitudes, subjective norms (trust), and perceived behavioural control (data comfort) on engagement and satisfaction, aligning with TPB principles.
# 
# - Technology Acceptance Model (TAM) Testing: Multiple regression analyses examined the impact of perceived usefulness and ease of use on engagement and satisfaction. This analysis tested whether user-friendly and relevant AI recommendations enhance engagement, supporting TAM.
# 
# - Complexity Theory Analysis: MANOVA was applied to explore the combined effects of cultural, economic, and infrastructure factors on engagement and satisfaction, aligning with Complexity Theory to reveal how these interrelated factors shape AI effectiveness in Lagos.
# 
# This structured approach provides a comprehensive understanding of Jumia’s AI-driven recommendations' effectiveness and the role of local factors. Findings contribute to practical insights for adapting AI personalisation strategies in Nigeria and similar emerging markets, emphasising the need for culturally attuned, economically inclusive, and accessible AI systems.

# # SECTION 1: IMPORTING AND ASSESING DATA

# In[1]:


# Step 1: Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, pearsonr, spearmanr
from datetime import datetime

# Set visualization style for clarity
plt.style.use('ggplot')


# In[2]:


# Loading the dataset 
aidata = pd.read_excel("C:\\Users\\taiwo\\Downloads\\Aldata.xlsx")
aidata.head()


# In[3]:


aidata.info()


# In[125]:


aidata.describe()


# In[124]:


import pandas as pd

# Calculate age distribution statistics (if numeric data isn't available, we'll calculate mode and frequency for categorical age groups)
age_mode = df['What is your age group?'].mode()[0]
age_counts = df['What is your age group?'].value_counts()
age_summary = pd.DataFrame({
    'Age Statistics': ['Mode', 'Most Frequent Count'],
    'Value': [age_mode, age_counts[age_mode]]
})

# Calculate gender distribution
gender_counts = df['What is your gender?'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

# Calculate income range distribution
income_counts = df['What is your monthly income range?'].value_counts().reset_index()
income_counts.columns = ['Income Range', 'Count']

# Concatenate age, gender, and income data into a single table
demographic_summary = pd.concat([
    age_summary.set_index('Age Statistics'),  # Age mode and count
    gender_counts.set_index('Gender'),        # Gender counts
    income_counts.set_index('Income Range')   # Income range counts
], axis=1).fillna('')  # Fill NaN with blank

# Display the final demographic summary table
demographic_summary


# # SECTION 2: DATA CLEANING
# I performed preliminary data cleaning; however, additional data cleaning steps will be undertaken during the EDA and hypothesis testing phases to ensure high data quality.

# In[5]:


df= aidata

# Converting 'Start time' to datetime format and create new columns for date and day of week
df['Start time'] = pd.to_datetime(df['Start time'], errors='coerce')
df['Date'] = df['Start time'].dt.date
df['Day of Week'] = df['Start time'].dt.day_name()

# Dropping any rows with critical missing data (e.g., demographic variables that are required for analysis)
df = df.dropna(subset=['What is your age group?', 'What is your monthly income range?'])

# Previewing the data to understand its structure and check the new columns
df.head()


# # SECTION 3: EXPLORATORY DATA ANALYSIS
# During the EDA phase, I conduct a thorough analysis of the data. This includes univariate analysis to explore individual variables, bivariate analysis to examine relationships between two variables, and multivariate analysis to investigate interactions across multiple variables. These steps help uncover patterns, detect anomalies, and guide hypothesis testing.

# In[7]:


df.columns


# # 3.1. Univariate Analysis

# In[8]:


# Data Collection Trend over Days of the Week
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Day of Week', palette='Set2', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title("Data Collection Trends by Day of Week")
plt.xlabel("Day of the Week")
plt.ylabel("Count of Responses")
plt.show()


# This illustrates response patterns for the research data collected in Lagos. Thursday emerged as the peak day, with over 50 responses, suggesting that individuals in Lagos are most responsive on this day. Wednesday and Friday also show high engagement, with around 40 responses each, making them suitable secondary days for data collection. Conversely, Tuesday, Saturday, and Sunday have the lowest engagement levels, with fewer than 20 responses, indicating they may not be ideal for gathering data. Monday falls in the mid-range, offering a moderate level of responses. These trends provide valuable insights into optimal days for data collection in Lagos.

# In[9]:


# Plotting Age Group Distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='What is your age group?', palette='Blues')
plt.title('Age Group Distribution')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# This chart highlights the age demographics of participants in the Lagos-based study. The 25-34 age group dominates the sample, with over 100 responses, indicating strong engagement from young adults. The 18-24 group follows, with around 60 responses, also contributing significantly to the data pool. In contrast, the 35-44, 45-54, and 55+ age groups have minimal representation, each with fewer than 20 responses. This distribution suggests that the research primarily reflects the perspectives of younger individuals, particularly those aged 18-34, while older age groups are underrepresented. These insights are valuable for understanding the sample’s demographic profile.

# In[10]:


# Plotting Gender Distribution
plt.figure(figsize=(6, 6))
sns.countplot(data=df, x='What is your gender?', palette='Greens')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# This chart illustrates the gender breakdown of participants in the Lagos-based research. Women make up the majority, with slightly over 100 responses, while men have around 80 responses. This suggests a higher level of engagement from female participants compared to male participants. The difference in gender representation indicates that the study’s findings may slightly lean toward the perspectives of women. Understanding this distribution is important for interpreting the results, as it highlights the gender dynamics within the respondent pool and provides context for the data's reliability across genders.

# In[11]:


# Plotting Monthly Income Range Distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='What is your monthly income range?', palette='Oranges')
plt.title('Monthly Income Range Distribution')
plt.xlabel('Count')
plt.ylabel('Income Range')
plt.show()


# The chart reveals the income demographics of participants in the Lagos-based research. The ₦50,000-₦100,000 income range has the highest representation, with around 60 responses, indicating this is the most common income bracket among respondents. Following closely, the "Below ₦50,000" and "₦100,000-₦200,000" ranges each have approximately 40-50 responses, showing that a significant portion of participants falls within low to moderate income levels. The ₦200,000-₦500,000 range is less represented, with about 20 responses, and the "Above ₦500,000" range has minimal responses, indicating a smaller high-income demographic. This distribution highlights the predominant income brackets and provides insight into the economic profile of the sample.

# In[12]:


# Shopping Frequency Distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='How frequently do you shop on Jumia?', palette='PuBuGn')
plt.title('Shopping Frequency Distribution')
plt.xlabel('Shopping Frequency')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# With most respondents indicating they shop "when needed," it suggests a utilitarian approach to online shopping among Jumia customers in Lagos. For AI recommendations, this insight is critical as it indicates the need for need-based, contextually relevant recommendations rather than generic or high-frequency promotional content.

# In[13]:


# Satisfaction with Personalized Recommendations
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='How satisfied are you with the personalised recommendations provided by Jumia?', palette='YlOrRd')
plt.title('Satisfaction with Personalised Recommendations')
plt.xlabel('Satisfaction Level')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# The chart shows that most respondents are either "Satisfied" or "Very satisfied" with the personalized recommendations they receive, which indicates that Jumia's AI system has generally been effective in enhancing customer satisfaction. This high satisfaction level suggests that personalized recommendations contribute positively to user experience, potentially fostering repeat purchases and customer loyalty, which aligns with the objective of increasing engagement on Jumia's platform.

# In[14]:


# Plot how well AI recommendations reflect customer preferences
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="How well do you think Jumia's personalised recommendations reflect your personal preferences and lifestyle?", palette='coolwarm')
plt.title("Alignment of AI Recommendations with Customer Preferences")
plt.xlabel("Reflection of Personal Preferences")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()


# Most respondents feel that recommendations align "Somewhat well" or "Extremely well" with their personal preferences. This suggests that Jumia's AI algorithms successfully capture user interests and behavioral data to provide relevant product suggestions. The high alignment with customer preferences reflects the effectiveness of Jumia’s recommendation system in delivering tailored experiences, which is likely to improve engagement and interaction with the platform, a key focus of your study.

# In[15]:


# Digital Literacy (Comfort Level with AI Recommendations)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Are you comfortable with Jumia using your browsing and purchasing data to provide personalised recommendations?", palette='OrRd')
plt.title("Comfort Level with Data Usage in AI Recommendations")
plt.xlabel("Comfort Level")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()


# The majority of respondents indicated that they are "Somewhat comfortable" or "Very comfortable" with their data being used for AI recommendations. This suggests that data privacy concerns, while present, may not be a major hindrance to AI adoption for many users in Lagos. However, a portion of respondents still feel neutral or uncomfortable, indicating a need for transparency and trust-building initiatives. Addressing these concerns is essential for maintaining consumer trust, especially as your research highlights privacy as a challenge in emerging markets.

# In[16]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='How often do you interact with Jumia’s AI-personalised product recommendations (e.g., clicking on recommended items, adding items to cart)?', palette="viridis")
plt.title("Interaction Frequency with AI Recommendations")
plt.xlabel("Count")
plt.ylabel("Interaction Frequency")
plt.show()


# The most common response is "Sometimes," indicating that while users do engage with AI recommendations, they may not do so consistently. This suggests that there might be an opportunity to make AI recommendations more engaging or relevant to increase interaction frequency.

# In[17]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Have Jumia’s personalised recommendations influenced your decision to make repeat purchases on the platform?', palette="Blues")
plt.title("Influence of AI Recommendations on Repeat Purchases")
plt.xlabel("Count")
plt.ylabel("Influence Level")
plt.show()


#  A significant number of users indicated that AI recommendations somewhat or very much influence their repeat purchase decisions. This demonstrates the effectiveness of personalised recommendations in fostering customer loyalty and increasing repeat transactions on Jumia.

# In[18]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="To what extent do you feel that Jumia's personalised recommendations reflect the cultural realities of living in Lagos?", palette="crest")
plt.title("Cultural Relevance of AI Recommendations")
plt.xlabel("Count")
plt.ylabel("Cultural Relevance Level")
plt.show()


# Many users feel that AI recommendations reflect their cultural preferences "Moderately well" to "Very well," showing that Jumia’s AI has been somewhat successful in tailoring suggestions to local cultural norms. However, there is room for improvement in making recommendations more culturally aligned.

# In[19]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="To what extent do you feel that Jumia's personalised recommendations reflect the economic realities of living in Lagos?", palette="cividis")
plt.title("Economic Relevance of AI Recommendations")
plt.xlabel("Count")
plt.ylabel("Economic Relevance Level")
plt.show()


# Respondents generally view AI recommendations as "Moderately well" or "Very well" aligned with their economic status, which is essential in Lagos’s emerging market. Personalisation that considers economic factors can enhance relevance and customer satisfaction.

# In[20]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="Are you concerned about the privacy of your personal data used for Jumia's personalised recommendations?", palette="rocket")
plt.title("Privacy Concerns about AI Recommendations")
plt.xlabel("Count")
plt.ylabel("Privacy Concern Level")
plt.show()


# Many respondents express "Very concerned" and "Somewhat concerned" views regarding data privacy. This highlights the need for Jumia to emphasize data transparency and build trust, ensuring customers feel secure with AI-powered personalization.

# In[21]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="Would clearer information on how your data is used improve your trust in Jumia's AI system?", palette="mako")
plt.title("Trust Improvement with Data Transparency")
plt.xlabel("Count")
plt.ylabel("Trust Level")
plt.show()


# A majority believe that data transparency would significantly improve their trust in AI recommendations. This reinforces the importance of transparency for Jumia to enhance customer confidence in its recommendation algorithms.

# In[22]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="Are you comfortable with Jumia using your browsing and purchasing data to provide personalised recommendations?", palette="flare")
plt.title("Comfort Level with Data Usage for Personalization")
plt.xlabel("Count")
plt.ylabel("Comfort Level")
plt.show()


# Most users are "Somewhat comfortable" or "Very comfortable" with data usage, suggesting an overall positive outlook on data-driven personalisation, though it still requires transparency to address concerns.

# In[23]:


# Split the responses and clean each response by stripping unwanted characters
all_challenges = df["What challenges or limitations have you experienced with Jumia's AI-personalised recommendation system? (Select all that apply)"].dropna().str.split(';').sum()
cleaned_challenges = [challenge.strip(' -') for challenge in all_challenges if challenge.strip() and challenge.lower() != 'nil']

# Count occurrences of each unique challenge after cleaning
challenge_counts = pd.Series(cleaned_challenges).value_counts()

# Plot the cleaned data
plt.figure(figsize=(12, 8))
sns.barplot(y=challenge_counts.index, x=challenge_counts.values, palette="Spectral")
plt.title("Frequency of Challenges or Limitations with AI Recommendations (Cleaned)")
plt.xlabel("Count")
plt.ylabel("Challenges or Limitations")
plt.show()


# The primary challenge noted by users is repetitive recommendations, indicating that Jumia’s AI could benefit from more varied suggestions. Privacy concerns and a lack of diversity in recommendations are also issues, aligning with the challenges mentioned in your research.

# In[24]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="Jumia’s AI-personalised recommendations have made you more loyal to the platform", palette="coolwarm")
plt.title("Customer Loyalty Influenced by AI Personalisation")
plt.xlabel("Count")
plt.ylabel("Customer Loyalty Level")
plt.show()


# Many respondents "Agree" or are "Neutral" regarding AI's influence on loyalty, showing that while personalisation positively affects loyalty, there is potential for Jumia to further enhance AI’s impact on customer loyalty through more targeted and engaging recommendations.

# In[25]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="How well do you think Jumia's personalised recommendations reflect your personal preferences and lifestyle?", palette="magma")
plt.title("Reflection of Personal Preferences and Lifestyle in AI Recommendations")
plt.xlabel("Count")
plt.ylabel("Reflection Level")
plt.show()


# The majority of respondents feel that the AI recommendations align "Somewhat well" with their personal preferences and lifestyle, with a substantial group indicating "Extremely well." This indicates that Jumia's AI recommendation system is generally successful in capturing relevant aspects of customers' preferences, though there remains an opportunity to fine-tune the recommendations for even greater personalisation.

# In[26]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="Do you think that your purchasing power (income) affects the relevance of the personalised recommendations provided to you?", palette="viridis")
plt.title("Influence of Purchasing Power on AI Recommendations Relevance")
plt.xlabel("Count")
plt.ylabel("Purchasing Power Influence")
plt.show()


# Many respondents acknowledge that their purchasing power somewhat influences the relevance of AI recommendations. A large group also indicated a "great" influence, which highlights the need for Jumia's AI system to continuously adjust and consider economic factors when suggesting products. This aligns with the economic challenges you identified as critical in the Lagos market, as recommendations must be tailored to align with users' spending capabilities.

# In[27]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="The AI personalised recommendations reflect your actual preferences and needs.", palette="cividis")
plt.title("Reflection of Actual Preferences and Needs in AI Recommendations")
plt.xlabel("Count")
plt.ylabel("Reflection Level")
plt.show()


# A majority of users "Agree" or "Strongly agree" that the AI recommendations reflect their actual preferences and needs, which underscores the effectiveness of Jumia’s AI system in understanding and aligning with customer desires. This also reinforces the potential for AI personalisation to enhance customer satisfaction and engagement by catering to actual user preferences accurately.

# In[28]:


import matplotlib.pyplot as plt
import seaborn as sns

# Set up a 4x3 grid for subplots
fig, axes = plt.subplots(4, 3, figsize=(20, 20))
fig.suptitle("Demographic and Core Variable Visualisations", fontsize=16)

# Satisfaction with Personalized Recommendations
sns.countplot(data=df, x='How satisfied are you with the personalised recommendations provided by Jumia?', palette='YlOrRd', ax=axes[0, 0])
axes[0, 0].set_title('Satisfaction with Personalised Recommendations')
axes[0, 0].set_xlabel('Satisfaction Level')
axes[0, 0].set_ylabel('Count')
axes[0, 0].tick_params(axis='x', rotation=45)

# Reflection of AI Recommendations on Personal Preferences
sns.countplot(data=df, x="How well do you think Jumia's personalised recommendations reflect your personal preferences and lifestyle?", palette='coolwarm', ax=axes[0, 1])
axes[0, 1].set_title("Reflection of Personal Preferences in AI")
axes[0, 1].set_xlabel("Reflection Level")
axes[0, 1].set_ylabel("Count")
axes[0, 1].tick_params(axis='x', rotation=45)

# Comfort Level with Data Usage in AI
sns.countplot(data=df, x="Are you comfortable with Jumia using your browsing and purchasing data to provide personalised recommendations?", palette='OrRd', ax=axes[0, 2])
axes[0, 2].set_title("Comfort Level with Data Usage")
axes[0, 2].set_xlabel("Comfort Level")
axes[0, 2].set_ylabel("Count")
axes[0, 2].tick_params(axis='x', rotation=45)

# Cultural Relevance of AI Recommendations
sns.countplot(data=df, y="To what extent do you feel that Jumia's personalised recommendations reflect the cultural realities of living in Lagos?", palette="crest", ax=axes[1, 0])
axes[1, 0].set_title("Cultural Relevance")
axes[1, 0].set_xlabel("Count")
axes[1, 0].set_ylabel("Cultural Relevance Level")

# Economic Relevance of AI Recommendations
sns.countplot(data=df, y="To what extent do you feel that Jumia's personalised recommendations reflect the economic realities of living in Lagos?", palette="cividis", ax=axes[1, 1])
axes[1, 1].set_title("Economic Relevance")
axes[1, 1].set_xlabel("Count")
axes[1, 1].set_ylabel("Economic Relevance Level")

# Privacy Concerns about AI Recommendations
sns.countplot(data=df, y="Are you concerned about the privacy of your personal data used for Jumia's personalised recommendations?", palette="rocket", ax=axes[1, 2])
axes[1, 2].set_title("Privacy Concerns")
axes[1, 2].set_xlabel("Count")
axes[1, 2].set_ylabel("Privacy Concern Level")

# Trust Improvement with Data Transparency
sns.countplot(data=df, y="Would clearer information on how your data is used improve your trust in Jumia's AI system?", palette="mako", ax=axes[2, 0])
axes[2, 0].set_title("Trust Improvement with Transparency")
axes[2, 0].set_xlabel("Count")
axes[2, 0].set_ylabel("Trust Level")

# Customer Loyalty Influenced by AI Personalisation
sns.countplot(data=df, y="Jumia’s AI-personalised recommendations have made you more loyal to the platform", palette="coolwarm", ax=axes[2, 1])
axes[2, 1].set_title("Customer Loyalty")
axes[2, 1].set_xlabel("Count")
axes[2, 1].set_ylabel("Loyalty Level")

# Influence of Purchasing Power on AI Recommendations
sns.countplot(data=df, y="Do you think that your purchasing power (income) affects the relevance of the personalised recommendations provided to you?", palette="viridis", ax=axes[2, 2])
axes[2, 2].set_title("Purchasing Power Influence")
axes[2, 2].set_xlabel("Count")
axes[2, 2].set_ylabel("Purchasing Power Influence")

# Reflection of Actual Preferences and Needs in AI Recommendations
sns.countplot(data=df, y="The AI personalised recommendations reflect your actual preferences and needs.", palette="cividis", ax=axes[3, 0])
axes[3, 0].set_title("Reflection of Actual Preferences and Needs")
axes[3, 0].set_xlabel("Count")
axes[3, 0].set_ylabel("Reflection Level")

# Challenges with AI Recommendations
all_challenges = df["What challenges or limitations have you experienced with Jumia's AI-personalised recommendation system? (Select all that apply)"].dropna().str.split(';').sum()
cleaned_challenges = [challenge.strip(' -') for challenge in all_challenges if challenge.strip() and challenge.lower() != 'nil']
challenge_counts = pd.Series(cleaned_challenges).value_counts()
sns.barplot(y=challenge_counts.index, x=challenge_counts.values, palette="Spectral", ax=axes[3, 1])
axes[3, 1].set_title("Challenges with AI Recommendations")
axes[3, 1].set_xlabel("Count")
axes[3, 1].set_ylabel("Challenges")

# Additional Core Variable - Reflection on Income Relevance
sns.countplot(data=df, y="Do you think that your purchasing power (income) affects the relevance of the personalised recommendations provided to you?", palette="Blues", ax=axes[3, 2])
axes[3, 2].set_title("Reflection on Income Relevance")
axes[3, 2].set_xlabel("Count")
axes[3, 2].set_ylabel("Income Relevance Level")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


# In[29]:


import matplotlib.pyplot as plt
import seaborn as sns

# 1. 2x2 Grid (Demographic Overview)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Age Group Distribution - Bar chart
sns.countplot(data=df, x='What is your age group?', ax=axes[0, 0], palette='Paired')
axes[0, 0].set_title('Age Group Distribution')
axes[0, 0].set_xlabel('Age Group')
axes[0, 0].set_ylabel('Count')
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=45, ha='right')

# Gender Distribution - Pie chart with distinct colors
gender_counts = df['What is your gender?'].value_counts()
axes[0, 1].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, 
               colors=['#FF9999', '#66B2FF'], wedgeprops={'edgecolor': 'black'})
axes[0, 1].set_title('Gender Distribution')

# Monthly Income Range Distribution - Bar chart
sns.countplot(data=df, x='What is your monthly income range?', ax=axes[1, 0], palette='mako')
axes[1, 0].set_title('Monthly Income Range Distribution')
axes[1, 0].set_xlabel('Monthly Income Range')
axes[1, 0].set_ylabel('Count')
axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=45, ha='right')

# Shopping Frequency on Jumia - Bar chart
sns.countplot(data=df, x='How frequently do you shop on Jumia?', ax=axes[1, 1], palette='crest')
axes[1, 1].set_title('Shopping Frequency on Jumia')
axes[1, 1].set_xlabel('Shopping Frequency')
axes[1, 1].set_ylabel('Count')
axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.show()


# In[30]:


# 2. 2x2 Grid (Engagement and Satisfaction with AI Recommendations)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Satisfaction with Personalized Recommendations
sns.countplot(data=df, x='How satisfied are you with the personalised recommendations provided by Jumia?', ax=axes[0, 0], palette='YlOrRd')
axes[0, 0].set_title('Satisfaction with Personalized Recommendations')
axes[0, 0].set_xlabel('')
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=45, ha='right')

# Alignment of AI Recommendations with Customer Preferences
sns.countplot(data=df, x="How well do you think Jumia's personalised recommendations reflect your personal preferences and lifestyle?", ax=axes[0, 1], palette='coolwarm')
axes[0, 1].set_title("Alignment of AI Recommendations with Customer Preferences")
axes[0, 1].set_xlabel('')
axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=45, ha='right')

# Comfort Level with Data Usage in AI Recommendations
sns.countplot(data=df, x="Are you comfortable with Jumia using your browsing and purchasing data to provide personalised recommendations?", ax=axes[1, 0], palette='OrRd')
axes[1, 0].set_title("Comfort Level with Data Usage in AI Recommendations")
axes[1, 0].set_xlabel('')
axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=45, ha='right')

# Interaction Frequency with AI Recommendations
sns.countplot(data=df, x="How often do you interact with Jumia’s AI-personalised product recommendations (e.g., clicking on recommended items, adding items to cart)?", ax=axes[1, 1], palette='coolwarm')
axes[1, 1].set_title("Interaction Frequency with AI Recommendations")
axes[1, 1].set_xlabel('')
axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.show()


# In[31]:


# 3. 2x2 Grid (Cultural, Economic, and Privacy Concerns)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Customer Loyalty Influenced by AI Personalisation
sns.countplot(data=df, y="Jumia’s AI-personalised recommendations have made you more loyal to the platform", ax=axes[0, 0], palette="YlGnBu")
axes[0, 0].set_title("Customer Loyalty Influenced by AI Personalisation")
axes[0, 0].set_ylabel('')

# Reflection of Actual Preferences and Needs
sns.countplot(data=df, y="The AI personalised recommendations reflect your actual preferences and needs.", ax=axes[0, 1], palette="magma")
axes[0, 1].set_title("Reflection of Actual Preferences and Needs in AI Recommendations")
axes[0, 1].set_ylabel('')

# Cultural Relevance of AI Recommendations
sns.countplot(data=df, y="To what extent do you feel that Jumia's personalised recommendations reflect the cultural realities of living in Lagos?", ax=axes[1, 0], palette="crest")
axes[1, 0].set_title("Cultural Relevance of AI Recommendations")
axes[1, 0].set_ylabel('')

# Economic Relevance of AI Recommendations
sns.countplot(data=df, y="To what extent do you feel that Jumia's personalised recommendations reflect the economic realities of living in Lagos?", ax=axes[1, 1], palette="cividis")
axes[1, 1].set_title("Economic Relevance of AI Recommendations")
axes[1, 1].set_ylabel('')

plt.tight_layout()
plt.show()


# In[32]:


import matplotlib.pyplot as plt
import seaborn as sns


# 4. 2x2 Grid (Challenges and Specific Preferences for AI)
fig, axes = plt.subplots(2, 2, figsize=(14, 15))

# Privacy Concerns about AI Recommendations
sns.countplot(data=df, y="Are you concerned about the privacy of your personal data used for Jumia's personalised recommendations?", ax=axes[0, 0], palette="rocket")
axes[0, 0].set_title("Privacy Concerns about AI Recommendations")
axes[0, 0].set_ylabel('')
axes[0, 0].set_xlabel('Count')

# Trust Improvement with Data Transparency
sns.countplot(data=df, y="Would clearer information on how your data is used improve your trust in Jumia's AI system?", ax=axes[0, 1], palette="mako")
axes[0, 1].set_title("Trust Improvement with Data Transparency")
axes[0, 1].set_ylabel('')
axes[0, 1].set_xlabel('Count')

# Influence of Purchasing Power on AI Recommendations Relevance
sns.countplot(data=df, y="Do you think that your purchasing power (income) affects the relevance of the personalised recommendations provided to you?", ax=axes[1, 0], palette="viridis")
axes[1, 0].set_title("Influence of Purchasing Power on AI Recommendations Relevance")
axes[1, 0].set_ylabel('')
axes[1, 0].set_xlabel('Count')

# Frequency of Challenges or Limitations with AI Recommendations
# Assuming "What challenges or limitations have you experienced with Jumia's AI-personalised recommendation system?" column exists in df
# If not, replace with the correct column name or data

# Cleaning and counting challenges
all_challenges = df["What challenges or limitations have you experienced with Jumia's AI-personalised recommendation system? (Select all that apply)"].dropna().str.split(';').sum()
cleaned_challenges = [challenge.strip(' -') for challenge in all_challenges if challenge.strip() and challenge.lower() != 'nil']
challenge_counts = pd.Series(cleaned_challenges).value_counts()

sns.barplot(y=challenge_counts.index, x=challenge_counts.values, palette="Spectral", ax=axes[1, 1])
axes[1, 1].set_title("Frequency of Challenges or Limitations with AI Recommendations")
axes[1, 1].set_xlabel('Count')
axes[1, 1].set_ylabel('Challenges or Limitations')

plt.tight_layout()
plt.show()


# # 3.2. Bivariate Analysis

# NOTE: To perform a comprehensive analysis, it's essential to transform categorical responses into numerical values, especially for ordinal data (i.e., data with a meaningful order but without a specific scale). This transformation, known as mapping, allows us to use statistical and machine learning techniques that require numerical input. By converting responses such as levels of satisfaction, trust, engagement, loyalty, and preference into numbers, we enable more precise calculations, comparisons, and visualisations.
# 
# Mapping is particularly critical for ordinal columns because these columns represent ordered categories that can directly influence the insights we derive from the data. For instance, without mapping, it would be challenging to quantitatively assess trends in satisfaction or trust levels, or to correlate these with other variables. This approach ensures that the analysis captures the inherent ordering in these responses (e.g., "Very dissatisfied" is less than "Neutral"), allowing for deeper statistical analysis and model training if needed.

# In[33]:


# Mapping dictionaries for some ordinal columns
satisfaction_mapping = {
    "Very dissatisfied": 1, "Dissatisfied": 2, "Neutral": 3, "Satisfied": 4, "Very satisfied": 5
}
trust_mapping = {
    "Not at all": 1, "No, not really": 2, "Neutral": 3, "Yes, somewhat": 4, "Yes, significantly": 5
}
engagement_mapping = {
    "Never": 1, "Rarely": 2, "Sometimes": 3, "Often": 4, "Always": 5
}
loyalty_mapping = {
    "Strongly disagree": 1, "Disagree": 2, "Neutral": 3, "Agree": 4, "Strongly agree": 5
}
preference_mapping = {
    "Extremely not well": 1, "Somewhat not well": 2, "Neutral": 3, "Somewhat well": 4, "Extremely well": 5
}

# Applying mappings to create new numeric columns
df['Satisfaction_Level'] = df["How satisfied are you with the personalised recommendations provided by Jumia?"].map(satisfaction_mapping)
df['Trust_Level'] = df["Would clearer information on how your data is used improve your trust in Jumia's AI system?"].map(trust_mapping)
df['Engagement_Level'] = df["How often do you interact with Jumia’s AI-personalised product recommendations (e.g., clicking on recommended items, adding items to cart)?"].map(engagement_mapping)
df['Loyalty_Level'] = df["Jumia’s AI-personalised recommendations have made you more loyal to the platform"].map(loyalty_mapping)
df['Preference_Level'] = df["How well do you think Jumia's personalised recommendations reflect your personal preferences and lifestyle?"].map(preference_mapping)

# Preview the new columns
df[['Satisfaction_Level', 'Trust_Level', 'Engagement_Level', 'Loyalty_Level', 'Preference_Level']].head()


# In[34]:


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="What is your age group?", hue="What is your monthly income range?", palette="viridis")
plt.title("Age Group vs. Monthly Income Range")
plt.xlabel("Count")
plt.ylabel("Age Group")
plt.legend(title="Income Range", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# The chart shows that younger age groups (18-24 and 25-34) are predominantly within lower income brackets, with a majority earning below ₦200,000 monthly. This distribution suggests that AI recommendations in Jumia may need to consider income level as a factor when targeting products, as a large portion of users may have budget constraints that affect purchasing decisions.

# In[35]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Engagement_Level', y='Satisfaction_Level', palette="coolwarm")
plt.title("Satisfaction Level vs. Engagement Frequency")
plt.xlabel("Engagement Level")
plt.ylabel("Satisfaction Level")
plt.show()


# The box plot indicates that as engagement frequency increases, satisfaction levels tend to stabilise around the higher values. This could imply that regular interaction with personalised recommendations correlates with a more positive user experience, potentially driving increased satisfaction.

# In[36]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Trust_Level', y='Loyalty_Level', palette="Blues")
plt.title("Trust Level vs. Customer Loyalty")
plt.xlabel("Trust Level")
plt.ylabel("Customer Loyalty Level")
plt.show()


# The relationship between trust and customer loyalty shows that higher trust levels generally align with higher loyalty levels. Users who trust Jumia’s AI system are more likely to exhibit brand loyalty. This highlights the importance of transparency in data usage to foster customer trust and loyalty.

# In[37]:


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Satisfaction_Level', y='Loyalty_Level', hue='Trust_Level', palette="viridis", s=100, alpha=0.7)
plt.title("Satisfaction Level vs. Loyalty Level (Colored by Trust Level)")
plt.xlabel("Satisfaction Level")
plt.ylabel("Loyalty Level")
plt.legend(title="Trust Level", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# The scatter plot reveals that high satisfaction and loyalty levels often coincide with higher trust levels. Users who are both satisfied with AI recommendations and have high trust are more inclined to stay loyal to Jumia. This underscores the impact of a positive, trustworthy AI experience on fostering brand loyalty.

# In[38]:


# Cultural Relevance by Age Group
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='What is your age group?', hue="To what extent do you feel that Jumia's personalised recommendations reflect the cultural realities of living in Lagos?", palette='viridis')
plt.title("Cultural Relevance of AI Recommendations by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend(title="Cultural Relevance Level", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# Most respondents across age groups feel that Jumia’s recommendations are culturally relevant, though younger age groups (25-34) seem to align more with “Very well” and “Moderately well.” This suggests that cultural factors are vital for younger users, possibly due to a higher sensitivity to personal relevance in product recommendations.

# In[39]:


# Economic Relevance by Income Range
plt.figure(figsize=(12, 6))
sns.countplot(data=df, y='What is your monthly income range?', hue="To what extent do you feel that Jumia's personalised recommendations reflect the economic realities of living in Lagos?", palette='plasma')
plt.title("Economic Relevance of AI Recommendations by Income Range")
plt.xlabel("Count")
plt.ylabel("Income Range")
plt.legend(title="Economic Relevance Level", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# Income range plays a significant role in perceived economic relevance. Those in the ₦50,000-₦100,000 bracket largely find the recommendations moderately relevant. This suggests that adjusting recommendations based on income levels can enhance perceived relevance for cost-sensitive users, aligning product options with affordability.

# In[40]:


# Analyzing engagement frequency by age group
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='What is your age group?', hue='How frequently do you shop on Jumia?', palette='coolwarm')
plt.title('Engagement Frequency by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Shopping Frequency')
plt.show()


# The most frequent engagement occurs in the 25-34 age group, predominantly when users need it, indicating a selective interaction pattern. This insight suggests that Jumia may enhance engagement by prompting recommendations based on user needs or shopping frequency.

# In[41]:


# Analyzing satisfaction level by income range
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='What is your monthly income range?', hue='How satisfied are you with the personalised recommendations provided by Jumia?', palette='magma')
plt.title('Satisfaction Level by Income Range')
plt.xlabel('Count')
plt.ylabel('Monthly Income Range')
plt.legend(title='Satisfaction Level')
plt.show()


# Income range appears to influence satisfaction, with higher satisfaction levels more prevalent among lower income brackets. This could suggest that these users find the recommendations useful and appropriate for their budget. Tailoring recommendations to align with specific income levels may continue to improve satisfaction across different demographics.

# # 3.3. Multivariate Analysis

# 
# In the multivariate analysis phase, I examine the relationships between multiple variables to uncover deeper insights into how they interact and influence each other. By analysing variables like satisfaction level, trust, engagement frequency, loyalty, and income, I identify patterns and correlations that may not be visible in univariate or bivariate analysis. For instance, I explore how trust in AI recommendations, combined with engagement frequency and income level, impacts customer loyalty on Jumia. This analysis helps in understanding complex dependencies between factors, allowing a more holistic view of customer behavior, which can guide Jumia in optimising personalised recommendations to improve user satisfaction.

# In[42]:


import matplotlib.pyplot as plt
import seaborn as sns

# Selecting the new numeric columns for correlation analysis
correlation_matrix = df[['Satisfaction_Level', 'Trust_Level', 'Engagement_Level', 'Loyalty_Level', 'Preference_Level']].corr()

# Plotting the correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True, square=True)
plt.title("Correlation Matrix of Satisfaction, Trust, Engagement, Loyalty, and Preference Levels")
plt.show()


# This correlation matrix shows the relationship between satisfaction, trust, engagement, loyalty, and preference levels. The values in the matrix range from -1 to 1, where positive values indicate a positive relationship between two variables, while negative values signify an inverse relationship. Here, we observe a moderate positive correlation between satisfaction and loyalty (0.41) and between loyalty and preference (0.54). This suggests that as customer satisfaction with AI recommendations increases, their loyalty to the platform tends to grow. Additionally, higher preference alignment with recommendations correlates with increased loyalty, highlighting the importance of accurate personalisation for retaining users. Other relationships, like satisfaction and engagement, show weaker correlations, indicating that while satisfaction may affect loyalty, it does not strongly influence engagement levels directly. These insights can inform strategies to improve specific aspects of AI personalisation that impact overall customer loyalty and trust.

# In[43]:


# Encoding ordinal variables for correlation analysis
ordinal_mapping = {
    "Very dissatisfied": 1, "Dissatisfied": 2, "Neutral": 3, "Satisfied": 4, "Very satisfied": 5,
    "Not at all": 1, "No, not really": 2, "Neutral": 3, "Yes, somewhat": 4, "Yes, significantly": 5,
    "Never": 1, "Rarely": 2, "Sometimes": 3, "Often": 4, "Always": 5
}

# Map satisfaction, trust, and engagement columns to numeric values
df['Satisfaction Level'] = df["How satisfied are you with the personalised recommendations provided by Jumia?"].map(ordinal_mapping)
df['Trust Level'] = df["Would clearer information on how your data is used improve your trust in Jumia's AI system?"].map(ordinal_mapping)
df['Engagement Level'] = df["How often do you interact with Jumia’s AI-personalised product recommendations (e.g., clicking on recommended items, adding items to cart)?"].map(ordinal_mapping)

# Calculate the correlation matrix for these encoded columns
correlation_matrix = df[['Satisfaction Level', 'Trust Level', 'Engagement Level']].corr()

# Plotting the correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True)
plt.title("Correlation Matrix of Satisfaction, Trust, and Engagement Levels")
plt.show()


# In this simplified correlation matrix focusing on satisfaction, trust, and engagement, we observe similar positive correlations. The relationship between satisfaction and trust is moderate (0.25), indicating that customers who are more satisfied with AI recommendations are likely to trust the platform more. However, there is a near-zero correlation between trust and engagement (-0.0005), suggesting that trust alone does not significantly affect how frequently customers engage with personalised recommendations. The engagement and satisfaction correlation (0.19) remains low, implying that engagement is influenced by factors other than just satisfaction. This matrix supports the notion that while satisfaction and trust are linked, increasing customer trust may not necessarily boost interaction with AI recommendations. Instead, targeted efforts to enhance engagement should consider other factors, such as recommendation relevance and usability, to foster active customer participation on the platform.

# In[44]:


# Trust by Satisfaction Level with AI Recommendations
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Would clearer information on how your data is used improve your trust in Jumia's AI system?", y='Satisfaction Level', palette='magma')
plt.title("Effect of Transparency on Trust and Satisfaction with AI Recommendations")
plt.xlabel("Trust Improvement with Data Transparency")
plt.ylabel("Satisfaction Level")
plt.xticks(rotation=45)
plt.show()


# This box plot shows the relationship between trust improvement due to data transparency and satisfaction with AI recommendations. Users who report significant trust improvements with clearer data transparency also display higher levels of satisfaction, as shown by the box extending towards the upper quartile. Those who feel "Yes, somewhat" and "No, not really" show slightly lower satisfaction distributions. This suggests that transparency about data use can positively impact satisfaction, reinforcing the importance of building transparent communication regarding AI personalization practices. Platforms like Jumia can leverage this insight to enhance user trust by clearly explaining how customer data is utilised to generate recommendations. This approach not only fosters trust but also aligns with users’ privacy expectations, potentially leading to improved satisfaction with the AI-driven experience.

# In[45]:


# Visualizing Satisfaction Levels by Income Range
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='What is your monthly income range?', y='Satisfaction Level', palette='coolwarm')
plt.title('Impact of Income on Satisfaction with AI Recommendations')
plt.xlabel('Monthly Income Range')
plt.ylabel('Satisfaction Level')
plt.xticks(rotation=45)
plt.show()


# This box plot compares satisfaction levels with AI recommendations across different income groups. The distribution shows that satisfaction levels are fairly consistent across most income brackets, but there are subtle variations. Higher income groups, such as those earning above ₦500,000, have a wider range of satisfaction levels, indicating varying perceptions of AI recommendations' relevance within this group. Lower income groups (₦50,000-₦100,000) display more stable satisfaction, suggesting that the expectations for AI-driven personalization might differ across income levels. By understanding these nuances, platforms can tailor their recommendation algorithms to cater to specific income groups, potentially leading to more targeted and relevant product suggestions. This insight can help Jumia enhance its recommendation accuracy for different customer segments, ultimately contributing to higher satisfaction across diverse income demographics.

# In[46]:


# Privacy Concerns by Engagement Level
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Are you concerned about the privacy of your personal data used for Jumia's personalised recommendations?", y='Engagement Level', palette='cool')
plt.title("Privacy Concerns by Engagement Level")
plt.xlabel("Privacy Concern Level")
plt.ylabel("Engagement Level")
plt.xticks(rotation=45)
plt.show()


# This box plot examines the relationship between privacy concerns and engagement level with AI recommendations. Users who are "Very concerned" about privacy show higher engagement levels, while those with "Neutral" or "Not concerned" attitudes have lower engagement levels. This counterintuitive trend might indicate that users who are more aware of their privacy may also be more vigilant and interactive with the platform, possibly due to a desire to monitor how their data is being used. On the other hand, users with lower privacy concerns engage less frequently, perhaps indicating a more passive relationship with AI recommendations. These findings suggest that addressing privacy concerns proactively could foster higher engagement, as users feel more secure in interacting with personalised recommendations. By assuring users of their data's security, Jumia could encourage a more active user base, particularly among privacy-conscious customers.

# In[47]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set up 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Privacy Concerns by Engagement Level
sns.boxplot(data=df, x="Are you concerned about the privacy of your personal data used for Jumia's personalised recommendations?", y='Engagement_Level', palette='cool', ax=axes[0, 0])
axes[0, 0].set_title("Privacy Concerns by Engagement Level")
axes[0, 0].set_xlabel("Privacy Concern Level")
axes[0, 0].set_ylabel("Engagement Level")

# Trust by Satisfaction Level with AI Recommendations
sns.boxplot(data=df, x="Would clearer information on how your data is used improve your trust in Jumia's AI system?", y='Satisfaction_Level', palette='magma', ax=axes[0, 1])
axes[0, 1].set_title("Effect of Transparency on Trust and Satisfaction")
axes[0, 1].set_xlabel("Trust Improvement with Data Transparency")
axes[0, 1].set_ylabel("Satisfaction Level")

# Satisfaction Level by Income Range
sns.boxplot(data=df, x='What is your monthly income range?', y='Satisfaction_Level', palette='coolwarm', ax=axes[1, 0])
axes[1, 0].set_title('Satisfaction Level by Income Range')
axes[1, 0].set_xlabel('Monthly Income Range')
axes[1, 0].set_ylabel('Satisfaction Level')
axes[1, 0].tick_params(axis='x', rotation=45)

# Trust by Satisfaction Level with AI Recommendations
sns.boxplot(data=df, x="Would clearer information on how your data is used improve your trust in Jumia's AI system?", y="Satisfaction_Level", palette="viridis", ax=axes[1, 1])
axes[1, 1].set_title("Trust by Satisfaction Level with AI Recommendations")
axes[1, 1].set_xlabel("Trust Improvement with Data Transparency")
axes[1, 1].set_ylabel("Satisfaction Level")

plt.tight_layout()
plt.show()


# In[48]:


import matplotlib.pyplot as plt
import seaborn as sns

# Setting up a 3x2 grid layout
fig, axes = plt.subplots(3, 2, figsize=(18, 20))

# Plot 1: Impact of Income on Satisfaction with AI Recommendations
sns.boxplot(data=df, x='What is your monthly income range?', y='Satisfaction Level', palette='coolwarm', ax=axes[0, 0])
axes[0, 0].set_title('Impact of Income on Satisfaction with AI Recommendations')
axes[0, 0].set_xlabel('Monthly Income Range')
axes[0, 0].set_ylabel('Satisfaction Level')
axes[0, 0].tick_params(axis='x', rotation=45)

# Plot 2: Effect of Transparency on Trust and Satisfaction with AI Recommendations
sns.boxplot(data=df, x="Would clearer information on how your data is used improve your trust in Jumia's AI system?", y='Satisfaction Level', palette='magma', ax=axes[0, 1])
axes[0, 1].set_title("Effect of Transparency on Trust and Satisfaction with AI Recommendations")
axes[0, 1].set_xlabel("Trust Improvement with Data Transparency")
axes[0, 1].set_ylabel("Satisfaction Level")
axes[0, 1].tick_params(axis='x', rotation=45)

# Plot 3: Satisfaction Level by Income Range (Count Plot)
sns.countplot(data=df, y='What is your monthly income range?', hue='How satisfied are you with the personalised recommendations provided by Jumia?', palette='magma', ax=axes[1, 0])
axes[1, 0].set_title('Satisfaction Level by Income Range')
axes[1, 0].set_xlabel('Count')
axes[1, 0].set_ylabel('Monthly Income Range')
axes[1, 0].legend(title='Satisfaction Level', bbox_to_anchor=(1.05, 1), loc='upper left')

# Plot 4: Engagement Frequency by Age Group
sns.countplot(data=df, x='What is your age group?', hue='How frequently do you shop on Jumia?', palette='coolwarm', ax=axes[1, 1])
axes[1, 1].set_title('Engagement Frequency by Age Group')
axes[1, 1].set_xlabel('Age Group')
axes[1, 1].set_ylabel('Count')
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].legend(title='Shopping Frequency', bbox_to_anchor=(1.05, 1), loc='upper left')

# Plot 5: Cultural Relevance of AI Recommendations by Age Group
sns.countplot(data=df, x='What is your age group?', hue="To what extent do you feel that Jumia's personalised recommendations reflect the cultural realities of living in Lagos?", palette='viridis', ax=axes[2, 0])
axes[2, 0].set_title("Cultural Relevance of AI Recommendations by Age Group")
axes[2, 0].set_xlabel("Age Group")
axes[2, 0].set_ylabel("Count")
axes[2, 0].tick_params(axis='x', rotation=45)
axes[2, 0].legend(title="Cultural Relevance Level", bbox_to_anchor=(1.05, 1), loc='upper left')

# Plot 6: Satisfaction Level vs. Loyalty Level (Colored by Trust Level)
sns.scatterplot(data=df, x='Satisfaction_Level', y='Loyalty_Level', hue='Trust_Level', palette="viridis", s=100, alpha=0.7, ax=axes[2, 1])
axes[2, 1].set_title("Satisfaction Level vs. Loyalty Level (Colored by Trust Level)")
axes[2, 1].set_xlabel("Satisfaction Level")
axes[2, 1].set_ylabel("Loyalty Level")
axes[2, 1].legend(title="Trust Level", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to avoid overlap
plt.tight_layout()
plt.show()


# # SECTION 4: TACKLING RANKING QUESTION IN THE DATA

# In the section, I tackled two ranking questions, which are crucial in assessing perceptions of AI-personalised recommendations on Jumia. The first question asked respondents to rank how relevant they found these recommendations, with options ranging from "Extremely relevant" to "Not relevant at all." The second question focused on the extent to which respondents felt AI recommendations improved their shopping experience, with choices from "Significantly improve" to "Significantly worsen."
# 
# To analyse these rankings effectively, I mapped the responses to numeric values, where 1 represented the highest relevance or improvement level and 5 the lowest. This conversion was essential for calculating an average weighted score, a method that ensures consistency and helps avoid irregularities in interpretation. By assigning weights to each response choice, I derived an average that reflects the overall sentiment, maintaining data quality and allowing a nuanced understanding of customer attitudes. This approach is essential to avoid inconsistencies in analysis and preserve the integrity of the responses.

# In[49]:


# Check unique values for the relevance and improvement columns to detect inconsistencies
print("Unique values in 'How relevant do you find the personalised recommendations on Jumia?':")
print(df['How relevant do you find the personalised recommendations on Jumia?\n\n(Please rank the options below from 1 to 5, where 1 is the highest and 5 is the lowest.)\n'].unique())

print("\nUnique values in 'To what extent do you believe the AI-personalised recommendations improve your overall shopping experience on Jumia?':")
print(df['To what extent do you believe the AI-personalised recommendations improve your overall shopping experience on Jumia?\n(Please rank the options below from 1 to 5, where 1 is the highest and 5 is the low'].unique())


# In[50]:


df8 = df.copy()
import re

# Standard ranking labels in correct order
relevance_labels = ['Extremely relevant', 'Very relevant', 'Moderately relevant', 'Slightly relevant', 'Not relevant at all']
improvement_labels = ['Significantly improve', 'Somewhat improve', 'No effect', 'Somewhat worsen', 'Significantly worsen']

# Function to standardize and encode rankings based on the provided labels
def standardize_and_encode_rankings(response, labels):
    # Split and clean the response
    split_response = [item.strip() for item in response.split(';')]
    
    # Create a dictionary for the given response
    response_dict = {item: rank + 1 for rank, item in enumerate(split_response)}
    
    # Use the standard labels to retrieve ranks or fill with None if missing
    standardized_ranks = [response_dict.get(label, None) for label in labels]
    return standardized_ranks

# Applying the function to encode both columns in correct label order
df8['Relevance_Rank'] = df8['How relevant do you find the personalised recommendations on Jumia?\n\n(Please rank the options below from 1 to 5, where 1 is the highest and 5 is the lowest.)\n'].dropna().apply(lambda x: standardize_and_encode_rankings(x, relevance_labels))
df8['Improvement_Rank'] = df8['To what extent do you believe the AI-personalised recommendations improve your overall shopping experience on Jumia?\n(Please rank the options below from 1 to 5, where 1 is the highest and 5 is the low'].dropna().apply(lambda x: standardize_and_encode_rankings(x, improvement_labels))

# Preview the first few rows to confirm the rankings are consistent and ordered
df8[['Relevance_Rank', 'Improvement_Rank']].head(10)


# In[51]:


# Updated function to fill missing ranks, checking if input is a list first
def fill_missing_rank(ranks):
    # Only proceed if 'ranks' is a list (i.e., not NaN)
    if isinstance(ranks, list):
        # Check if there's a missing value (None) in the list
        if None in ranks:
            # Find the missing rank by identifying numbers not in ranks
            filled_ranks = [rank if rank is not None else (set([1, 2, 3, 4, 5]) - set(ranks)).pop() for rank in ranks]
            return filled_ranks
        else:
            return ranks  # Return as-is if no None is present
    return ranks  # Return as-is if input is not a list

# Apply the function to fill missing ranks on both Relevance_Rank and Improvement_Rank columns
df8['Relevance_Rank'] = df8['Relevance_Rank'].apply(fill_missing_rank)
df8['Improvement_Rank'] = df8['Improvement_Rank'].apply(fill_missing_rank)

# Confirm the result
df8[['Relevance_Rank', 'Improvement_Rank']].head(10)


# In[52]:


df1 = df8.copy()
#Now let further determine the average weight score for each rows in the two columns
# Define weights such that 1 (highest) gets the maximum weight (5) and 5 (lowest) gets the minimum weight (1)
weights = [5, 4, 3, 2, 1]

# Redefine the weighted score function to ensure proper calculation based on ranks
def weighted_score(ranks):
    if isinstance(ranks, list) and len(ranks) == len(weights):
        # Calculate the score with 1 as the highest rank getting the highest weight
        return sum(rank * weight for rank, weight in zip(ranks, weights)) / sum(weights)
    else:
        # Handle cases where ranks are not lists or are NaN
        return None  # Or use a default score like 0, depending on the analysis needs

# Apply weighted scoring to each ranking column with the updated weights
df['Relevance_Score'] = df1['Relevance_Rank'].apply(weighted_score)
df['Improvement_Score'] = df1['Improvement_Rank'].apply(weighted_score)

# Display the updated DataFrame to confirm correct scores
df[['Relevance_Score', 'Improvement_Score']].head()


# Now that I have finnally mapped the ranking questions data, let explore some visualisation

# In[53]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Filter out rows where Relevance_Rank or Improvement_Rank contain NaN values
relevance_ranks_df = pd.DataFrame(df1['Relevance_Rank'].dropna().tolist(), columns=['Extremely relevant', 'Very relevant', 'Moderately relevant', 'Slightly relevant', 'Not relevant at all'])
improvement_ranks_df = pd.DataFrame(df1['Improvement_Rank'].dropna().tolist(), columns=['Significantly improve', 'Somewhat improve', 'No effect', 'Somewhat worsen', 'Significantly worsen'])

# Plot distribution for each rank in the Relevance_Rank category
plt.figure(figsize=(15, 10))
for i, label in enumerate(relevance_ranks_df.columns):
    plt.subplot(3, 2, i+1)
    sns.histplot(relevance_ranks_df[label], bins=range(1, 7), kde=False)
    plt.title(f'Relevance: {label}')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# 
# The charts above illustrate the distribution of rankings for the perceived relevance of Jumia's personalised recommendations across five categories: "Extremely relevant," "Very relevant," "Moderately relevant," "Slightly relevant," and "Not relevant at all." Each graph shows how frequently each rank (from 1 to 5) was assigned within these categories, where rank 1 is the highest and rank 5 the lowest.
# 
# For "Extremely relevant" and "Very relevant" categories, a noticeable concentration appears at the top ranks, indicating that a significant portion of respondents rated these recommendations highly. However, for the "Moderately relevant" and "Slightly relevant" categories, the rankings are more spread out, reflecting a varied perception of relevance among respondents. Interestingly, the "Not relevant at all" category has a heavy concentration at rank 5, showing a strong consensus among respondents who viewed these recommendations as irrelevant. This analysis provides insights into user sentiment toward Jumia's personalised recommendations and the perceived effectiveness of AI-driven suggestions.

# In[54]:


# Plot distribution for each rank in the Improvement_Rank category
plt.figure(figsize=(15, 10))
for i, label in enumerate(improvement_ranks_df.columns):
    plt.subplot(3, 2, i+1)
    sns.histplot(improvement_ranks_df[label], bins=range(1, 7), kde=False)
    plt.title(f'Improvement: {label}')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# The charts above show the frequency distribution of rankings for the perceived impact of Jumia's AI-personalised recommendations on users' shopping experiences. Each chart represents a specific level of improvement or detriment, ranked from 1 (most significant impact) to 5 (least impact).
# 
# In the "Significantly improve" category, the majority of respondents placed it at rank 1, suggesting a strong positive impact on their shopping experience. Similarly, the "Somewhat improve" category sees a high frequency at ranks 2 and 3, indicating moderate enhancement perceived by users. For the "No effect" category, ranks are distributed primarily in the middle, showing that many users feel neutral towards the AI recommendations' influence.
# 
# Conversely, the "Somewhat worsen" and "Significantly worsen" categories have higher rankings, indicating that for those who perceive a negative impact, the effect is generally minimal. This analysis reflects a diverse range of opinions on how Jumia's AI recommendations affect shopping satisfaction, from substantial improvement to slight detriment.

# In[55]:


import matplotlib.pyplot as plt
import pandas as pd

# Define labels for each category
relevance_labels = ['Extremely relevant', 'Very relevant', 'Moderately relevant', 'Slightly relevant', 'Not relevant at all']
improvement_labels = ['Significantly improve', 'Somewhat improve', 'No effect', 'Somewhat worsen', 'Significantly worsen']

# Drop NaN rows in Relevance_Rank and Improvement_Rank and create DataFrames
relevance_ranks_df = pd.DataFrame(df1['Relevance_Rank'].dropna().tolist(), columns=relevance_labels)
improvement_ranks_df = pd.DataFrame(df1['Improvement_Rank'].dropna().tolist(), columns=improvement_labels)

# Reverse the scale: 1 becomes 5, 2 becomes 4, ..., 5 becomes 1
relevance_ranks_df = 6 - relevance_ranks_df  # 6 - rank will reverse the scale
improvement_ranks_df = 6 - improvement_ranks_df  # 6 - rank will reverse the scale

# Calculate weighted average for each label in Relevance_Rank with reversed scale
relevance_avg_weights = relevance_ranks_df.mean()

# Calculate weighted average for each label in Improvement_Rank with reversed scale
improvement_avg_weights = improvement_ranks_df.mean()

# Plotting Weighted Average Rankings for Relevance
plt.figure(figsize=(10, 6))
relevance_avg_weights.sort_values().plot(kind='barh', color='skyblue')
plt.title("Average Weighted Scale for Relevance of Personalised Recommendations")
plt.xlabel("Average Rank (5 = Most Relevant, 1 = Least Relevant)")
plt.ylabel("Relevance Aspects")
plt.show()


# The chart illustrates the average weighted score for different levels of relevance in Jumia's personalised recommendations, rated by users. This scoring method considers rankings from 1 to 5, with 1 indicating the highest relevance and 5 indicating the lowest.
# 
# "Extremely relevant" holds the highest average score, reflecting that users perceive a substantial alignment of recommendations with their preferences. Following closely, "Very relevant" also receives a strong average score, indicating a significant level of perceived relevance. The scores gradually decrease through "Moderately relevant" and "Slightly relevant," showing a moderate to minimal level of resonance for these categories. Finally, "Not relevant at all" scores the lowest, aligning with users who do not find value in the personalised recommendations.
# 
# This analysis highlights that while a majority find Jumia's recommendations relevant, there are varying degrees, with some users perceiving little to no relevance. The weighted scoring approach offers nuanced insights into these preferences.

# In[56]:


# Plotting Weighted Average Rankings for Improvement
plt.figure(figsize=(10, 6))
improvement_avg_weights.sort_values().plot(kind='barh', color='salmon')
plt.title("Average Weighted Scale for Improvement in Shopping Experience")
plt.xlabel("Average Rank (5 = Most Improvement, 1 = Least Improvement)")
plt.ylabel("Improvement Aspects")
plt.show()


# This chart shows the average weighted scores for user perceptions on how AI-personalised recommendations on Jumia impact their shopping experience. The scores range from "Significantly improve" to "Significantly worsen," with ranks assigned from 1 (highest improvement) to 5 (least improvement).
# 
# "Significantly improve" holds the highest average weighted score, indicating that a notable portion of users find Jumia’s personalised recommendations enhance their shopping experience considerably. "Somewhat improve" also has a strong average, suggesting many users perceive moderate benefits from these recommendations. "No effect" and "Somewhat worsen" have lower scores, indicating limited or negative perceptions of the AI’s influence. "Significantly worsen" ranks lowest, representing a small group that feels the recommendations harm their experience.
# 
# This analysis using weighted averages reveals that while many users appreciate the improvement AI recommendations bring, some remain neutral or even view the impact as negative, underscoring varied user experiences with AI personalisation.

# In[57]:


import matplotlib.pyplot as plt

# Setting up a 1x2 grid layout
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Plot 1: Average Weighted Scale for Relevance of Personalised Recommendations
relevance_avg_weights.sort_values().plot(kind='barh', color='skyblue', ax=axes[0])
axes[0].set_title("Average Weighted Scale for Relevance of Personalised Recommendations")
axes[0].set_xlabel("Average Rank (5 = Most Relevant, 1 = Least Relevant)")
axes[0].set_ylabel("Relevance Aspects")

# Plot 2: Average Weighted Scale for Improvement in Shopping Experience
improvement_avg_weights.sort_values().plot(kind='barh', color='salmon', ax=axes[1])
axes[1].set_title("Average Weighted Scale for Improvement in Shopping Experience")
axes[1].set_xlabel("Average Rank (5 = Most Improvement, 1 = Least Improvement)")
axes[1].set_ylabel("Improvement Aspects")

# Adjust layout to ensure clear visibility
plt.tight_layout()
plt.show()


# In[58]:


#let analyse it further with income and age group to get more deeper insights
# Adding Income Level and Age Group to the ranking DataFrames for grouping
relevance_ranks_df['Income Level'] = df1['What is your monthly income range?']
relevance_ranks_df['Age Group'] = df1['What is your age group?']

improvement_ranks_df['Income Level'] = df1['What is your monthly income range?']
improvement_ranks_df['Age Group'] = df1['What is your age group?']

# Calculate average relevance rank by income level
avg_relevance_income = relevance_ranks_df.groupby('Income Level').mean()

# Calculate average improvement rank by age group
avg_improvement_age = improvement_ranks_df.groupby('Age Group').mean()

# Plotting Relevance by Income Level
avg_relevance_income.plot(kind='bar', figsize=(12, 8), colormap='Blues')
plt.title("Average Relevance Ranking by Income Level")
plt.xlabel("Income Level")
plt.ylabel("Average Rank (5 = Most Relevant, 1 = Least Relevant)")
plt.xticks(rotation=45)
plt.show()

# Plotting Improvement by Age Group
avg_improvement_age.plot(kind='bar', figsize=(12, 8), colormap='Greens')
plt.title("Average Improvement Ranking by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Rank (5 = Most Improvement, 1 = Least Improvement)")
plt.xticks(rotation=45)
plt.show()


# In the analysis, I created two bar plots to illustrate the average weighted relevance and improvement rankings. The first plot, "Average Relevance Ranking by Income Level," shows how individuals from different income brackets perceive the relevance of Jumia's personalised recommendations. By calculating average ranks, it becomes clear how each income group rates aspects of recommendation relevance, with lower average ranks indicating higher relevance. Similarly, the second plot, "Average Improvement Ranking by Age Group," highlights how various age groups perceive the extent to which AI-personalised recommendations enhance their shopping experience. Lower ranks in this plot signify higher perceived improvement. These visualisations allow a clearer understanding of how income level and age influence perceptions of AI recommendations on relevance and improvement.

# In[59]:


import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(4, 3, figsize=(24, 28))
fig.suptitle("Hypothesis Support Visualizations", fontsize=18)

# Plot 1: Correlation Matrix
correlation_matrix = df[['Satisfaction_Level', 'Trust_Level', 'Engagement_Level', 'Loyalty_Level', 'Preference_Level']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=axes[0, 0])
axes[0, 0].set_title("Correlation Matrix of Core Variables")

# Plot 2: Age Group vs. Monthly Income Range
sns.countplot(data=df, y="What is your age group?", hue="What is your monthly income range?", palette="viridis", ax=axes[0, 1])
axes[0, 1].set_title("Age Group vs. Monthly Income Range")
axes[0, 1].set_ylabel("Age Group")
axes[0, 1].set_xlabel("Count")
axes[0, 1].legend(title="Income Range")

# Plot 3: Satisfaction Level vs. Engagement Frequency
sns.boxplot(data=df, x='Engagement_Level', y='Satisfaction_Level', palette="coolwarm", ax=axes[0, 2])
axes[0, 2].set_title("Satisfaction Level vs. Engagement Frequency")
axes[0, 2].set_xlabel("Engagement Level")
axes[0, 2].set_ylabel("Satisfaction Level")

# Plot 4: Trust Level vs. Customer Loyalty
sns.boxplot(data=df, x='Trust_Level', y='Loyalty_Level', palette="Blues", ax=axes[1, 0])
axes[1, 0].set_title("Trust Level vs. Customer Loyalty")
axes[1, 0].set_xlabel("Trust Level")
axes[1, 0].set_ylabel("Customer Loyalty Level")

# Plot 5: Satisfaction Level vs. Loyalty Level (Colored by Trust Level)
sns.scatterplot(data=df, x='Satisfaction_Level', y='Loyalty_Level', hue='Trust_Level', palette="viridis", s=100, ax=axes[1, 1])
axes[1, 1].set_title("Satisfaction vs. Loyalty (Colored by Trust)")
axes[1, 1].set_xlabel("Satisfaction Level")
axes[1, 1].set_ylabel("Loyalty Level")
axes[1, 1].legend(title="Trust Level")

# Plot 6: Engagement Frequency by Age Group
sns.countplot(data=df, x='What is your age group?', hue='How frequently do you shop on Jumia?', palette='coolwarm', ax=axes[1, 2])
axes[1, 2].set_title("Engagement Frequency by Age Group")
axes[1, 2].set_xlabel("Age Group")
axes[1, 2].set_ylabel("Count")
axes[1, 2].legend(title="Shopping Frequency")

# Plot 7: Satisfaction Level by Income Range
sns.countplot(data=df, y='What is your monthly income range?', hue='How satisfied are you with the personalised recommendations provided by Jumia?', palette='magma', ax=axes[2, 0])
axes[2, 0].set_title("Satisfaction Level by Income Range")
axes[2, 0].set_xlabel("Count")
axes[2, 0].set_ylabel("Monthly Income Range")
axes[2, 0].legend(title="Satisfaction Level")

# Plot 8: Effect of Transparency on Trust and Satisfaction
sns.boxplot(data=df, x="Would clearer information on how your data is used improve your trust in Jumia's AI system?", y='Satisfaction Level', palette='magma', ax=axes[2, 1])
axes[2, 1].set_title("Effect of Transparency on Trust and Satisfaction")
axes[2, 1].set_xlabel("Trust Improvement with Data Transparency")
axes[2, 1].set_ylabel("Satisfaction Level")

# Plot 9: Impact of Income on Satisfaction
sns.boxplot(data=df, x='What is your monthly income range?', y='Satisfaction Level', palette='coolwarm', ax=axes[2, 2])
axes[2, 2].set_title("Impact of Income on Satisfaction")
axes[2, 2].set_xlabel("Monthly Income Range")
axes[2, 2].set_ylabel("Satisfaction Level")

# Plot 10: Privacy Concerns by Engagement Level
sns.boxplot(data=df, x="Are you concerned about the privacy of your personal data used for Jumia's personalised recommendations?", y='Engagement Level', palette='cool', ax=axes[3, 0])
axes[3, 0].set_title("Privacy Concerns by Engagement Level")
axes[3, 0].set_xlabel("Privacy Concern Level")
axes[3, 0].set_ylabel("Engagement Level")

# Plot 11: Weighted Average for Relevance
relevance_avg_weights.sort_values().plot(kind='barh', color='skyblue', ax=axes[3, 1])
axes[3, 1].set_title("Average Weighted Scale for Relevance")
axes[3, 1].set_xlabel("Average Rank")
axes[3, 1].set_ylabel("Relevance Aspects")

# Plot 12: Weighted Average for Improvement
improvement_avg_weights.sort_values().plot(kind='barh', color='salmon', ax=axes[3, 2])
axes[3, 2].set_title("Average Weighted Scale for Improvement")
axes[3, 2].set_xlabel("Average Rank")
axes[3, 2].set_ylabel("Improvement Aspects")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


# # SECTION 5: TESTING HYPOTHESIS

# # 1. Consumer Engagement and Satisfaction with AI Recommendations:
# 
# - H1: AI-driven personalised recommendations positively impact customer engagement.
# - H2: AI-driven personalised recommendations positively influence customer satisfaction.
# 
# 
# Test: Correlation Analysis (Pearson or Spearman correlation) between AI personalisation metrics (e.g., satisfaction level, engagement frequency) and customer satisfaction/engagement levels.

# # H1: AI-driven personalised recommendations positively impact customer engagement.

# In[60]:


from scipy.stats import pearsonr, spearmanr

# Drop rows with NaN values in Engagement_Level or Satisfaction_Level
df_cleaned = df[['Engagement_Level', 'Satisfaction_Level']].dropna()

# Example of testing correlation between Engagement_Level and Satisfaction_Level
corr, p_value = pearsonr(df_cleaned['Engagement_Level'], df_cleaned['Satisfaction_Level'])
print(f"Pearson Correlation between Engagement and Satisfaction: {corr}, p-value: {p_value}")


# - Hypothesis Status: Accepted
# 
# The Pearson correlation analysis for the hypothesis that AI-driven personalised recommendations positively impact customer engagement indicates a positive correlation coefficient of 0.196 (p = 0.008). This statistically significant result (p < 0.05) suggests a modest but meaningful positive association between the engagement level and customer satisfaction in response to personalised AI recommendations.
# 
# While the correlation is relatively weak, the positive direction confirms that as customers engage more with personalised recommendations, their satisfaction levels tend to increase slightly. This implies that AI recommendations may contribute to enhancing customer engagement, but additional strategies may be needed to amplify this effect. The findings support the hypothesis that personalised recommendations encourage customer engagement, though the influence might not be strong enough to be the primary engagement driver. Therefore, this hypothesis is accepted, affirming the beneficial role of AI personalisation in encouraging engagement, albeit modestly.

# # H2: AI-driven personalised recommendations positively influence customer satisfaction.

# In[61]:


# Spearman correlation (in case data isn't normally distributed)
spearman_corr, spearman_p_value = spearmanr(df_cleaned['Engagement_Level'], df_cleaned['Satisfaction_Level'])
print(f"Spearman Correlation between Engagement and Satisfaction: {spearman_corr}, p-value: {spearman_p_value}")


# - Hypothesis Status: Accepted
# 
# The Spearman correlation analysis supports the hypothesis that AI-driven personalised recommendations positively influence customer satisfaction. With a positive correlation coefficient of 0.189 (p = 0.011), this result indicates a statistically significant, though modest, association between engagement with personalised recommendations and satisfaction. This suggests that customers who interact more frequently with AI-driven recommendations tend to report slightly higher satisfaction levels.
# 
# Despite the weak correlation strength, the significant p-value (below 0.05) confirms that there is a meaningful relationship between these variables. This finding implies that while AI recommendations contribute positively to satisfaction, they may not be the sole or most potent driver of satisfaction. Enhancing the relevance and quality of these recommendations could further strengthen their impact on customer satisfaction. Thus, the hypothesis is accepted, but with the understanding that additional factors may also play a role in influencing satisfaction.

# # 2.  Cultural and Economic Influence:
# 
# - H3: Cultural factors moderate the effectiveness of AI recommendations on customer engagement.
# 
# - H4: Economic factors (e.g., income disparity) moderate the relationship between AI recommendations and customer satisfaction.
# 
# Test: ANOVA to assess differences in engagement and satisfaction across cultural and income groups.

# In[62]:


# Print unique values in the Cultural Relevance column
print("Unique values in Cultural Relevance column:")
print(df["To what extent do you feel that Jumia's personalised recommendations reflect the cultural realities of living in Lagos?"].unique())

# Print unique values in the Economic Relevance column
print("\nUnique values in Economic Relevance column:")
print(df["To what extent do you feel that Jumia's personalised recommendations reflect the economic realities of living in Lagos?"].unique())


# In[63]:


# Define the mapping dictionary
relevance_mapping = {
    "Not well at all": 1,
    "Slightly well": 2,
    "Moderately well": 3,
    "Very well": 4,
    "Extremely well": 5
}

# Apply the mapping to create numeric columns
df['Cultural_Relevance'] = df["To what extent do you feel that Jumia's personalised recommendations reflect the cultural realities of living in Lagos?"].map(relevance_mapping)
df['Economic_Relevance'] = df["To what extent do you feel that Jumia's personalised recommendations reflect the economic realities of living in Lagos?"].map(relevance_mapping)

# Confirm the new columns by printing unique values
print("Mapped Cultural Relevance Levels:", df['Cultural_Relevance'].unique())
print("Mapped Economic Relevance Levels:", df['Economic_Relevance'].unique())


# In[64]:


# Count the NaN values in Cultural_Relevance and Economic_Relevance columns
cultural_nan_count = df['Cultural_Relevance'].isna().sum()
economic_nan_count = df['Economic_Relevance'].isna().sum()

print(f"Number of NaN values in Cultural_Relevance: {cultural_nan_count}")
print(f"Number of NaN values in Economic_Relevance: {economic_nan_count}")


# In[65]:


# Remove rows with NaN values in either Cultural_Relevance or Economic_Relevance columns
df_cleaned = df.dropna(subset=['Cultural_Relevance', 'Economic_Relevance'])

# Confirm that NaN values are removed by checking the unique values again
print("\nUnique values in cleaned Cultural_Relevance column:", df_cleaned['Cultural_Relevance'].unique())
print("Unique values in cleaned Economic_Relevance column:", df_cleaned['Economic_Relevance'].unique())


# # H3: Cultural factors moderate the effectiveness of AI recommendations on customer engagement

# In[66]:


from scipy.stats import f_oneway

# Perform ANOVA for Engagement Level across different levels of Cultural Relevance
cultural_groups = [df_cleaned['Engagement_Level'][df_cleaned['Cultural_Relevance'] == level].dropna() for level in range(1, 6)]
anova_engagement_culture = f_oneway(*cultural_groups)
print("ANOVA for Engagement Level across Cultural Relevance Levels:", anova_engagement_culture)


# - Hypothesis Status: Rejected
# 
# The ANOVA test conducted to evaluate whether cultural factors moderate the effectiveness of AI recommendations on customer engagement yielded an F-statistic of 2.384 with a p-value of 0.053. Since the p-value is just above the commonly accepted threshold of significance (p < 0.05), the results are not statistically significant. This implies that there is insufficient evidence to conclude that cultural factors meaningfully influence the relationship between AI recommendations and engagement levels.
# 
# While the test result indicates a trend towards significance, the lack of statistical support means we cannot confidently assert that cultural factors act as a moderator in this context. This suggests that AI recommendation effectiveness on engagement may be relatively consistent across cultural backgrounds in this dataset. Consequently, this hypothesis is rejected, as we cannot confirm a significant moderating role of cultural factors on engagement with AI-driven recommendations.

# In[67]:


import matplotlib.pyplot as plt
import seaborn as sns

# Box plot for Engagement Level across Cultural Relevance levels
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_cleaned, x='Cultural_Relevance', y='Engagement_Level', palette="viridis")
plt.title("Engagement Level across Cultural Relevance Levels")
plt.xlabel("Cultural Relevance Level")
plt.ylabel("Engagement Level")
plt.xticks(ticks=[0, 1, 2, 3, 4], labels=["Not well at all", "Slightly well", "Moderately well", "Very well", "Extremely well"])
plt.show()


# The box plot of Engagement Level across Cultural Relevance Levels visually supports the ANOVA findings. Each cultural relevance level, ranging from "Not well at all" to "Extremely well," shows a distribution of engagement levels. The plot suggests some variability in engagement across cultural relevance levels, with "Extremely well" showing the highest variability in engagement scores, indicating that participants who find AI recommendations extremely culturally relevant report a broader range of engagement levels.
# 
# However, the differences across these groups are not statistically significant at the 0.05 level, as indicated by the p-value of 0.053 from the ANOVA test. This aligns with our conclusion to reject the hypothesis that cultural factors significantly moderate AI recommendation effectiveness on engagement. Despite slight trends suggesting higher engagement for higher cultural relevance, these differences lack sufficient evidence to confirm a strong moderating effect of cultural factors. The visualisation reinforces the statistical outcome, indicating that while cultural relevance may influence engagement trends, it does not do so significantly.

# # H4: Economic factors (e.g., income disparity) moderate the relationship between AI recommendations and customer satisfaction.

# In[68]:


# Perform ANOVA for Satisfaction Level across different levels of Economic Relevance
economic_groups = [df_cleaned['Satisfaction_Level'][df_cleaned['Economic_Relevance'] == level].dropna() for level in range(1, 6)]
anova_satisfaction_economics = f_oneway(*economic_groups)
print("ANOVA for Satisfaction Level across Economic Relevance Levels:", anova_satisfaction_economics)


# - Hypothesis Outcome: Accepted
# 
# 
# The hypothesis that economic factors moderate the relationship between AI recommendations and customer satisfaction is supported by the data.
# 
# The ANOVA results for satisfaction levels across different economic relevance levels show a significant effect, with an F-statistic of 6.65 and a p-value of 5.28e-05. This indicates a statistically significant difference in customer satisfaction levels across groups with varying perceptions of economic relevance. This result suggests that economic relevance plays a moderating role in how satisfied customers feel with AI-driven recommendations.
# 
# Specifically, customers who perceive Jumia's AI recommendations as more economically relevant (aligning with their income or spending habits) tend to report higher satisfaction levels. Conversely, when economic relevance is perceived as low, satisfaction levels are likely to decrease, highlighting the importance of aligning AI recommendations with customers' financial realities. This finding underscores the need for AI personalisation that takes economic factors into account to enhance customer satisfaction and effectiveness in different economic segments.

# In[69]:


# Box plot for Satisfaction Level across Economic Relevance levels
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_cleaned, x='Economic_Relevance', y='Satisfaction_Level', palette="magma")
plt.title("Satisfaction Level across Economic Relevance Levels")
plt.xlabel("Economic Relevance Level")
plt.ylabel("Satisfaction Level")
plt.xticks(ticks=[0, 1, 2, 3, 4], labels=["Not well at all", "Slightly well", "Moderately well", "Very well", "Extremely well"])
plt.show()


# The boxplot visualises satisfaction levels across different economic relevance levels and provides strong visual support for the hypothesis that economic factors moderate the relationship between AI recommendations and customer satisfaction. The plot reveals a trend where satisfaction levels are higher for groups perceiving AI recommendations as economically relevant ("Very well" and "Extremely well"), while lower satisfaction levels are observed among those who find recommendations less relevant economically ("Not well at all" and "Slightly well").
# 
# The ANOVA results, paired with this boxplot, underscore the importance of economic alignment in AI-driven recommendations to improve customer satisfaction. The spread of satisfaction levels also highlights the potential for dissatisfaction if economic factors are not adequately considered, particularly for lower income or cost-sensitive customers. Thus, aligning AI recommendations with users' economic situations appears critical for boosting satisfaction and engagement, validating the hypothesis and illustrating the moderating role of economic factors.

# # 3. Trust and Privacy Concerns:
# 
# - H5: Consumer trust positively correlates with engagement with AI-driven recommendations.
# - H6: Privacy concerns negatively impact customer engagement and satisfaction with AI recommendations.
# 
# Test: Correlation Analysis for continuous variables or Independent Samples T-Test for comparing high vs. low trust/privacy groups with engagement and satisfaction.

# In[70]:


# View unique values in Trust_Level and Engagement_Level columns
print("Unique values in Trust_Level column:")
print(df['Trust_Level'].unique())

print("\nUnique values in Engagement_Level column:")
print(df['Engagement_Level'].unique())


# In[71]:


# View unique values in the original Trust column
print("Unique values in the original Trust column:")
print(df["Would clearer information on how your data is used improve your trust in Jumia's AI system?"].unique())


# In[72]:


# Define the updated mapping, excluding "No, not at all" since it has no entries
trust_mapping = {
    "Yes, significantly": 3,
    "Yes, somewhat": 2,
    "No, not really": 1
}

# Apply the mapping to create a numeric Trust_Level column
df1['Trust_Level'] = df1["Would clearer information on how your data is used improve your trust in Jumia's AI system?"].map(trust_mapping)

# Confirm the mapping by viewing unique values in the Trust_Level column
print("Mapped Trust_Level unique values:", df['Trust_Level'].unique())


# In[73]:


# Remove rows with NaN values in Trust_Level or Engagement_Level
df_cleaned = df.dropna(subset=['Trust_Level', 'Engagement_Level'])

# Verify the cleaning process
print("Unique values in cleaned Trust_Level column:", df_cleaned['Trust_Level'].unique())
print("Unique values in cleaned Engagement_Level column:", df_cleaned['Engagement_Level'].unique())


# # H5: Consumer trust positively correlates with engagement with AI-driven recommendations.

# In[74]:


from scipy.stats import ttest_ind

# Split data into high and low trust groups based on median Trust_Level
median_trust = df_cleaned['Trust_Level'].median()
high_trust = df_cleaned[df_cleaned['Trust_Level'] >= median_trust]['Engagement_Level']
low_trust = df_cleaned[df_cleaned['Trust_Level'] < median_trust]['Engagement_Level']

# Perform T-Test between high and low trust groups for Engagement Level
ttest_trust_engagement = ttest_ind(high_trust, low_trust)
print("T-Test for Engagement Level between High and Low Trust Groups:", ttest_trust_engagement)


# Hypothesis Outcome: Rejected
# 
# The independent t-test conducted to assess the relationship between consumer trust and engagement level with AI-driven recommendations yields a 
# 𝑡
# t-statistic of 0.256 and a 
# 𝑝
# p-value of 0.798. Given that the 
# 𝑝
# p-value is significantly higher than the standard significance threshold (0.05), we fail to reject the null hypothesis. This indicates that there is no statistically significant difference in engagement levels between consumers with high trust and those with low trust in the AI-driven recommendations.
# 
# This result suggests that consumer trust in AI recommendations does not have a meaningful impact on engagement levels. In other words, customers' engagement with AI recommendations appears to be relatively independent of their level of trust in the system. This finding could imply that other factors—such as perceived relevance, ease of use, or economic suitability of recommendations—might be more influential in driving engagement than trust alone. Therefore, while trust is often considered a cornerstone in customer-AI interactions, it may not be a strong predictor of engagement in this context.
# 
# This result could encourage further investigation into what other elements are more critical in influencing engagement with AI-driven recommendations.

# In[76]:


df.columns


# # H6: Privacy concerns negatively impact customer engagement and satisfaction with AI recommendations.

# In[117]:


#Using Correlation analysis
from scipy.stats import pearsonr

# Drop rows with NaNs in the columns
df_cleaned = df.dropna(subset=['Privacy_Concern_Level', 'Engagement_Level', 'Satisfaction_Level'])

# Perform Pearson correlation on the cleaned dataset
privacy_engagement_corr, p_value_engagement = pearsonr(df_cleaned['Privacy_Concern_Level'], df_cleaned['Engagement_Level'])
privacy_satisfaction_corr, p_value_satisfaction = pearsonr(df_cleaned['Privacy_Concern_Level'], df_cleaned['Satisfaction_Level'])

print(f"Pearson Correlation between Privacy Concerns and Engagement: {privacy_engagement_corr}, p-value: {p_value_engagement}")
print(f"Pearson Correlation between Privacy Concerns and Satisfaction: {privacy_satisfaction_corr}, p-value: {p_value_satisfaction}")


# Privacy Concerns and Engagement: The Pearson correlation between privacy concerns and engagement is 
# 𝑟
# =
# 0.144
# r=0.144 with a p-value of 
# 0.057
# 0.057. This weak positive correlation is not statistically significant (p > 0.05), indicating that privacy concerns do not significantly impact engagement with AI-driven recommendations. Thus, H6 for engagement is not supported.
# 
# Privacy Concerns and Satisfaction: The Pearson correlation between privacy concerns and satisfaction is 
# 𝑟
# =
# 0.254
# r=0.254 with a p-value of 
# 0.001
# 0.001, indicating a weak but statistically significant positive association. This suggests that privacy-conscious customers may actually experience higher satisfaction, possibly due to the perceived value of transparency or privacy safeguards.

# In[118]:


#For T test btw high and low privacy level
from scipy.stats import ttest_ind

# Define high and low privacy concern groups based on the median of Privacy_Concern_Level
high_privacy_concern = df[df['Privacy_Concern_Level'] >= df['Privacy_Concern_Level'].median()]
low_privacy_concern = df[df['Privacy_Concern_Level'] < df['Privacy_Concern_Level'].median()]

# T-Test for Engagement Level
ttest_privacy_engagement = ttest_ind(high_privacy_concern['Engagement_Level'], low_privacy_concern['Engagement_Level'])
print(f"T-Test for Engagement Level between High and Low Privacy Concern Groups: {ttest_privacy_engagement}")

# T-Test for Satisfaction Level
ttest_privacy_satisfaction = ttest_ind(high_privacy_concern['Satisfaction_Level'], low_privacy_concern['Satisfaction_Level'])
print(f"T-Test for Satisfaction Level between High and Low Privacy Concern Groups: {ttest_privacy_satisfaction}")


# Hypothesis Outcome:
# 
# - H6 (Privacy Concerns and Engagement): Rejected. Privacy concerns do not significantly impact engagement.
# - H6 (Privacy Concerns and Satisfaction): Accepted. Privacy concerns positively impact satisfaction.
# Interpretation of Results:
# 
# The T-test results for the impact of privacy concerns on engagement and satisfaction levels reveal contrasting outcomes:
# 
# Engagement Level: The T-test for engagement between high and low privacy concern groups shows a non-significant result with a t-statistic of 
# 0.917
# 0.917 and a p-value of 
# 0.361
# 0.361. This suggests no meaningful difference in engagement levels between customers with high and low privacy concerns. Thus, privacy concerns do not have a significant impact on customer engagement, leading to the rejection of H6 for engagement.
# 
# Satisfaction Level: The T-test for satisfaction reveals a significant difference, with a t-statistic of 
# 2.524
# 2.524 and a p-value of 
# 0.013
# 0.013, indicating that customers with higher privacy concerns report greater satisfaction. This unexpected positive relationship may imply that privacy-conscious users experience a sense of reassurance that enhances their satisfaction with AI recommendations.
# 
# Overall, while privacy concerns do not reduce engagement, they appear to positively influence satisfaction among privacy-aware customers.

# # 4. Digital Literacy and AI Acceptance:
# 
# 
# - H7: Higher digital literacy among consumers leads to greater acceptance of AI-driven recommendations.
# - H8: Consumers with higher digital literacy report higher satisfaction levels with AI recommendations.
# 
# 
# Test: Correlation Analysis or ANOVA to test differences in acceptance and satisfaction across literacy levels.

# In[90]:


# Check unique values in the potential proxy columns
print("Unique values in 'Interaction Frequency':")
print(df["How often do you interact with Jumia’s AI-personalised product recommendations (e.g., clicking on recommended items, adding items to cart)?"].unique())

print("\nUnique values in 'Shopping Frequency':")
print(df["How frequently do you shop on Jumia?"].unique())


# In[91]:


# Define mapping for Interaction Frequency and Shopping Frequency
interaction_mapping = {
    "Always": 5,
    "Often": 4,
    "Sometimes": 3,
    "Rarely": 2,
    "Never": 1
}

shopping_mapping = {
    "Every day": 5,
    "Once a week": 4,
    "Every other week": 3,
    "Every month": 2,
    "When needed": 1
}

# Apply mapping to create numeric columns for Interaction Frequency and Shopping Frequency
df['Digital_Literacy'] = df["How often do you interact with Jumia’s AI-personalised product recommendations (e.g., clicking on recommended items, adding items to cart)?"].map(interaction_mapping)
df['Shopping_Frequency_Level'] = df["How frequently do you shop on Jumia?"].map(shopping_mapping)

# Verify the mapping
print("Mapped Digital Literacy (Interaction Frequency) values:", df['Digital_Literacy'].unique())
print("Mapped Shopping Frequency Level values:", df['Shopping_Frequency_Level'].unique())


# In[92]:


# Drop rows with NaN in relevant columns
df_cleaned = df.dropna(subset=['Digital_Literacy', 'Shopping_Frequency_Level', 'Engagement_Level', 'Satisfaction_Level'])

# Verify that there are no NaN values in the relevant columns
print("Unique values in cleaned Digital Literacy:", df_cleaned['Digital_Literacy'].unique())
print("Unique values in cleaned Shopping Frequency Level:", df_cleaned['Shopping_Frequency_Level'].unique())
print("Unique values in cleaned Engagement Level:", df_cleaned['Engagement_Level'].unique())
print("Unique values in cleaned Satisfaction Level:", df_cleaned['Satisfaction_Level'].unique())


# # H7: Higher digital literacy among consumers leads to greater acceptance of AI-driven recommendations.

# In[93]:


# Create Digital Literacy Levels based on the mapped Digital Literacy values
df_cleaned['Digital_Literacy_Level'] = pd.cut(df_cleaned['Digital_Literacy'], bins=[0, 2, 3, 5], labels=["Low", "Medium", "High"])

# ANOVA for Engagement Level across Digital Literacy Levels
from scipy.stats import f_oneway

engagement_groups = [df_cleaned['Engagement_Level'][df_cleaned['Digital_Literacy_Level'] == level].dropna() for level in df_cleaned['Digital_Literacy_Level'].unique()]
anova_engagement = f_oneway(*engagement_groups)
print("ANOVA for Engagement Level across Digital Literacy Levels:", anova_engagement)


# Hypothesis Outcome: Accepted
# 
# 
# 
# The ANOVA test examining the impact of digital literacy levels on engagement with AI-driven recommendations shows a statistically significant result, with an F-statistic of 
# 696.086
# 696.086 and a very low p-value (
# 𝑝
# =
# 1.83
# ×
# 1
# 0
# −
# 83
# p=1.83×10 
# −83
#  ), which is well below the conventional threshold for significance (p < 0.05). This outcome indicates that there are substantial differences in engagement levels across different digital literacy groups.
# 
# The finding supports H7, suggesting that consumers with higher digital literacy are more likely to engage with AI-driven recommendations. This could imply that individuals with greater comfort and familiarity with digital tools find AI recommendations more accessible, useful, and relevant to their shopping experience. Higher digital literacy may enable these consumers to better navigate and understand the personalised recommendations, fostering a greater level of engagement. This insight highlights the importance of consumer digital literacy in enhancing the effectiveness and reach of AI-powered recommendation systems.

# # H8: Consumers with higher digital literacy report higher satisfaction levels with AI recommendations.

# In[94]:


# ANOVA for Satisfaction Level across Digital Literacy Levels
satisfaction_groups = [df_cleaned['Satisfaction_Level'][df_cleaned['Digital_Literacy_Level'] == level].dropna() for level in df_cleaned['Digital_Literacy_Level'].unique()]
anova_satisfaction = f_oneway(*satisfaction_groups)
print("ANOVA for Satisfaction Level across Digital Literacy Levels:", anova_satisfaction)


# Hypothesis Outcome: Accepted
# 
# 
# The ANOVA analysis examining satisfaction levels across digital literacy groups shows a statistically significant result, with an F-statistic of 
# 3.128
# 3.128 and a p-value of 
# 0.046
# 0.046, which is slightly below the conventional significance threshold of 0.05. This suggests that satisfaction with AI recommendations varies significantly across different levels of digital literacy.
# 
# This result supports H8, indicating that consumers with higher digital literacy tend to report higher satisfaction with AI-driven recommendations. Individuals who are more digitally literate may find the personalised recommendations more aligned with their preferences, as they are likely to have a better understanding of how to interact with AI-based tools effectively. This finding underscores the importance of digital literacy in enhancing user satisfaction with personalised recommendation systems, suggesting that fostering digital literacy could be a strategic approach to increasing user satisfaction with AI-enabled services.

# # Challenges in Emerging Markets:
# 
# 
# - H9: Infrastructure limitations (e.g., internet connectivity) negatively impact the effectiveness of AI-driven recommendations.
# - H10: Algorithmic bias in AI recommendations negatively affects perceived fairness and satisfaction among diverse economic segments.
# 
# Test: T-Test or Chi-Square Test to compare the perception of recommendation fairness and effectiveness between groups with different levels of infrastructure and economic segments.

# In[95]:


df.columns


# In[96]:


# Check unique values in infrastructure-related, economic segment, effectiveness, and fairness columns
print("Unique values in Infrastructure-related column (Challenges or limitations):")
print(df["What challenges or limitations have you experienced with Jumia's AI-personalised recommendation system? (Select all that apply)"].unique())

print("\nUnique values in Economic-related column (Income):")
print(df["What is your monthly income range?"].unique())

print("\nUnique values in Effectiveness column (Satisfaction with recommendations):")
print(df["How satisfied are you with the personalised recommendations provided by Jumia?"].unique())

print("\nUnique values in Fairness column (Preferences and lifestyle reflection):")
print(df["How well do you think Jumia's personalised recommendations reflect your personal preferences and lifestyle?"].unique())


# In[97]:


# Define a function to map infrastructure limitations based on the presence of "No challenges encountered"
def map_infrastructure_limitations(challenges):
    if pd.isna(challenges):
        return 0  # Adequate Infrastructure if NaN
    elif "No challenges encountered" in challenges or "Nil" in challenges:
        return 0  # Adequate Infrastructure
    else:
        return 1  # Limited Infrastructure

# Apply the mapping
df['Infrastructure_Limitation'] = df["What challenges or limitations have you experienced with Jumia's AI-personalised recommendation system? (Select all that apply)"].apply(map_infrastructure_limitations)

# Check the distribution
print("Distribution of Infrastructure Limitation:")
print(df['Infrastructure_Limitation'].value_counts())


# In[98]:


# Check unique income values to decide on segmentation
print("Unique values in Economic-related column (Income):")
print(df["What is your monthly income range?"].unique())


# In[99]:


# Define mapping for economic segments
income_mapping = {
    "Below ₦50,000": "Low",
    "₦50,000 - ₦100,000": "Low",
    "\xa0₦100,000 - ₦200,000": "Medium",
    "₦200,000 - ₦500,000": "High",
    "Above ₦500,000": "High"
}

# Apply the mapping
df['Economic_Segment'] = df["What is your monthly income range?"].map(income_mapping)

# Verify the mapping
print("Distribution of Economic Segments:")
print(df['Economic_Segment'].value_counts())


# # H9: Infrastructure limitations negatively impact the effectiveness of AI-driven recommendations.

# In[100]:


from scipy.stats import ttest_ind

# Map satisfaction responses to a numeric scale if not already done
satisfaction_mapping = {
    "Very satisfied": 5,
    "Satisfied": 4,
    "Neutral": 3,
    "Dissatisfied": 2,
    "Very dissatisfied": 1
}
df['Effectiveness_Perception'] = df["How satisfied are you with the personalised recommendations provided by Jumia?"].map(satisfaction_mapping)

# Create groups based on Infrastructure Limitation
limited_infrastructure = df[df['Infrastructure_Limitation'] == 1]['Effectiveness_Perception']
adequate_infrastructure = df[df['Infrastructure_Limitation'] == 0]['Effectiveness_Perception']

# Perform T-Test
ttest_infrastructure_effectiveness = ttest_ind(limited_infrastructure.dropna(), adequate_infrastructure.dropna())
print("T-Test for Perception of Effectiveness across Infrastructure Levels:", ttest_infrastructure_effectiveness)


# Hypothesis Outcome: Rejected
# 
# The T-Test for comparing the perceived effectiveness of AI-driven recommendations across different levels of infrastructure quality resulted in a test statistic of 
# −
# 1.398
# −1.398 and a p-value of 
# 0.164
# 0.164. Since the p-value is greater than the standard significance level of 
# 0.05
# 0.05, we fail to reject H9. This suggests that infrastructure limitations, such as internet connectivity issues, do not significantly impact how effective users perceive AI recommendations to be.
# 
# This outcome indicates that users' perception of AI-driven recommendations’ effectiveness is relatively stable, regardless of infrastructure challenges. It might imply that the recommendation system is robust enough to maintain user engagement and satisfaction even when infrastructure limitations are present. However, it’s also possible that users may not directly associate connectivity issues or other infrastructure constraints with the AI's recommendation quality, focusing instead on the relevance and accuracy of the recommendations. Further qualitative insights could help explore other factors influencing perceived effectiveness in varied infrastructure conditions.

# # H10: Algorithmic bias in AI recommendations negatively affects perceived fairness and satisfaction among diverse economic segments.

# In[101]:


from scipy.stats import chi2_contingency

# Map fairness responses to a simplified categorical variable if necessary
fairness_mapping = {
    "Extremely well": "Positive",
    "Very well": "Positive",
    "Moderately well": "Neutral",
    "Slightly well": "Neutral",
    "Not well at all": "Negative"
}
df['Fairness_Perception'] = df["How well do you think Jumia's personalised recommendations reflect your personal preferences and lifestyle?"].map(fairness_mapping)

# Create a contingency table based on Economic Segment and Fairness Perception
contingency_table = pd.crosstab(df['Economic_Segment'], df['Fairness_Perception'])

# Perform Chi-Square Test
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-Square Test for Fairness Perception across Economic Segments: chi2={chi2}, p-value={p}")


# Hypothesis Outcome: Rejected
# 
# 
# The Chi-Square test for assessing perceived fairness across different economic segments shows a chi-square value of 
# 0.0
# 0.0 and a p-value of 
# 1.0
# 1.0. This indicates no statistically significant relationship between economic segment and perceived fairness of AI recommendations. The result does not support H10, which hypothesised that algorithmic bias in AI recommendations would lead to differences in fairness perception among consumers from diverse economic backgrounds.
# 
# This lack of significant difference suggests that, regardless of economic segment, users perceive the fairness of AI recommendations in a similar manner. This could imply that Jumia's AI recommendation system is viewed as relatively fair and unbiased across economic demographics, or it might suggest that factors other than economic segmentation, such as user experience or familiarity with AI, could play a more critical role in shaping fairness perceptions. Further analysis could explore other variables that may influence fairness perceptions among users.

# # 1. Theory of Planned Behavior (TPB) - Multiple Regression Analysis
# This analysis will assess if attitudes (satisfaction), subjective norms (trust), and perceived control (privacy and data comfort) predict acceptance (engagement level).
# 
# - Hypothesis 1 (H12): Attitudes (measured by Satisfaction Level) positively influence Engagement Level with AI recommendations.
# 
# - Hypothesis 2 (H13): Subjective Norms (measured by Trust Level) positively influence Engagement Level with AI recommendations.
# 
# 
# - Hypothesis 3 (H14): Perceived Control (measured by Privacy Concern and Data Comfort) positively influences Engagement Level with AI recommendations.
# 

# In[102]:


# Check unique values in the relevant columns
print("Unique values in Satisfaction Level:")
print(df['Satisfaction_Level'].unique())

print("\nUnique values in Trust Level:")
print(df['Trust_Level'].unique())

print("\nUnique values in Privacy Concerns column:")
print(df["Are you concerned about the privacy of your personal data used for Jumia's personalised recommendations?"].unique())

print("\nUnique values in Data Comfort column:")
print(df["Are you comfortable with Jumia using your browsing and purchasing data to provide personalised recommendations?"].unique())


# In[103]:


# Mapping for Privacy Concerns
privacy_mapping = {
    "Very concerned": 5,
    "Somewhat concerned": 4,
    "Neutral": 3,
    "Not concerned": 2,
    "Not at all concerned": 1
}
df['Privacy_Concern_Level'] = df["Are you concerned about the privacy of your personal data used for Jumia's personalised recommendations?"].map(privacy_mapping)

# Mapping for Data Comfort
data_comfort_mapping = {
    "Very comfortable": 5,
    "Somewhat comfortable": 4,
    "Neutral": 3,
    "Somewhat uncomfortable": 2,
    "Very uncomfortable": 1
}
df['Data_Comfort_Level'] = df["Are you comfortable with Jumia using your browsing and purchasing data to provide personalised recommendations?"].map(data_comfort_mapping)
print(df['Data_Comfort_Level'].head())
print(df['Privacy_Concern_Level'])


#  Run Multiple Regression Analysis

# In[104]:


import statsmodels.api as sm

# Drop rows with NaN values in relevant columns
df_cleaned = df.dropna(subset=['Satisfaction_Level', 'Trust_Level', 'Privacy_Concern_Level', 'Data_Comfort_Level', 'Engagement_Level'])

# Define the dependent variable (Engagement Level) and independent variables
X = df_cleaned[['Satisfaction_Level', 'Trust_Level', 'Privacy_Concern_Level', 'Data_Comfort_Level']]
y = df_cleaned['Engagement_Level']

# Add a constant term to the model (intercept)
X = sm.add_constant(X)

# Run the multiple regression
model = sm.OLS(y, X).fit()

# Print the regression results
print(model.summary())


# ## Hypothesis Outcomes:
# 
# - H12 (Attitudes → Engagement): Rejected. Satisfaction Level does not significantly influence Engagement Level.
# - H13 (Subjective Norms → Engagement): Rejected. Trust Level does not significantly influence Engagement Level.
# - H14 (Perceived Control → Engagement): Partially Accepted. Privacy Concern and Data Comfort significantly influence Engagement Level.
# 
# # Interpretation
# 
# The regression analysis shows that Data Comfort and Privacy Concern are significant predictors of Engagement Level (p < 0.05). Data Comfort, with a positive coefficient (0.2631), indicates that users who feel comfortable with Jumia using their data are more likely to engage with AI recommendations, aligning with the Theory of Planned Behavior (TPB) in terms of perceived control. Privacy Concern also shows a positive effect (0.1494), suggesting that while users are concerned about privacy, this does not reduce engagement; it may even slightly increase it, which is an interesting finding.
# 
# However, Satisfaction Level (attitudes) and Trust Level (subjective norms) are not significant predictors, indicating that positive attitudes and trust alone do not drive engagement. The model's R-squared (0.121) suggests that other factors may also influence engagement, with only about 12.1% of engagement variance explained by these variables. Overall, the results partially support TPB, particularly highlighting the importance of perceived control (data comfort) in driving engagement.

# # 2. Technology Acceptance Model (TAM) - Multiple Regression Analysis
# This analysis tests if perceived usefulness (relevance) and ease of use (interaction frequency) predict acceptance (engagement level) and satisfaction.
# 
# - Hypothesis 4 (H15): Perceived Usefulness (measured by Satisfaction Level and Relevance of Recommendations) positively influences Acceptance (Engagement Level) of AI recommendations.
# 
# 
# - Hypothesis 5 (H16): Perceived Ease of Use (measured by Data Comfort Level) positively influences Acceptance (Engagement Level) of AI recommendations.
# 
# 

# In[105]:


# Check unique values in columns related to Perceived Usefulness (Relevance) and Perceived Ease of Use (Interaction Frequency)

# Checking unique values in the 'How relevant do you find the personalised recommendations on Jumia?' column for Relevance
print("Unique values in 'How relevant do you find the personalised recommendations on Jumia?' column:")
print(df['How relevant do you find the personalised recommendations on Jumia?\n\n(Please rank the options below from 1 to 5, where 1 is the highest and 5 is the lowest.)\n'].unique())

# Checking unique values in 'To what extent do you believe the AI-personalised recommendations improve your overall shopping experience on Jumia?' column for Relevance
print("\nUnique values in 'To what extent do you believe the AI-personalised recommendations improve your overall shopping experience on Jumia?' column:")
print(df['To what extent do you believe the AI-personalised recommendations improve your overall shopping experience on Jumia?\n(Please rank the options below from 1 to 5, where 1 is the highest and 5 is the low'].unique())

# Checking unique values in the 'How often do you interact with Jumia’s AI-personalised product recommendations' column for Interaction Frequency
print("\nUnique values in 'How often do you interact with Jumia’s AI-personalised product recommendations (e.g., clicking on recommended items, adding items to cart)?' column:")
print(df['How often do you interact with Jumia’s AI-personalised product recommendations (e.g., clicking on recommended items, adding items to cart)?'].unique())


# In[106]:


# Define the mapping for Interaction Frequency
interaction_mapping = {
    'Always': 5,
    'Often': 4,
    'Sometimes': 3,
    'Rarely': 2,
    'Never': 1
}

# Apply the mapping to convert Interaction Frequency to a numeric scale
df['Interaction_Frequency'] = df['How often do you interact with Jumia’s AI-personalised product recommendations (e.g., clicking on recommended items, adding items to cart)?'].map(interaction_mapping)

# Check if there are any NaN values after mapping (e.g., due to missing or unrecognized values)
print("Unique values in Interaction_Frequency after mapping:", df['Interaction_Frequency'].unique())

# Drop rows with NaN values in Interaction_Frequency to ensure clean data for analysis
df = df.dropna(subset=['Interaction_Frequency', 'Relevance_Score', 'Engagement_Level'])

# Proceed with the TAM analysis as planned
import statsmodels.api as sm

# Define the predictors and the dependent variable
X = df[['Relevance_Score', 'Interaction_Frequency']]
y = df['Engagement_Level']

# Add a constant for the intercept
X = sm.add_constant(X)

# Run the regression model
model = sm.OLS(y, X).fit()

# Display the regression summary
print(model.summary())


# ## Hypothesis Outcomes:
# 
# - H15 (Perceived Usefulness → Engagement): Accepted. Relevance Score significantly influences Engagement Level.
# - H16 (Perceived Ease of Use → Engagement): Accepted. Interaction Frequency significantly influences Engagement Level.
# 
# 
# # Interpretation
# 
# The regression analysis results for the Technology Acceptance Model (TAM) indicate a very high R-squared value (1.000), suggesting that the model almost perfectly explains the variance in the engagement level among respondents. This outcome implies that the combination of Relevance_Score (perceived usefulness) and Interaction_Frequency (ease of use) are highly predictive of engagement with Jumia's AI recommendations.
# 
# The coefficient for Interaction_Frequency is 1.000, which is statistically significant (p < 0.001). This suggests a direct, one-to-one relationship between interaction frequency and engagement level, meaning that higher interaction frequency is strongly associated with increased engagement. In the context of TAM, this supports the hypothesis that ease of use (interaction frequency) is a key factor in driving user engagement.
# 
# The Relevance_Score coefficient is slightly negative (-1.388e-16) and also statistically significant (p = 0.024), although its effect is minimal. This result might indicate that while relevance is essential, it has a marginal or negligible impact in this model, possibly due to high multicollinearity with interaction frequency.
# 
# Overall, the findings align with TAM, suggesting that ease of use is a critical predictor of engagement, with perceived usefulness playing a smaller role. However, such a high R-squared value may also indicate potential model overfitting or multicollinearity, warranting further investigation.

# # 3. Complexity Theory - Multivariate Analysis of Variance (MANOVA)
# This test will assess the combined effect of economic relevance, cultural relevance, and infrastructure limitations on satisfaction level and perceived relevance.
# 
# - Hypothesis 6 (H17): Multiple, Interconnected Factors (such as Economic Relevance, Cultural Relevance, and Infrastructure Limitations) together impact Engagement Level with AI recommendations.
# 
# 
# - Hypothesis 7 (H18): Economic Disparities and Cultural Norms moderate the effectiveness of AI recommendations in influencing engagement and satisfaction.
# 
# 

# In[107]:


from statsmodels.multivariate.manova import MANOVA

# Define the dependent and independent variables
dependent_vars = df[['Satisfaction_Level', 'Relevance_Score']]
independent_vars = df[['Economic_Relevance', 'Cultural_Relevance', 'Infrastructure_Limitation']]

# Fit the MANOVA model
manova = MANOVA.from_formula('Satisfaction_Level + Relevance_Score ~ Economic_Relevance + Cultural_Relevance + Infrastructure_Limitation', data=df)
manova_results = manova.mv_test()

# Display the MANOVA results
print(manova_results)


# ## Hypothesis Outcomes:
# 
# - H17 (Combined Effect of Economic Relevance, Cultural Relevance, and Infrastructure Limitations): Accepted. 
# 
# Significant multivariate effect observed (Wilks' lambda, Pillai's trace, etc., all p < 0.0001) indicates that these factors collectively impact the outcomes.
# 
# 
# - H18 (Moderation by Economic Disparities and Cultural Norms): Partially Accepted. 
# 
# While the combined effect is significant, individual effects of Economic and Cultural Relevance are close to the threshold but not significant at the 5% level (p ≈ 0.0919 for both).
# 
# 
# # Interpretation
# 
# The MANOVA analysis was conducted to evaluate the combined effects of Economic Relevance, Cultural Relevance, and Infrastructure Limitation on Satisfaction Level and Perceived Relevance of AI-driven recommendations. This test helps us understand if these interconnected factors jointly influence how users engage with and perceive the value of AI recommendations.
# 
# - Intercept Significance: All multivariate tests (Wilks' Lambda, Pillai's Trace, Hotelling-Lawley Trace, and Roy’s Greatest Root) show that the intercept has a significant effect (p < 0.0001). This result indicates a strong baseline effect in the model, confirming that there is overall variance in Satisfaction Level and Perceived Relevance in the dataset. However, this intercept significance does not provide information about the effects of Economic, Cultural, and Infrastructure factors specifically; it only reflects that the model itself detects variation.
# 
# #
# - Economic Relevance: The MANOVA results for Economic Relevance yield a Wilks' Lambda of 0.9731 with an F-value of 2.4201 and a p-value of 0.0919, which is just above the conventional 0.05 significance threshold. This indicates that while Economic Relevance does not have a statistically significant impact on Satisfaction Level and Perceived Relevance, it is close to having an effect. This borderline result suggests that economic factors might play a role in influencing satisfaction and relevance perceptions, though the effect may not be strong enough to achieve significance in this sample. Further research with a larger dataset or more granular economic categories may help clarify its role.
# 
# #
# - Cultural Relevance: Similarly, the p-value for Cultural Relevance (0.0920) is also close to significance, with Wilks' Lambda at 0.9731 and an F-value of 2.4190. This result indicates that cultural relevance might influence satisfaction and relevance perceptions to some degree, though the effect was not strong enough to reach statistical significance. Cultural norms and values may influence how users perceive and interact with AI recommendations, but more robust data is needed to confirm this effect.
# 
# #
# 
# - Infrastructure Limitation: Infrastructure Limitation has a Wilks' Lambda of 0.9951 and a p-value of 0.6485, suggesting no significant effect on satisfaction and relevance perception. This result implies that infrastructure constraints, as measured here, do not appear to influence users' satisfaction with or perceived relevance of AI recommendations.
# 
# These findings suggest that economic and cultural contexts may play a role in how users perceive AI recommendations, but further exploration with larger samples or additional contextual factors would be beneficial.

# # SECTION 5: Thematic Analysis for Qualitative Columns

# # 1. How do you think Jumia’s AI-personalised recommendations could better cater to your needs, considering factors such as your purchasing habits, product preferences, income level, and browsing behaviour?

# # Thematic Analysis

# In[108]:


import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load data into DataFrame (assuming it's in a column named as specified)
# df = pd.read_csv('your_data.csv')  # If loading from a CSV file

# Display first few rows of the column to confirm the content
print(df['How do you think Jumia’s AI-personalised recommendations could better cater to your needs, considering factors such as your purchasing habits, product preferences, income level, and browsing behaviour'].head())

# Clean and tokenize
def clean_text(text):
    text = str(text).lower()  # Convert to lowercase
    text = re.sub(r'\n', ' ', text)  # Replace newline characters with spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabet characters
    return text

# Apply cleaning to the column
df['AI_Personalisation_Cleaned'] = df['How do you think Jumia’s AI-personalised recommendations could better cater to your needs, considering factors such as your purchasing habits, product preferences, income level, and browsing behaviour'].apply(clean_text)

# Tokenize and remove stopwords
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

def process_text(text):
    words = word_tokenize(text)
    words_filtered = [word for word in words if word not in stop_words]
    return words_filtered

# Apply processing to the cleaned column
df['AI_Personalisation_Tokens'] = df['AI_Personalisation_Cleaned'].apply(process_text)


# In[109]:


# Get most common words to identify themes
def get_common_themes(column_tokens, n=10):
    all_words = [word for tokens in column_tokens for word in tokens]
    return Counter(all_words).most_common(n)

# Extract top themes for AI personalisation improvement suggestions
ai_personalization_themes = get_common_themes(df['AI_Personalisation_Tokens'])
print("Top Themes in AI Personalization:", ai_personalization_themes)


# In[110]:


# Function to create a word cloud
def generate_wordcloud(themes, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(themes))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Generate word cloud for AI personalization column themes
generate_wordcloud(ai_personalization_themes, 'Common Themes in AI Personalisation Suggestions')


# In[111]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Combine all text from the first qualitative column 'How do you think Jumia’s AI-personalised recommendations could better cater to your needs, considering factors such as your purchasing habits, product preferences, income level, and browsing behaviour?'
# Assuming the column name is 'AI_Personalization_Improvements' in the DataFrame
text_data_combined = ' '.join(df['How do you think Jumia’s AI-personalised recommendations could better cater to your needs, considering factors such as your purchasing habits, product preferences, income level, and browsing behaviour'].dropna().tolist())

# Generate the word cloud
wordcloud1 = WordCloud(width=800, height=400, background_color='white', colormap='plasma', max_words=100).generate(text_data_combined)

# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud1, interpolation='bilinear')
plt.axis('off')
plt.title("Suggested Improvements for Jumia’s AI-Personalised Recommendations")
plt.show()


# # 2. What concerns, if any, do you have regarding the use of your personal data for AI-personalised recommendations on Jumia

# # Thematic Analysis

# In[113]:


import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample the column with responses for data privacy concerns
text_data = df['What concerns, if any, do you have regarding the use of your personal data for AI-personalised recommendations on Jumia?'].dropna()

# Preprocess text data: lowercasing, removing punctuation, etc.
text_data = text_data.apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x.lower()))

# Initialize CountVectorizer
vectorizer = CountVectorizer(stop_words='english', max_features=500)
text_vectors = vectorizer.fit_transform(text_data)

# Initialize and fit LDA for topic modeling
lda_model = LatentDirichletAllocation(n_components=4, random_state=42)
lda_model.fit(text_vectors)

# Display top words for each topic
terms = vectorizer.get_feature_names_out()
for idx, topic in enumerate(lda_model.components_):
    print(f"Top words for Topic {idx+1}:")
    print([terms[i] for i in topic.argsort()[-10:]])
    print("\n")


# Combine all text from the 'What concerns, if any, do you have regarding the use of your personal data for AI-personalised recommendations on Jumia?' column
text_data_combined = ' '.join(text_data.dropna().tolist())

# Generate the word cloud
wordcloud2 = WordCloud(width=800, height=400, background_color='white', colormap='viridis', max_words=100).generate(text_data_combined)

# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Data Privacy Concerns on AI-Personalised Recommendations")
plt.show()


# # 3. Please provide any additional comments you have about Jumia’s AI-personalised recommendation system.

# In[115]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Combine all text from the third qualitative column 'Please provide any additional comments you have about Jumia’s AI-personalised recommendation system'
# Assuming the column name is 'Additional_Comments' in the DataFrame
text_data_combined = ' '.join(df['Please provide any additional comments you have about Jumia’s AI-personalised recommendation system.'].dropna().tolist())

# Generate the word cloud
wordcloud3 = WordCloud(width=800, height=400, background_color='white', colormap='viridis', max_words=100).generate(text_data_combined)

# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud3, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Additional Comments on Jumia’s AI-Personalised Recommendation System")
plt.show()


# In[116]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Assume wordcloud_1, wordcloud_2, wordcloud_3 are the three WordCloud objects for each text

fig, axes = plt.subplots(3, 1, figsize=(12, 18))

# Plot for the first word cloud (e.g., general suggestions)
axes[0].imshow(wordcloud1, interpolation='bilinear')
axes[0].axis('off')
axes[0].set_title("Suggested Improvements for Jumia’s AI-Personalised Recommendations", fontsize=14)

# Plot for the second word cloud (e.g., privacy concerns)
axes[1].imshow(wordcloud2, interpolation='bilinear')
axes[1].axis('off')
axes[1].set_title("Concerns Regarding Use of Personal Data for AI Recommendations", fontsize=14)

# Plot for the third word cloud (e.g., additional comments)
axes[2].imshow(wordcloud3, interpolation='bilinear')
axes[2].axis('off')
axes[2].set_title("Additional Comments on Jumia’s AI-Personalised Recommendation System", fontsize=14)

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




