# Generate dummy data with 4 dependent variables and 3 independent variables
set.seed(123) # Set a seed for reproducibility
n <- 100 # Sample size
dep_vars <- matrix(rnorm(n*4, mean=5, sd=2), nrow=n) # Generate 4 dependent variables
indep_var1 <- runif(n, 1, 10) # Generate a continuous independent variable
indep_var2 <- rnorm(n, mean=3, sd=1) # Generate another continuous independent variable
indep_var3 <- factor(sample(c("A", "B", "C"), n, replace=TRUE)) # Generate a factor independent variable
data <- data.frame(dep_vars, indep_var1, indep_var2, indep_var3) # Combine into a data frame

# Perform MANOVA analysis
library(car) # Load the car package for MANOVA function
model <- manova(cbind(dep_vars[,1], dep_vars[,2], dep_vars[,3], dep_vars[,4]) ~ indep_var1 + indep_var2 + indep_var3, data=data)
summary(model) # Print the results



# Perform MANOVA analysis using aov() function
dep_vars_mat <- as.matrix(data[,1:4]) # Convert dependent variables to matrix
indep_vars <- data[,5:7] # Extract independent variables
model <- aov(dep_vars_mat ~ indep_var1 + indep_var2 + indep_var3, data=indep_vars)
model <- aov(dep_vars[,4] ~ indep_var1 + indep_var2 + indep_var3, data=indep_vars)

summary(model) # Print the results




########################
# peudocode for final algorithm

for folders exps/+[set 1, set 2, set 3]:
  for folders __exp small network+[0/1/2/5]+observed:
  for all files:
  read in file as json
add columns "nr_of_boids", "chase_time", "nr_neighbors_observed" and "boid_speed"
set all values of nr_neighbors_observed to 0/1/2/5 depending on the folder we are currently in

if filename contains "10":
  set all values of nr_of_boids to 10
else
  set all values to 20

if filename contains "slower":
  set all values of boid speed to 0.0283
else
  set all values to 0.0333

if filename contains "short":
  set all values of chase_time to 10
else
  set all values to 20

append the data to all_data