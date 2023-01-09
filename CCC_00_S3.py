n = int(input())
links = []
for i in range(n):
	web_code = input()
	html_code = ""
	html = ""
	while html != "</HTML>":
		html = input()
		html_code += html
	links.append(html_code)

print(links)

