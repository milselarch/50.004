
def segment_generator(num_segments, total):
    # print('ENTRY', num_segments, total)
    if num_segments > total:
        return []
    if num_segments == 0:
        return []
    if total == 0:
        return []

    if num_segments == 1:
        return [[total]]

    all_segments = []
    for k in range(1, total - num_segments + 1):
        start_segment = [k]
        sub_segments = segment_generator(num_segments - 1, total - k)

        for sub_segment in sub_segments:
            all_segments.append(start_segment + sub_segment)

    # print("RETURNING", all_segments)
    return all_segments

