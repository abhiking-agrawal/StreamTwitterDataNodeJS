#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = 'HTNc6rm4tX63VYQKWQCV40TFm'
consumer_secret = 'bAWS75kNkDMKrWvGvzoGVYrRdjrtrZk7BaPwTBcBzdpfdHr0Il'
access_token = '969603656080330753-ucYDl5fW5aJmzT2AJIuR6wtKaa8Jf7A'
access_token_secret = 'HrI9XHNBqtQ0xxouDPqeY6OOOzLav1moLk1BgP7l29an9'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#women'])