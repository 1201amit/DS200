import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re 
from textwrap import wrap
from scipy.ndimage.filters import gaussian_filter1d


def scatterPlot():
	def forward(x):
	    return x**(0.1)
	def inverse(x):
	    return x**(10)

	data = pd.read_csv('./data/Category-wise_Automobile_Production.csv')

	fig =plt.figure(figsize = (8,6))
	plt.scatter(data.iloc[3,:].values[2: 16], data.iloc[4,:].values[2: 16], s=100, alpha=0.7, label='Medium/Heavy Weight')
	plt.scatter(data.iloc[6,:].values[2: 16], data.iloc[7,:].values[2: 16], s=100, alpha=0.7,label='Light Weight')
	plt.scatter(data.iloc[10,:].values[2: 16], data.iloc[11,:].values[2: 16], s=100, alpha=0.7,label='Three Wheelers')

	plt.title("Annual production of vehicles from 2001-02 to 2014-15", fontsize=16)
	plt.legend(title='Vehicle Type')
	plt.xlabel('Number of Passenger Vehicles', fontsize=16)
	plt.ylabel('Number of Goods Vehicles', fontsize=16)

	plt.yscale('function', functions=(forward, inverse))
	plt.xscale('function', functions=(forward, inverse))
	plt.xticks(rotation=90) 
	plt.grid(linestyle=':', linewidth=1,)
	plt.savefig('ScatterPlot.png', format='png', dpi = 300, bbox_inches = 'tight')
	plt.show()


def boxPlot():
	data = pd.read_csv('./data/GDP_of_India_and_Major_Industrial_Sectors_of_Economy.csv')
	columns = data.columns[8:14].to_list()
	gdp_share = data[columns].dropna().to_numpy()
	labels = [re.split(r'\s-\s?Share', label)[0] for label in columns]
	wrapped_labels =  [ '\n'.join(wrap(l, 15)) for l in labels ]

	fig = plt.figure(figsize=(8,6))
	plt.boxplot(gdp_share, labels=wrapped_labels, vert=False)
	plt.gca().xaxis.grid(linestyle=':', linewidth=1,)
	plt.xlabel("Share in GDP [Rs. Cr.]", fontsize=16)
	plt.ylabel("Sectors", fontsize=16)
	plt.title("Contribution variability in total GDP from 1951-2012", fontsize=16)
	plt.savefig('BoxPlot.png', format='png', dpi = 300, bbox_inches = 'tight')
	plt.show()


def linePlot():
	data = pd.read_csv('./data/GDP_of_India_and_Major_Industrial_Sectors_of_Economy.csv')
	columns = data.columns[8:14].to_list()
	gdp_share = data[columns].dropna().to_numpy()
	labels = [re.split(r'\s-\s?Share', label)[0] for label in columns]
	wrapped_labels =  [ '\n'.join(wrap(l, 15)) for l in labels ]
	colors = ['tab:gray', 'tab:brown', 'tab:orange', 'tab:green', 'tab:pink', 'tab:cyan']

	fig = plt.figure(figsize=(15,8))
	for i in range(len(columns)):
	    col = columns[i]
	    c = colors[i]
	    x = data['Financial Year']
	    y = data[col]
	    plt.plot(data['Financial Year'],gaussian_filter1d(data[col], sigma=5), '-', alpha=1, c=c, label=labels[i], linewidth=2)
	    plt.plot(data['Financial Year'], data[col], 'o', alpha=0.3, c=c,)
	    
	plt.tick_params(axis='x', rotation=90, labelsize=10)
	plt.tick_params(axis='y', labelsize=10)
	plt.xlabel("Year", fontsize=16)
	plt.ylabel("Share in GDP [Rs. Cr.]", fontsize=16)
	plt.title("Contribution Trend in total GDP from 1951-2012", fontsize=16)
	plt.legend()
	plt.grid(alpha=0.2)
	plt.savefig('LinePlot.png', format='png', dpi = 300, bbox_inches = 'tight')
	plt.show()

def main():
	scatterPlot()
	boxPlot()
	linePlot()

if __name__ == '__main__':
	main()