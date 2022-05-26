# This script can distinguish between normal words and basic plural words.
# If the word ends in s, it will detect it as plural. If it doesn't, it will detect it as singular
print("Please type in a word: ")
wordInput = string(input())
suffix = "s"


def detect_plurality():
	if wordInput.endswith(suffix):
		isPlural = wordInput + " is a plural word."
		return isPlural 
	else:
		notPlural = wordInput + " is not a plural word."
		return notPlural


print(detect_plurality())
