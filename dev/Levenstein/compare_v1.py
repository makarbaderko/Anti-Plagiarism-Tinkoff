import argparse
from helper import flatten, dump, levenshtein
parser = argparse.ArgumentParser(description='Levenstein Distance Code Plagiarism Comparison')
parser.add_argument('input_pth', type=str, help='path to input file (txt)')
parser.add_argument('output_pth', type=str, help='path to output file (txt)')
args = parser.parse_args()
with open(args.input_pth, 'r') as file:
	input_data = [item.split(" ")[:2] for item in file.readlines()]
unique_pths = list(set(flatten(input_data)))
for path in unique_pths:
	dump(f"../data/original/{path}", f"../data/cache/{path.replace('/','-')[:-3]}_dump.txt")
scores = []
print(input_data)
for pair in input_data:
	with open(f"../data/cache/{pair[0].replace('/','-')[:-3]}_dump.txt", "r") as f:
		file1 = f.read()
	with open(f"../data/cache/{pair[1].replace('/','-')[:-3]}_dump.txt", "r") as f:
		file2 = f.read()
	try:
		score = 1 / (levenshtein(file1, file2) / len(file1))
	except ZeroDivisionError:
		score = 1
	print(score)