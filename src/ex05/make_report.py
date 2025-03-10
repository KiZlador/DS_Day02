from analytics import *

if __name__ == '__main__':
    a = Analytics(sys.argv[1])
    f = open(sys.argv[1], 'r')
    prob_header = f.readline()
    f.close()
    c = a.Calculations()
    has_header = (prob_header == "head,tail\n")
    data = a.file_reader(has_header)
    res = c.counts(data)
    proc = c.fractions(res)
    num_of_steps = len(data)
    res_prob = a.predict_random(num_of_steps)
    last_res = a.predict_last()
    res_prob.append(last_res)
    counts = res[0] + res[1]    
    tails = res[1]
    heads = res[0]
    prob_counts = c.counts(res_prob)
    tails_prob = proc[1]
    heads_prob = proc[0]
    counts_rand = len(res_prob)
    tails_rand = prob_counts[1]
    heads_rand = prob_counts[0]
    report = text.format(
        counts = counts,
        tails = tails,
        heads = heads,
        tails_prob = tails_prob,
        heads_prob = heads_prob,
        counts_rand = counts_rand,
        tails_rand = tails_rand,
        heads_rand = heads_rand
    )
    a.save_file(report, input("Write file name without format:"), input("Write format:"))




