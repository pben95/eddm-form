import csv

#ONLY MODIFY BELOW



bundle_size = 50
permit_holder = "Postal Wizards"
permit_number = "842"
input_filename = "data.csv"
output_filename = "EDDM_form.csv"

#ONLY MODIFY ABOVE

def generate_csv(routes, bundle_size, permit_holder, permit_number, output_file):
    headers = ["zipcode", "crrt", "bmc", "bundle size", "bundle number", "count", "permit holder", "permit #"]

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for route in routes:
            zipcode = route["crrt"][:5]
            crrt = route["crrt"][5:]
            bmc = route["bmc"]
            addresses = route["addresses"]

            full_bundles = addresses // bundle_size
            remainder = addresses % bundle_size
            if remainder < (bundle_size * .25):
                full_bundles -= 1
                remainder += bundle_size
            count = 0
            for i in range(full_bundles):
                count += bundle_size
                writer.writerow([zipcode, crrt, bmc, bundle_size, i+1, count, permit_holder, permit_number])
            
            if remainder > 0:
                count += remainder
                writer.writerow([zipcode, crrt, bmc, remainder, full_bundles+1, count, permit_holder, permit_number])

            writer.writerow(["xxx", "xxx", "xxx", "xxx", "xxx", "xxx", "xxx"])
            
    print(f"CSV file '{output_file}' generated successfully.")

def load_routes(input_file):

    routes = []
    with open(input_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            routes.append({
                "crrt": row["crrt"],
                "bmc": row["bmc"],
                "addresses": int(row["addresses"])
            })
        return routes

routes_data = load_routes(input_filename)
generate_csv(routes_data, bundle_size, permit_holder, permit_number, output_filename)