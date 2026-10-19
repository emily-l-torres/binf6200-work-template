import collections

entry_ids = ["104L", "104L", "101M", "4HHB", "4HHB", "4HHB", "4HHB"] 
 
counts = collections.Counter(entry_ids)
for entry_id, chains in counts.most_common(1):
    print(f"{entry_id}: {chains}")
print(counts["4HHB"])