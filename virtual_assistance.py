import wolframalpha

input = raw_input("Questions:")

app_id = "EX9LTQ-TG2EXHQURT"

client = wolframalpha.Client(app_id)

res = client.query(input)
answer= next(res.results).text

print answer




                  
