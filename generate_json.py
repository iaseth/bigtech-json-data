import csv
import json
import os



def main():
	companies = []
	with open('raw/companiesmarketcap.com - Largest tech companies by market cap.csv', newline='') as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			company = {}
			company["rank"] = row[0]
			company["name"] = row[1]
			company["symbol"] = row[2]
			company["marketCap"] = row[3]
			company["priceUsd"] = row[4]
			company["country"] = row[5]
			companies.append(company)

	jo = {}
	jo["companies"] = companies
	output_json_path = "bigtech-market-cap.json"
	with open(output_json_path, "w") as f:
		json.dump(jo, f, indent="\t")
	print(f"Saved: {output_json_path} [{len(companies)} companies]")


if __name__ == '__main__':
	main()
