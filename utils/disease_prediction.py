import openai
openai.api_key = "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"


def make_openapi_call(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048
    )
    result=response["choices"][0]["text"]
    print(result)
    return result

symptoms = ["cough", "cold", "running nose", "shortness of breath"]
diseases=make_openapi_call(f"List as points without explanation the top 2 names of disease that is likely given the following symptoms  : {', '.join(symptoms)}")
print("dwew",diseases)
medicine=''

for disease in diseases.split("\n"):
    print("dd",disease)
    medicine+=make_openapi_call(f"What are the  medication for {disease}")
