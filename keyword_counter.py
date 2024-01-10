from collections import Counter

file = open("output.txt","r")
content = []
while True:
    temp=file.readline()
    if not temp:
        break
    else:
        s = temp.split(', ')
        content = content+ s
        content[-1] = content[-1].replace('\n','')
    
file.close()
# Example job description

job_description = content

words = content
print(words)
file.close()
count = Counter(words)
lis = count.most_common()
for_words = []

for i in lis:
    for_words.append(i[0])
formatted_words = ', '.join(for_words)
with open('final.txt', 'w') as output_file:
    # Append the formatted words to the output file
    output_file.write(formatted_words )

print(f"Formatted words have been written to 'output.txt'")