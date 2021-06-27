# Password_checker

Developed using an API, the project lets us to know whether our password has ever been a part of a data breach. The program uses an API provided by the website https://haveibeenpwned.com/ .To secure the transfer even further, Pwned Passwords implements a k-Anonymity model that allows a password to be searched for by partial hash. 

The first 5 characters of a SHA-1 password hash (not case-sensitive) have to be passed to the API. When a password hash with the same first 5 characters is found in the Pwned Passwords repository, the API will respond with an HTTP 200 and include the suffix of every hash beginning with the specified prefix, followed by a count of how many times it appears in the data set. The API consumer can then search the results of the response for the presence of their source hash and if not found, the password does not exist in the data set.





