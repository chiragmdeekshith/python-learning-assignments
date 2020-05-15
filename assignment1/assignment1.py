def main():
    print("\nStarting assignment 1\n")

    banks = {
        "IN": {
            "SBIN": "State Bank of India",
            "ICIC": "ICICI Bank",
            "CNRB": "Canara Bank",
            "AXIS": "Axis Bank"
        },
        "US": {
            "USBK": "United States Bank"
        }
    }

    del banks

    banks = {
        "SBIN": "State Bank of India",
        "ICIC": "ICICI Bank",
        "CNRB": "Canara Bank",
        "AXIS": "Axis Bank",
        "USBK": "United States Bank"
    }

    countries = {
        "IN": "India",
        "US": "United States of America"
    }

    locations = {
        "US": {
            "USBK": {
                    "44": "MINNEAPOLIS"
            }
        },
        "IN": {
            "ICIC": {
                "MY": "Mysore",
                "BB": "Bangalore"
            },
            "SBIN": {
                "MY": "Mysore",
                "BB": "Bangalore"
            },
            "AXIS": {
                "MY": "Mysore",
                "BB": "Bangalore"
            },
            "CNRB": {
                "MY": "Mysore",
                "BB": "Bangalore"
            }
        }
    }
    del locations

    locations = {
        "44": "MINNEAPOLIS",
        "MY": "Mysore",
        "BB": "Bangalore"
    }

    branches = {
        "US": {
            "USBK": {
                "IMT": "U.S. BANK N.A."
            }
        },
        "IN": {
            "ICIC": {
                "001": "One Branch",
                "002": "Two Branch"
            },
            "SBIN": {
                "001": "One Branch",
                "002": "Two Branch"
            },
            "AXIS": {
                "001": "One Branch",
                "002": "Two Branch"
            },
            "CNRB": {
                "001": "One Branch",
                "002": "Two Branch"
            }
        }
    }

    del branches

    branches = {
        "001": "One Branch",
        "002": "Two Branch",
        "IMT": "U.S. BANK N.A."
    }

    print("Enter bank's SWIFT code:- ")
    swift_code = input()
    swift_code = swift_code.upper()

    if len(swift_code) != 11:
        print("Invalid code. Please enter valid 11 character Swift code")
        return -1

    bank = swift_code[0:4]
    country = swift_code[4:6]
    location = swift_code[6:8]
    branch = swift_code[8:11]

    print("\nThese are the fetched bank details:-")
    print("Bank name:- ", bank, " : ", banks[bank])
    print("Bank country:- ", country, " : ", countries[country])
    print("Bank location:- ", location, " : ", locations[location])
    print("Bank branch:- ", branch, " : ", branches[branch])

    del(bank, banks, country, countries, location, locations, branch, branches)
