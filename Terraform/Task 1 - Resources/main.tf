resource "local_file" "try" {
  content  = "hey there"
  filename = "./a.txt"
}

resource "local_file" "carzy" {
  content  = "Crazy there"
  filename = "./di/f.txt"
}

resource "local_file" "stan" {
  content  = "Appreciate you bro"
  filename = "./di/s.txt"
}
