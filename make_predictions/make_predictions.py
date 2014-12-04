import sys, csv, math
""" Calculate prediction based on global effects
    Input: Validation set, global effects set
    Output: movie, user, probability the pair exists in 2006 """
# Load movie averages
movie_dic = {}
with open('movie_averages.txt', "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter = '\t')
    for row in reader:
        movie_avg = float(row[1])
        movie_dic[row[0]] = movie_avg
# Load user averages
user_dic = {}
with open('user_averages.txt', "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter = '\t')
    for row in reader:
        user_avg = float(row[1])
        user_dic[row[0]] = user_avg
# Load movie time coefficients
movie_time_dic = {}
with open('movie_coefficients.txt', "rb") as csvfile:
    alpha = 1
    reader = csv.reader(csvfile, delimiter = '\t')
    for row in reader:
        theta = float(row[1])
        N = int(row[2])
        movie_time_dic[row[0]] = (theta*N)/float(N+alpha)
# Load user time coefficients
user_time_dic = {}
with open('user_coefficients.txt', "rb") as csvfile:
    alpha = 1
    reader = csv.reader(csvfile, delimiter = '\t')
    for row in reader:
        theta = float(row[1])
        N = int(row[2])
        user_time_dic[row[0]] = (theta*N)/float(N+alpha)

def make_prediction(user, movie):
    population_rate = (100480507/float(480189*17750))
    if user not in user_dic:
        user_adjusted_rate = 0
        user_time_adjusted_rate = 0
    else:
        user_adjusted_rate = user_dic[user]
        user_time_adjusted_rate = user_time_dic[user]
    if movie not in movie_dic:
        movie_adjusted_rate = 0
        movie_time_adjusted_rate = 0
    else:
        movie_adjusted_rate = movie_dic[movie]
        movie_time_adjusted_rate = movie_time_dic[movie]
    # prediction can be changed to include or exclude user/movie rates
    prediction = (population_rate + user_adjusted_rate + movie_adjusted_rate +
        user_time_adjusted_rate + movie_time_adjusted_rate)
    if prediction < 0:
        prediction = 0
    return prediction
# global_effects is generated from the baseline/movie_total and user_total code
RMSE = 0
count = 0
for line in sys.stdin:
    user, movie, answer = line.strip().split(',', 2)
    prediction = make_prediction(user, movie)
    if int(answer) > 0:
        answer = 1
    RMSE += (int(answer) - prediction)**2
    count += 1
    print '%s\t%s\t%s\t%s' % (user, movie, answer, prediction)
print math.sqrt(RMSE/float(count))
