# second -> first	second_income / 100 * 15
# first -> boss	(recieved + first_income) / 100 * 15
# boss recieved + boss_income

# build the tree
# 	record income for every child
# 	record child under parent
# find boss(with no distributor)


def	main():
	n = int(input().strip())
	income_map = {}
	children_map = {}

	for _ in range(n):
		id, parent_id, income = map(int, input().strip().split)
		income_map[id] = income
		if parent_id not in children_map:
			children_map[parent_id] = []
		children_map[parent_id].append(id)


if __name__ == "__main__":
    main()
