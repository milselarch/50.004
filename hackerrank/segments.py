from enum import Enum, auto


class STACK_VARS(Enum):
    k = auto()
    all_segments = auto()
    num_segments = auto()
    total = auto()


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


def segment_generate_defaults(num_segments, total):
    # print('ENTRY', num_segments, total)
    if num_segments > total:
        return []
    if (num_segments == 0) or (total == 0):
        return []
    if num_segments == 1:
        return [[total]]

    return False


def get_stack_segments(stack):
    segment_lengths = []
    for stack_frame in stack:
        segment_length = stack_frame[STACK_VARS.k]
        segment_lengths.append(segment_length)
        return segment_lengths


def segment_generator_iterative(
    num_segments, total
):
    segments = segment_generate_defaults(num_segments, total)
    if segments is not False:
        return segments

    stack = [{
        STACK_VARS.k: 0,
        STACK_VARS.total: total,
        STACK_VARS.num_segments: num_segments
    }]

    while len(stack) > 0:
        stack_frame = stack[-1]

        k = stack_frame[STACK_VARS.k]
        total = stack_frame[STACK_VARS.total]
        num_segments = stack_frame[STACK_VARS.num_segments]
        k += 1

        if num_segments > total:
            # TODO: print stack frame chain
            stack.pop()
            yield get_stack_segments(stack)
            continue
        elif (num_segments == 0) or (total == 0):
            stack.pop()
            yield get_stack_segments(stack)
            continue
        elif num_segments == 1:
            stack_frame = {
                STACK_VARS.k: -1,
                STACK_VARS.total: total,
                STACK_VARS.num_segments: 0
            }

            stack.append(stack_frame)
            continue

    """
    all_segments = []
    for k in range(1, total - num_segments + 1):
        start_segment = [k]
        sub_segments = segment_generator(num_segments - 1, total - k)

        for sub_segment in sub_segments:
            all_segments.append(start_segment + sub_segment)

    # print("RETURNING", all_segments)
    return all_segments
    """


def findMaxSubsegmentsCount(arr):
    # Write your code here
    segments = 1
    max_length = 0
    sorted_arr = sorted(arr)

    for k in range(1, len(arr)):
        segment_combinations = segment_generator(k, len(arr))
        has_valid_segment = False

        for segment_lengths in segment_combinations:
            valid_combi = True
            index = 0

            for length in segment_lengths:
                segment = arr[index:index + length]
                min_seg, max_seg = min(segment), max(segment)

                if not((min_seg == sorted_arr[index]) and (max_seg == sorted_arr[index + length -1 ])):
                    # print('BAD SEGMENT', segment, arr)
                    valid_combi = False
                    break

                index += length

            if not valid_combi:
                continue

            # print('VALID SEGMENT')
            has_valid_segment = True
            break

        if not has_valid_segment:
            break

        max_length = k

    return max_length


print(segment_generator(3, 5))
print(segment_generator(1, 5))
print(findMaxSubsegmentsCount([2, 5, 1, 9, 7, 6]))