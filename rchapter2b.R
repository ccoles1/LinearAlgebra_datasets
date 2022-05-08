require(matrixcalc)#install this package
#install.packages('janeaustenr')
#install.packages('dplyr')
#install.packages('tidytext')
#install.packages('text2vec')
#install.packages('HMM')

library(text2vec)
library(janeaustenr)
library(dplyr)
library(stringr)
library(tidytext)
library(tidyr)
library(HMM)
wordlist <-c("miss","anne","poor","marianne","when","replied","with","felt","jane","appeared","cried","but")
original_books <- austen_books() %>%
  group_by(book) %>%
  mutate(linenumber = row_number(),
         chapter = cumsum(str_detect(text, regex("^chapter [\\divxlc]",
                                                 ignore_case = TRUE)))) %>%
  ungroup()

original_books
tidy_books <- original_books %>%
  unnest_tokens(word, text)
tidy_books
data(stop_words)

tidy_books <- tidy_books %>%
  anti_join(stop_words)

tidy_books %>%
  count(word, sort = TRUE) 
austen_bigrams <- austen_books() %>%
  unnest_tokens(bigram, text, token = "ngrams", n = 2)
austen_bigrams %>%
  count(bigram, sort = TRUE)
bigrams_separated <- austen_bigrams %>%
  separate(bigram, c("word1", "word2"), sep = " ")

bigrams_filtered <- bigrams_separated %>%
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word)

# new bigram counts:
bigram_counts <- bigrams_filtered %>% 
  count(word1, word2, sort = TRUE)
word_filtered <- bigrams_separated %>%
  filter(word1 %in% wordlist) %>%
  filter(word2 %in% wordlist)
word_counts <-word_filtered%>% 
  count(word1, word2, sort = TRUE)
T<-matrix(0,length(wordlist),length(wordlist))
for (j in 1:length(wordlist))
{
oneword<-word_filtered  %>%
  filter(word1 == wordlist[j])
onewordcount<-oneword%>% 
  count(word1, word2, sort = TRUE)
for(i in 1:nrow(onewordcount)){
  T[j,match(onewordcount[i,2],wordlist)]<-as.numeric(onewordcount[i,3])/as.numeric(sum(onewordcount[3]))
}}
initial<-matrix(0,length(wordlist))
initialword<-"marianne"
sentence<-initialword
initial[match(initialword,wordlist)]<-1
for (i in 1:4)
{
sentence<-append(sentence,wordlist[match(max(matrix.power(T,i)%*%initial),matrix.power(T,i)%*%initial)])
} 
print(sentence)
#autocorrect part of case study
# Initialise HMM
transProbs<-matrix(c(.1,.29,.33,.21,.17,.18,.40,.36,.28,.21,.27,.29,.45,.32,0,.14),4)
emissionProbs<-transProbs
hmm<-initHMM(c("A","E","L","R"), c("A","E","L","R"), startProbs=c(3/4,1/8,0,1/8),transProbs,emissionProbs=transProbs)
print(hmm)
# Sequence of observations
observations = c("A","E","R")
# Calculate Viterbi path
viterbi = viterbi(hmm,observations)
print(viterbi)

#writes the entire bigram for future use
write.csv(bigram_counts, "C:/Users/ccoles/Dropbox/linear_databook/stockmarket/bigram.csv")
