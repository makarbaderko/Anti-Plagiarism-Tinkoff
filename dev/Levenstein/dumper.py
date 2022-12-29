import os
import ast
files_pths = os.listdir("../data/original/files")
plagiat1_pths = os.listdir("../data/original/plagiat1")
plagiat2_pths = os.listdir("../data/original/plagiat2")
skipped_pths = []
# Files
for path in files_pths:
	with open(f"../data/original/files/{path}", "r") as old:
		source = old.read()
	with open(f"../data/dumps/files/{path}", "w") as new:
		try:
			parse = ast.parse(source)
			dump = ast.dump(parse)
			new.write(dump)
		except SyntaxError:
			print("Syntax Error in " + f"original/files/{path}")
			skipped_pths.append(path)
# Plagiat 1
for path in plagiat1_pths:
	with open(f"../data/original/plagiat1/{path}", "r") as old:
		source = old.read()
	with open(f"../data/dumps/plagiat1/{path}", "w") as new:
		try:
			parse = ast.parse(source)
			dump = ast.dump(parse)
			new.write(dump)
		except SyntaxError:
			print("Syntax Error in " + f"original/plagiat1/{path}")
			skipped_pths.append(path)
# Plagiat 2
for path in plagiat2_pths:
	with open(f"../data/original/plagiat2/{path}", "r") as old:
		source = old.read()
	with open(f"../data/dumps/plagiat2/{path}", "w") as new:
		try:
			parse = ast.parse(source)
			dump = ast.dump(parse)
			new.write(dump)
		except SyntaxError:
			print("Syntax Error in " + f"original/plagiat2/{path}")
			skipped_pths.append(path)
print(f"Total Skips {len(set(skipped_pths))}, this is {(len(set(skipped_pths)) / len(files_pths)) * 100}% of the whole dataset")