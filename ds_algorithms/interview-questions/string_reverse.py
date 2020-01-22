def reverse(string):
    response = ""
    for index in range((len(string) - 1), -1, -1):
        response += string[index]
    return response


response = reverse("Hello World!")
print(response)
