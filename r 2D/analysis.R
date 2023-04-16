library(jsonlite)

# Initialize empty data frame to store all data
all_data <- data.frame()


for (x in c(1, 2, 3)) {
  print(x)
}


folders <- c("exps/set 1", "exps/set 2", "exps/set 3")
folders <- c("exps/best set")

# create an empty dataframe to hold all the data
all_data <- data.frame()

# loop over the folders
for (folder in folders) {
  # create a list of subfolder names
  subfolders <- c(paste0(folder, "/__exp small network 0 observed"), 
                  paste0(folder, "/__exp small network 1 observed"),
                  paste0(folder, "/__exp small network 2 observed"),
                  paste0(folder, "/__exp small network 5 observed"))
  # loop over the subfolders
  for (subfolder in subfolders) {
    print(as.numeric(stringr::str_extract_all(subfolder, "[0-9]+")[[1]])[2])
    # get a list of all the JSON files in the subfolder
    json_files <- list.files(subfolder, pattern = "*.json", full.names = TRUE)
    # loop over the JSON files
    for (json_file in json_files) {
      # read in the JSON file as a dataframe
      data <- jsonlite::fromJSON(json_file, simplifyDataFrame = TRUE)
      data <- data.frame(data[c("all_cluster_sizes", "all_pos_deviations", "all_rot_deviations")])
      # add the columns with specified values
      if (folder == "exps/best set") {
        nr_neighbors_observed <- as.numeric(stringr::str_extract_all(subfolder, "[0-9]+")[[1]])[1]
      } else {
        nr_neighbors_observed <- as.numeric(stringr::str_extract_all(subfolder, "[0-9]+")[[1]])[2]
      }
      data$nr_of_boids <- ifelse(grepl("10", json_file), 10, 20)
      data$chase_time <- ifelse(grepl("short", json_file), 10, 20)
      data$boid_speed <- ifelse(grepl("slower", json_file), 0.0283, 0.0333)
      data$nr_neighbors_observed <- nr_neighbors_observed
      # append the data to the all_data dataframe
      all_data <- rbind(all_data, data)
    }
  }
}









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