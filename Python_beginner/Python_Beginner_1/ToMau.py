data = input().split(" ")
data = [int(x) for x in data]
h, w, k = data[0], data[1], data[2]

data = []
for i in range(h):
  chars = input()
  for char in chars:
    data.append(char) 

paper = []
for i in range(0,len(data), w):
    paper.append(data[i:w+i])

def count_black_square(paper, h, w):
  num_black_square = 0
  for i in range(h):
    for j in range(w):
      if paper[i][j] == '#':
        num_black_square += 1
  return num_black_square

def get_all_subsets(n):
  all_subsets = []

  for i in range(1 << n):
    subset = [j for j in range(n) if (i & (1 << j)) > 0]
    all_subsets.append(subset)
  
  return all_subsets

def count_ways_to_paint(paper, h, w, k):
  num_ways = 0

  if count_black_square(paper, h, w) < k:
    return 0

  row_subsets = get_all_subsets(h)
  col_subsets = get_all_subsets(w)

  for selected_row in row_subsets:
    for selected_col in col_subsets:
      black_cells = 0

      for i in range(h):
        for j in range(w):
          if (i not in selected_row) and (j not in selected_col):
            if paper[i][j] == '#':
              black_cells += 1

      if black_cells == k:
          num_ways += 1

  return num_ways
result = count_ways_to_paint(paper, h, w, k)
print(result)