import cohere

co = cohere.ClientV2("W6jMlPJCOXkjsh1R71fayjnNrSyKEexCtjoyEXHT")
response = co.chat(
    model="command-r-plus",
    messages=[{"role": "user", "content": "solutions for digitising transport in the UK"}]
)

print(response)
