import pandas as pd

#Load CSV file 
file_path = 'C:\\Users\\ysj04\\Downloads\\updated2.csv' #Replace with your own file path 
df = pd.read_csv(file_path)

#Replace streets accordingly with proper spelling and abbreviations extended
replacements = {             
    "STUPHIN BLVD": "SUTPHIN BOULEVARD", 
    "OSCAWANA LK RD": "OSCAWANA LAKE ROAD", 
    "NY25A": "NEW YORK 25A",        
    "VAN WYCK EXPY SR N": "VAN WYCK EXPRESSWAY SERVICE ROAD NORTH", 
    "VAN WYCK EXPY S SR": "VAN WYCK EXPRESSWAY SOUTH SERVICE ROAD",
    "VAN WYCK EXPY N SR": "VAN WYCK EXPRESSWAY NORTH SERVICE ROAD",
    "NASSAU COUNTY LINE": "NASSAU COUNTY BORDER, NEW YORK",
    "NY25A NORTHERN BLVD": "NEW YORK 25A NORTHERN BLVD",
    "JAMACIA AVE": "JAMAICA AVENUE",
    "NY25 HILLSIDE AVE": "NEW YORK 25 HILLSIDE AVENUE",
    "CROSS ISLAND PKWY WB": "CROSS ISLAND PARKWAY WESTBOUND",
    "GCP SR W": "GRAND CENTRAL PARKWAY SERVICE ROAD WEST",
    "IN495": "INTERSTATE 495",
    "CI PKWY SR N": "CROSS ISLAND PARKWAY SERVICE ROAD NORTH",
    "HOR HARDING EXWY SR N": "HARDING EXPRESSWAY SERVICE ROAD NORTH",
    "RT 907A CROSS ISLAND EXPY": "ROUTE 907A CROSS ISLAND EXPRESSWAY",
    "COLLEGE PT BLV": "COLLEGE POINT BOULEVARD",
    "MARINE PKWY BRG": "MARINE PARKWAY BRIDGE",
    "RIIS PARK ENT Ramp": "RIIS PARK ENTRANCE RAMP",
    "ROCKWY BCH BLVD": "ROCKAWAY BEACH BOULEVARD",
    "MRG BCH 169TH RMP": "MORGAN BEACH 169TH RAMP",
    "CI PKWY SR S": "CROSS ISLAND PARKWAY SERVICE ROAD SOUTH",
    "KINGS CO LINE": "KINGS COUNTY LINE",
    "VAN WYCK EXPY SR S": "VAN WYCK EXPRESSWAY SERVICE ROAD SOUTH",
    "HOR HARDING EXWY SR S": "HARDING EXPRESSWAY SERVICE ROAD SOUTH",
    "GRD CENTRL PKY": "GRAND CENTRAL PARKWAY",
    "FRAN LEWIS BLVD NB": "FRANCIS LEWIS BOULEVARD NORTHBOUND",
    "ACC I495": "ACCESS INTERSTATE 495",
    "FRAN LEWIS BLV": "FRANCIS LEWIS BOULEVARD",
    "CROSS IS PKWY SR S": "CROSS ISLAND PARKWAY SERVICE ROAD SOUTH",
    "CORP KENNDY ST": "CORPORAL KENNEDY STREET",
    "GRND CNTRL PKWY SR N": "GRAND CENTRAL PARKWAY SERVICE ROAD NORTH",
    "260TH ST CIR": "260TH STREET CIRCLE",
    "IN678 SR N": "INTERSTATE 678 SERVICE ROAD NORTH",
    "LITTLE NK PKWY": "LITTLE NECK PARKWAY",
    "HOLLIS CT BLVD SB": "HOLLIS COURT BOULEVARD SOUTHBOUND",
    "CLEARVIEW EXPY SR S": "CLEARVIEW EXPRESSWAY SERVICE ROAD SOUTH",
    "IN278": "INTERSTATE 278",
    "IN278 SR W": "INTERSTATE 278 SERVICE ROAD WEST",
    "ASTORIA BLVD NB": "ASTORIA BOULEVARD NORTHBOUND",
    "QUEENS BLVD NB": "QUEENS BOULEVARD NORTHBOUND",
    "METROPOLITN AV": "METROPOLITAN AVENUE",
    "I495": "INTERSTATE 495",
    "QUEENS BLVD N SR": "QUEENS BOULEVARD NORTH SERVICE ROAD",
    "IN278E": "INTERSTATE 278 EASTBOUND",
    "GRAND CNTRL PKWY SVC RD": "GRAND CENTRAL PARKWAY SERVICE ROAD",
    "QUEENS BLVD SR": "QUEENS BOULEVARD SERVICE ROAD",
    "BX QN EXWY W": "BRONX QUEENS EXPRESSWAY WESTBOUND",
    "LITTLENECK PKY": "LITTLE NECK PARKWAY",
    "COMMNWLTH BLVD": "COMMONWEALTH BOULEVARD",
    "GrandCntrl Srv Rd": "GRAND CENTRAL PARKWAY SERVICE ROAD",
    "CROSS IS PKWY NB EXIT 28 B": "CROSS ISLAND PARKWAY NORTHBOUND EXIT 28B",
    "SHORE PKWY SR W": "SHORE PARKWAY SERVICE ROAD WEST",
    "CROSS IS PKY SR S": "CROSS ISLAND PARKWAY SERVICE ROAD SOUTH",
    "LITTLE NK PKWY": "LITTLE NECK PARKWAY",
    "CROSS IS PKY SR N": "CROSS ISLAND PARKWAY SERVICE ROAD NORTH",
    "CI PKWY So S": "CROSS ISLAND PARKWAY SOUTH SERVICE ROAD",
    "LAGUARDIA ACCESS RD": "LAGUARDIA AIRPORT ACCESS ROAD",
    "WHITESTONE EXPY NB": "WHITESTONE EXPRESSWAY NORTHBOUND",
    "GRAND CENTRAL PKWY SR N": "GRAND CENTRAL PARKWAY SERVICE ROAD NORTH",
    "EAST BQE WB (ON)": "EASTBOUND BROOKLYN QUEENS EXPRESSWAY ON-RAMP",
    "CROSS IS PKWY SR S": "CROSS ISLAND PARKWAY SOUTHBOUND",
    "CORP KENNDY ST": "CORPORAL KENNEDY STREET",
    "GRND CNTRL PKWY SR N": "GRAND CENTRAL PARKWAY SERVICE ROAD NORTH",
    "IN678 SR N": "INTERSTATE 678 SERVICE ROAD NORTH",
    "CI PKWY So S": "CROSS ISLAND PARKWAY SOUTH SERVICE ROAD",
    "LAGUARDIA ACCESS RD": "LAGUARDIA AIRPORT ACCESS ROAD",
    "WHITESTONE EXPY NB": "WHITESTONE EXPRESSWAY NORTHBOUND",
    "EAST BQE WB (ON)": "EASTBOUND BROOKLYN QUEENS EXPRESSWAY",
    "BX QN EXWY W": "BRONX QUEENS EXPRESSWAY WESTBOUND",
    "CROSS IS PKWY NB EXIT 28 B": "CROSS ISLAND PARKWAY NORTHBOUND EXIT 28 B",
    "SHORE PKWY SR W": "SHORE PARKWAY SERVICE ROAD WESTBOUND",
    "GRAND CNTRL PKWY SVC RD": "GRAND CENTRAL PARKWAY SERVICE ROAD",
    "HOOK CREEK BLV": "HOOK CREEK BOULEVARD",
    "METROPOLTAN AVE": "METROPOLITAN AVENUE",
    "DIVERGE GCP @ MERIDIAN": "DIVERGE GRAND CENTRAL PARKWAY AT MERIDIAN",
    "MERGE GCP & WHITESTONE EXPY": "MERGE GRAND CENTRAL PARKWAY & WHITESTONE EXPRESSWAY",
    "UNION TPK@138TH ST": "UNION TURNPIKE AT 138TH STREET",
    "HILLSIDE/BRADDOCK AVE": "HILLSIDE AVENUE & BRADDOCK AVENUE",
    "LITTLE NECK PKWY UNDER": "LITTLE NECK PARKWAY UNDERPASS",
    "RT 907A UNDER CROSS ISLAND P": "ROUTE 907A UNDER CROSS ISLAND PARKWAY",
    "RT 25 OVER QUEENS BLVD": "ROUTE 25 OVER QUEENS BOULEVARD",
    "KINGS C/L ELDERT LN": "KINGS COUNTY LINE AT ELDERT LANE",
    "I495": "INTERSTATE 495",
    "COLLEGE PT BLV": "COLLEGE POINT BOULEVARD",
    "GRAND CENTRAL PKWY SR W": "GRAND CENTRAL PARKWAY SERVICE ROAD WESTBOUND",
    "IN678 SR N": "INTERSTATE 678 SERVICE ROAD NORTH",
    "BQE RAMP": "BROOKLYN-QUEENS EXPRESSWAY RAMP",
    "VAN WYCK EXPY SR W": "VAN WYCK EXPRESSWAY SERVICE ROAD WEST",
    "LIBEROUTEY AVE": "LIBERTY AVENUE",
    "MAROUTEENSE AVE": "MARTENSE AVENUE",
    "LAGUARDIA AIRPOROUTE": "LAGUARDIA AIRPORT",
    "NEW YORK 25A NOROUTEHERN BOULEVARD": "NEW YORK 25A NORTHERN BOULEVARD",
    "INTERSTATE 495, QUEENS, NY": "INTERSTATE 495",
    "MYROUTELE AVE": "MYRTLE AVENUE",
    "NOROUTEHERN BOULEVARD": "NORTHERN BOULEVARD",
    "VAN WYCK EXPRESSWAY SERVICE RD": "VAN WYCK EXPRESSWAY SERVICE ROAD",
    "VAN WYCK EXPRESSWAY SR N": "VAN WYCK EXPRESSWAY NORTH SERVICE ROAD",
    "VAN WYCK EXPRESSWAY SR S": "VAN WYCK EXPRESSWAY SOUTH SERVICE ROAD",
    "VAN WYCK EXPY SERVICE RD": "VAN WYCK EXPRESSWAY SERVICE ROAD",
    "VAN WYCK EXPRESSWAY SERVICE ROAD NORTH": "VAN WYCK EXPRESSWAY NORTH SERVICE ROAD",
    "VAN WYCK EXPRESSWAY SERVICE ROAD SOUTH": "VAN WYCK EXPRESSWAY SOUTH SERVICE ROAD",
    "CROSS ISLAND PARKWAY SERVICE ROAD SOUTH": "CROSS ISLAND PARKWAY SERVICE ROAD SOUTH",
    "KINGS COUNTY LINE": "KINGS COUNTY LINE",
    "FRANCIS LEWIS BOULEVARDD N": "FRANCIS LEWIS BOULEVARD",
    "HOOK CREEK BOULEVARDD": "HOOK CREEK BOULEVARD",
    "VAN WYCK EXPRESSWAY SOUTH SERVICE ROAD": "VAN WYCK EXPRESSWAY SOUTH SERVICE ROAD",
    "VAN WYCK EXPRESSWAY NORTH SERVICE ROAD": "VAN WYCK EXPRESSWAY NORTH SERVICE ROAD",
    "NASSAU COUNTY BORDER, NEW YORK": "NASSAU COUNTY BORDER",
    "HOOK CREEK BOULEVARDD": "HOOK CREEK BOULEVARD",
    "FRANCIS LEWIS BOULEVARDD": "FRANCIS LEWIS BOULEVARD",
    "HOOK CREEK BOULEVARDD": "HOOK CREEK BOULEVARD",
    "COLLEGE POINT BOULEVARDD": "COLLEGE POINT BOULEVARD"
}

#Replace the bad addresses with cleaned addresses, then replace them in the DataFrame
def clean_address(address):
    for old, new in replacements.items():
        address = address.replace(old, new)
    return address

df['5'] = df['5'].apply(clean_address)
df['6'] = df['6'].apply(clean_address)

#Save the cleaned DataFrame as a new CSV file
cleaned_data_3 = 'C:\\Users\\ysj04\\Downloads\\updated3.csv' #Replace with your own file path
df.to_csv(cleaned_data_3, index=False)
