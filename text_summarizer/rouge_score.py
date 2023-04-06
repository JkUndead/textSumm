from rouge_score import rouge_scorer

def cal_Rouge_1(prompt,result):
    scorer = rouge_scorer.RougeScorer(['rouge1'], use_stemmer=True)
    score = scorer.score(prompt,result)
    return score

def cal_Rouge_2(prompt,result):
    scorer = rouge_scorer.RougeScorer(['rouge2'], use_stemmer=True)
    scores = scorer.score(prompt,result)
    return scores

def cal_Rouge_L(prompt,result):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    scores = scorer.score(prompt,result)
    return scores