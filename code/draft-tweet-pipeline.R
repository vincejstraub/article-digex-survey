## packages ----
pkgs <- c("tidyverse", "academictwitteR", "tweetbotornot", "vader")

for (p in pkgs){
  if(!require(p, character.only = TRUE)){
    install.packages(p)
    library(p, character.only = TRUE)
  }
}
rm(p, pkgs)

## [this is arbitrary - we'd get usernames through ads] get historial tweets from of wwg1wga tweeters ----
token <- "<INSERT BEARER TOKEN FOR TWITTER V2 ACADEMIC API>"
tweeters <- get_all_tweets(query = "WWG1WGA", 
                           start_tweets = "2021-06-15T00:00:00Z",
                           end_tweets = "2021-06-22T00:00:00Z",
                           bearer_token = token,
                           bind_tweets = T,
                           lang = "en")

# make vector of ids
user_ids <- tweeters$author_id

# get users' profile-level data from numeric ids
user_profs <- get_user_profile(x = user_ids,
                               bearer_token = token)
# make vector of usernames
usernames <- user_profs$username

# sample 100 for exploratory purposes
usernames <- sample(usernames, 10)

# get the users' tweets from the past month
tweets <- get_user_tweets(users = usernames,
                         start_tweets = "2021-06-08T00:00:00Z",
                         end_tweets = "2021-06-22T00:00:00Z",
                         bearer_token = token,
                         bind_tweets = T)

# loop through tweets and get expanded urls
urls <- data.frame(author_id = NA, expanded_url = NA) # empty df to store data
all_url_data <- tweets$entities$urls # nested list of url related data from tweets
ids <- tweets$author_id
for (i in 1:nrow(tweets)) {
  
  # make df with url data
  x <- as.data.frame(all_url_data[i])
  
  # if no url in tweet, then put NA, otherwise grab expanded url
  if(nrow(x) < 1){
    urls <- rbind(urls, c(ids[i], NA))
  } else {
    urls <- rbind(urls, c(ids[i], x$expanded_url))
  }
}
rm(x)

# remove empty row
urls <- urls[-1, ]

## see if users have tweeted "iffy" links ----

# read in iffy news data: https://iffy.news/index/ 
iffynews <- read.csv("iffynews_data_22June2021.csv")

# create vector of iffy urls
iffy_urls <- as.character(iffynews$Domain)
names(iffy_urls) <- iffy_urls

# create booleans showing if iffy url is detected
## NOTE: THIS DOES NOT MATCH CASE 
## (e.g., "csglobal.com" will be detected in "statisticsglobal.com")
temp <- iffy_urls %>%
  map_dfc(~ str_detect(urls$expanded_url, .x)) %>%
  add_column(expanded_url = urls$expanded_url) 

# tally up number of iffy urls present in each tweet, and tidy up the df
user_iffyness <- cbind(urls$author_id, temp)
names(user_iffyness)[1] <- c("author_id")
user_iffyness <- user_iffyness[ ,-492] # removes expanded_url column
user_iffyness$n_iffy <- rowSums(user_iffyness[ ,c(2:491)])
rm(temp)

# tally up number of iffy urls tweeted by each user
user_iffyness <- user_iffyness %>%
  group_by(author_id) %>%
  summarise(sum_iffy = sum(n_iffy, na.rm = T))


## get VADER sentiment scores for each tweet ----
vader_scores <- vader_df(tweets$text, rm_qm = T)

# make col with author_id for each tweet's vader score
vader_scores$author_id <- tweets$author_id

## get user bot scores ----

bot_scores <- tweetbotornot(usernames)
names(bot_scores) <- c("username", "author_id", "prob_bot")

## bind together user-level metrics ----

# join user metrics: average sentiment, number of tweets, bot prob, iffyness 
user_metrics <- vader_scores %>%
  group_by(author_id) %>%
  summarise(m_vader_compound = mean(compound),
            n_tweets = n())

# bind together user metrics (iffyness + sentiment)
user_metrics <- inner_join(user_metrics, user_iffyness, by = "author_id")
user_metrics <- inner_join(user_metrics, bot_scores, by = "author_id")

