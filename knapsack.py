def fractional_knapsack_brute_force(values, weights, capacity):
  n = len(values)
  max_value = 0
  best_fractions = [0] * n

  def explore(i, current_weight, current_value, fractions):
    nonlocal max_value, best_fractions
    if i == n:
      if current_weight <= capacity and current_value > max_value:
        max_value = current_value
        best_fractions = fractions.copy()
      return

    if current_weight + weights[i] <= capacity:
      new_fraction = (capacity - current_weight) / weights[i]
      explore(i + 1, current_weight + weights[i], current_value + values[i] * new_fraction, fractions + [new_fraction])

    explore(i + 1, current_weight, current_value, fractions + [0])

  explore(0, 0, 0, [])
  return max_value, best_fractions

def fractionalKnapsack(values, weights, capacity):
  value_to_weight_ratios = [value / weight for value, weight in zip(values, weights)]

  sorted_items = sorted(zip(value_to_weight_ratios, values, weights), reverse=True)

  current_weight = 0
  max_value = 0
  fractions = [0] * len(values)

  for a, value, weight in sorted_items:
    if current_weight + weight <= capacity:
      current_weight += weight
      max_value += value
      fractions[values.index(value)] = 1
    else:
      fraction = (capacity - current_weight) / weight
      current_weight += weight * fraction
      max_value += value * fraction
      fractions[values.index(value)] = fraction
      break 

  return max_value, fractions
 

def knapsack_01_brute_force(values, weights, capacity):

  n = len(values)
  max_value = 0
  best_items = [0] * n

  def explore(i, current_weight, current_value, items):
    nonlocal max_value, best_items
    if i == n:
      if current_weight <= capacity and current_value > max_value:
        max_value = current_value
        best_items = items.copy()
      return

    if current_weight + weights[i] <= capacity:
      explore(i + 1, current_weight + weights[i], current_value + values[i], items + [1])

    explore(i + 1, current_weight, current_value, items + [0])

  explore(0, 0, 0, [])
  return max_value, best_items

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value_frac, fractions = fractionalKnapsack(values, weights, capacity)
print("Fractional Knapsack:")
print(f"Maximum value: {max_value_frac:.2f}")
print(f"Fractions of items included: {fractions}")

max_value_01, items_included = knapsack_01_brute_force(values, weights, capacity)
print("\n0/1 Knapsack:")
print(f"Maximum value: {max_value_01}")
print(f"Items included: {items_included}")