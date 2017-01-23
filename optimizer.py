def optimize(f, parameter_ranges, buckets=6, retries=4):
    n = len(parameter_ranges)
    begins = [p for (p, e) in parameter_ranges]
    steps = [(e-p)/(buckets - 1) for (p, e) in parameter_ranges]
    minres = 10**90
    wh = None
    whr = None
    for i in range(buckets**n):
        tmp = i
        vec = []
        converted_vec = []
        for j in range(n):
            pos = tmp % buckets
            vec.append(pos)
            converted_vec.append(begins[j] + pos*steps[j])
            tmp /= buckets
        res = f(converted_vec)
        if res < minres:
            minres = res
            wh = vec
            whr = converted_vec
    if retries == 0:
        return whr, minres
    new_ranges = []
    for i in range(n):
        val = begins[i] + wh[i] * steps[i]
        beg = val - steps[i] if i > 0 else val
        end = val + steps[i] if i < n - 1 else val
        new_ranges.append((beg, end))
    return optimize(f, parameter_ranges, buckets, retries-1)




