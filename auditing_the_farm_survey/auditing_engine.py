"""
Maji Ndogo Farm Survey Auditing Engine
======================================
Core algorithmic implementations for high-throughput farm auditing,
logarithmic field searches, recursive yield sorting, and functional data transforms.

ALX Data Science Program - Python II: Module 1
Author: Yonatan (YonInsights)
"""

from typing import List, Dict, Any, Optional


def linear_search_field(field_list: List[Dict[str, Any]], target_id: int) -> Optional[float]:
    """
    Sequentially search for a field by Field_ID across unsorted records.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Returns:
        Pollution_level (float) of the first matching field, or None if not found.
    """
    for record in field_list:
        if record['Field_ID'] == target_id:
            return record['Pollution_level']
    return None


def binary_search_yield(sorted_field_list: List[Dict[str, Any]], target_id: int) -> Optional[float]:
    """
    Logarithmically search for a field by Field_ID in an ascending sorted list.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Returns:
        Annual_yield (float) of the matching field, or None if not found.
    """
    low = 0
    high = len(sorted_field_list) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_id = sorted_field_list[mid]['Field_ID']
        if mid_id == target_id:
            return sorted_field_list[mid]['Annual_yield']
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None


def merge_sort_yields(field_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Recursively sort field records into descending order of Annual_yield.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Returns:
        New list of dictionaries sorted by Annual_yield descending.
    """
    if len(field_list) <= 1:
        return field_list
    mid = len(field_list) // 2
    left = merge_sort_yields(field_list[:mid])
    right = merge_sort_yields(field_list[mid:])
    return merge(left, right)


def merge(left: List[Dict[str, Any]], right: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Helper function to merge two sorted lists in descending order of Annual_yield.
    """
    sorted_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i]['Annual_yield'] >= right[j]['Annual_yield']:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


def identify_high_pollution(field_list: List[Dict[str, Any]], threshold: float) -> List[Dict[str, Any]]:
    """
    Filter field records with Pollution_level strictly greater than threshold.
    
    Time Complexity: O(n)
    Space Complexity: O(k) where k <= n
    
    Returns:
        Filtered list of high-pollution field records.
    """
    return list(filter(lambda record: record['Pollution_level'] > threshold, field_list))


def project_harvests(field_list: List[Dict[str, Any]]) -> List[float]:
    """
    Project total harvest (Plot_size * Standard_yield) rounded to 2 decimal places.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Returns:
        List of projected harvest floats.
    """
    return list(map(lambda record: round(record['Plot_size'] * record['Standard_yield'], 2), field_list))


if __name__ == '__main__':
    # 5-record sample benchmark
    sample = [
        {'Field_ID': 40734, 'Pollution_level': 0.0853, 'Plot_size': 1.3, 'Crop_type': 'cassava', 'Annual_yield': 0.7514, 'Standard_yield': 0.578},
        {'Field_ID': 30629, 'Pollution_level': 0.3997, 'Plot_size': 2.2, 'Crop_type': 'cassava', 'Annual_yield': 1.0699, 'Standard_yield': 0.4863},
        {'Field_ID': 39924, 'Pollution_level': 0.358, 'Plot_size': 3.4, 'Crop_type': 'tea', 'Annual_yield': 2.2088, 'Standard_yield': 0.6496},
        {'Field_ID': 5754, 'Pollution_level': 0.2867, 'Plot_size': 2.4, 'Crop_type': 'cassava', 'Annual_yield': 1.2776, 'Standard_yield': 0.5323},
        {'Field_ID': 14146, 'Pollution_level': 0.0432, 'Plot_size': 1.5, 'Crop_type': 'wheat', 'Annual_yield': 0.8326, 'Standard_yield': 0.5551}
    ]

    print("=== Maji Ndogo Auditing Engine Verification ===")
    
    # 1. Linear Search
    p1 = linear_search_field(sample, 39924)
    print(f"[1] Linear Search (ID 39924): {p1} (Expected: 0.358)")
    
    # 2. Binary Search
    sorted_sample = sorted(sample, key=lambda f: f['Field_ID'])
    y1 = binary_search_yield(sorted_sample, 30629)
    print(f"[2] Binary Search (ID 30629): {y1} (Expected: 1.0699)")
    
    # 3. Merge Sort
    sorted_yields = merge_sort_yields(sample)
    top_yields = [f['Annual_yield'] for f in sorted_yields[:3]]
    print(f"[3] Merge Sort Top 3 Yields: {top_yields} (Expected: [2.2088, 1.2776, 1.0699])")
    
    # 4. Filter Pollution
    polluted = identify_high_pollution(sample, 0.3)
    polluted_ids = [f['Field_ID'] for f in polluted]
    print(f"[4] High Pollution (>0.3): Field IDs {polluted_ids} (Expected: [30629, 39924])")
    
    # 5. Project Harvests
    harvests = project_harvests(sample)
    print(f"[5] Projected Harvests: {harvests} (Expected: [0.75, 1.07, 2.21, 1.28, 0.83])")
    
    print("\n[OK] All auditing engine modules executed successfully.")
