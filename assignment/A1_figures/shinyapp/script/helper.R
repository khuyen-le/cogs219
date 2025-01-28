library("readxl")
library("tidyverse")

rep4yo <- read_excel("data/Disjunction_Data.xlsx", sheet = "Replication 4yos") %>%
  mutate(expt = "Replication", 
         age_years = 4, 
         Months = as.numeric(Months))
rep5yo <- read_excel("data/Disjunction_Data.xlsx", sheet = "Replication 5yos") %>%
  mutate(expt = "Replication", 
         age_years = 5)

rep <- bind_rows(rep4yo, rep5yo)

threealt4yo <- read_excel("data/Disjunction_Data.xlsx", sheet = "3 Objects 4yos") %>%
  mutate(expt = "Three Alternatives", 
         age_years = 4, 
         `Adult Response?` = as.numeric(`Adult Response?`), 
         Months = as.numeric(Months))
threealt5yo <- read_excel("data/Disjunction_Data.xlsx", sheet = "3 Objects 5yos") %>%
  mutate(expt = "Three Alternatives", 
         age_years = 5, 
         Months = as.numeric(Months))

threealt <- bind_rows(threealt4yo, threealt5yo)

data <- bind_rows(rep, threealt) %>%
  filter(!is.na(`Subject ID`)) %>%
  mutate(response_yes = case_when(
    `Response (Y/N)` == "N" ~ 0, 
    `Response (Y/N)` == "Y" ~ 1, 
    .default = 0)) # default = 0
