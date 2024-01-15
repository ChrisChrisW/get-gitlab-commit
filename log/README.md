# Git Repository Author Analysis

This repository contains data analysis and visualization of Git commit history from a Git repository log. The analysis includes:

1. Cleaning and preprocessing the data.
2. Renaming author names for consistency.
3. Counting the number of commits for each author.
4. Visualizing commit counts with a histogram and a pie chart.
5. Extracting and displaying author emails.

## Analysis of Commit Data

The analysis is performed on the commit data to gain insights into the contribution of different authors. Key steps include:

### Data Cleaning

Entries with the "Author Name" equal to "Christophe WANG" were removed from the dataset to ensure data consistency.

### Author Name Standardization

Author names were standardized for better analysis. Notable changes include:

- "Hugo0x18" to "Hugo Boutot"
- "Teddy Not Bear" and "TeddyNotBear" to "Jean-François Teddy"
- "LIM Jacky" to "Jacky LIM"
- "Nas f" to "Nacer Fl"

### Commit Count per Author

A histogram was created to visualize the number of commits made by each author. The histogram provides insights into the author's contribution to the repository.

### Contribution of Authors

A pie chart was generated to visualize the contribution of all authors. The pie chart shows the percentage of commits made by each author relative to the total.

## Plots

### Histogram: Commit Count per Author

![Histogram](./output/commit_count_histogram.png)

### Pie Chart: Contribution of Authors

![Pie Chart](./output/contribution_pie_chart.png)

## Author Emails

The extracted author emails can be found in the "author_emails.txt" file. Each author's emails are listed for reference.

## Files

- [commit_count_histogram.png](./output/commit_count_histogram.png) - Histogram plot.
- [contribution_pie_chart.png](./output/contribution_pie_chart.png) - Pie chart plot.
- [author_emails.txt](./output/author_emails.txt) - Author emails.

For more details and code, please refer to the Jupyter Notebook in this repository.
