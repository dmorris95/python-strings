#Task 1

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def keyword_highlight(revi):
    for r in revi:
        lower_r = r.lower()
        if lower_r.find("good") != -1:
            print(r.replace("good", "GOOD"))
        elif lower_r.find("excellent") != -1:
            print(r.replace("excellent", "EXCELLENT"))
        elif lower_r.find("bad") != -1:
            print(r.replace("bad", "BAD"))
        elif lower_r.find("poor") != -1:
            #adding extra replace statements can account for the first letter being capitalized without dismantling the entire string
            print(r.replace("Poor", "POOR"))
        elif lower_r.find("average") != -1:
            print(r.replace("average", "AVERAGE"))
        else:
            print(r)

keyword_highlight(reviews)


#Task 2

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def pos_neg_count(pos_words, neg_words, review):
    for r in review:
        low_r = r.lower()
        p_count = 0
        n_count = 0
        for p in pos_words:
            if low_r.find(p) != -1:
                p_count += low_r.count(p)
        for n in neg_words:
            if low_r.find(n) != -1:
                n_count += low_r.count(n)
        print(f"The review has {p_count} positive words and {n_count} negative words.")

pos_neg_count(positive_words, negative_words, reviews)     



#Task 3

def review_summary(review):
    for r in review:
        c = 30
        sum_slice = r[:c]
        while sum_slice.endswith(" ") != True:
            c += 1
            sum_slice = r[:c]
        print(sum_slice[:c-1] + "...")

review_summary(reviews)
