
from collections import Counter


content = []
file = open("job_desc.txt","r")
while True:
	temp=file.readline()
	if not temp:
		break
	content.append(temp)
file.close()
job_description = content




words = content

    # Join the words in the specified format
formatted_words = ', '.join(words).replace('\n', '')

# Print the formatted words
print(formatted_words)


# Open the output file in write mode
with open('output.txt', 'a') as output_file:
    # Append the formatted words to the output file
    output_file.write(formatted_words + '\n')

print(f"Formatted words have been written to 'output.txt'")