def gc_content(sequence: str) -> float:
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total_length = len(sequence)
    if total_length == 0:
        return 0.0
    gc_percentage = ((g_count + c_count) / total_length) * 100
    return gc_percentage