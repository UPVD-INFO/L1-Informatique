setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
library(tidyverse)

# Exercice 6.1 ----
# Q.6.1.1
m = 0.2
alpha = 0.004
p_0 = 10

# Q 6.1.2
evolution <- function(actuel, b){
  return(floor((1 + b - m - alpha * actuel) * actuel ))
  }

# Q 6.1.3
# Avec une boucle pour
bacterie <- numeric(12)
bacterie[1] <- p_0
for (jour in 1:12){
  bacterie[jour+1] = evolution(bacterie[jour], 1.51)
  }
# Puis la création du tibble
donnee <- tibble(jour = 0:12,
                    b = rep(1.51, 13),
                    bacterie)

# En programmation fonctionnelle
donnee <- tibble(jour = 0:12) %>%
  mutate(b = 1.51) %>%
  mutate(bacterie = accumulate(.x = b[-1],
                                  .f = evolution,
                                  .init = p_0))

# Q 6.1.4
ggplot(data = donnee) +
  aes(x = jour,
         y = bacterie) +
  geom_point() +
  geom_line(linetype = "dashed")
# Exercice 6.2 ----
m = 0.2
alpha = 0.004
p_0 = 10

evolution <- function(actuel, b){
  return(floor((1 + b - m - alpha * actuel) * actuel ))
  }

# Avec une boucle pour
donnee_plot <- tibble()
for (b in c(1.51, 2.5, 3)){
  bacterie <- numeric(20)
  bacterie[1] <- p_0
  for (jour in 1:20){
    bacterie[jour+1] = evolution(bacterie[jour], b)
    }
  donnee <- tibble(jour = 0:20,
                      bacterie) %>%
    mutate(b = b)
  donnee_plot <- bind_rows(donnee_plot, donnee)
  }
donnee_plot <- mutate(donnee_plot, b = factor(b))

# En programmation fonctionnelle
donnee_plot <- tibble(jour = 0:21) %>%
  expand(jour, b = c(1.51, 2.5, 3.0)) %>%
  group_by(b) %>%
  mutate(bacterie = accumulate(.x = b[-1],
                                  .f = evolution,
                                  .init = p_0)) %>%
  mutate(b = factor(b))

ggplot(data = donnee_plot) +
  aes(x = jour,
         y = bacterie,
         color = b) +
  geom_point() +
  geom_line()
ggsave("factor_1.png")

ggplot(data = donnee_plot) +
  aes(x = jour,
         y = bacterie,
         linetype = b,
         color = b) +
  geom_point() +
  geom_line()
ggsave("factor_2.png")
# Exercice 6.3 ----
# Q 6.3.1
b <- 3
m <- 0.2
alpha <- 0.004
p_0 <- 10

evolution <- function(actuel, b){
  return(floor((1 + b - m - alpha * actuel) * actuel ))
  }

donnee <- tibble(jour = 0:11) %>%
  mutate(b = 3) %>%
  mutate(bacterie = accumulate(.x = b[-1],
                                  .f = evolution,
                                  .init = p_0))

# Q 6.3.2
donnee_decale <- donnee %>%
  mutate(suivant = lead(bacterie)) %>%
  rename(actuel = bacterie)

# Q 6.3.3
donnee_bissectrice <- donnee_decale %>%
  mutate(actuel = suivant)

# Q 6.3.4
donnee_application <- bind_rows(donnee_decale, donnee_bissectrice) %>%
  arrange(jour) %>%
  drop_na() %>%
  mutate(etape = case_when(actuel != suivant ~ jour))

# Q 6.1.3
ggplot(data = donnee_application) +
  aes(x = actuel,
         y = suivant,
         label = etape) +
  geom_path(size = 0.5, linetype = "dashed") +
  geom_function(fun = ~ .x) +
  geom_function(fun = ~ (1 + b - m - alpha *.x)*.x ) +
  geom_label() +
  coord_fixed(xlim = c(0, 1000),
                 ylim = c(0, 1000))
ggsave("application_1.png")

# Alternative colorée
ggplot(data = donnee_application) +
  aes(x = actuel,
         y = suivant,
         color = etape) +
  geom_path(size = 0.5, linetype = "dashed", color = "black") +
  geom_function(fun = ~ .x) +
  geom_function(fun = ~ (1 + b - m - alpha *.x)*.x ) +
  geom_point(size = 4) +
  coord_fixed(xlim = c(0, 1000),
                 ylim = c(0, 1000))
ggsave("application_2.png")