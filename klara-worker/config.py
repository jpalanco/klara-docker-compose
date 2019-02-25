# Setup the loglevel
logging_level  = "debug"

# Api location for Dispatcher. No trailing slash !!
# Dispatcher is exposing the API at "/api/" location
api_location = "http://klara-dispatcher:8888/api"
# The API key set up in the `agents` SQL table
api_key      = "test"

# Specify worker refresh time in seconds
refresh_new_jobs    = 60

# Yara settings
# Set-up path for Yara binary
yara_path           = "/opt/yara-latest/bin/yara"
# Use 8 threads to scan and scan dirs recursively
yara_extra_args     = "-p 8 -r"
# Where to store Yara temp results file
yara_temp_dir       = "/tmp/"

# md5sum settings
# binary location
md5sum_path         = "/usr/bin/md5sum"

# tail settings
# We only want the first 1k results
head_path_and_args  = ["/usr/bin/head", "-1000"]

# Virus collection should NOT have a trailing slash !!
virus_collection                = "/var/projects/klara/repository"
virus_collection_control_file   = "repo_ctrl.txt"

