
class Phrasing():
  def count_items(list_of_items):
    dict_items_counts = {}
    for item in list_of_items:
      if item not in dict_items_counts.keys():
        dict_items_counts[item] = 0
      
      dict_items_counts[item] += 1

    summary_items = []
    for item, count in dict_items_counts.items():
      summary_items.append(f"{count} {item}{'s' if count != 1 else ''}")

    return ', '.join(summary_items)

