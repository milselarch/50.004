from collections import deque
from typing import List, Dict, Set, Deque


class Tweet(object):
    def __init__(self, tweet_id: int, sender_id: int, stamp: int):
        self.sender_id = sender_id
        self.tweet_id = tweet_id
        self.stamp = stamp


class Twitter:
    def __init__(self):
        # maps users to their followers
        self.followers: Dict[int, Set[int]] = {}
        # maps users to all the people who they followed
        self.followed: Dict[int, Set[int]] = {}

        self.tweets_sent: Dict[int, Set[Tweet]] = {}
        self.tweets_history: Dict[int, Deque[Tweet]] = {}

        self.tweet_origin: Dict[int, Tweet] = {}
        self.feed: Dict[int, Deque[Tweet]] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_sent:
            self.tweets_sent[userId] = set()
            self.tweets_history[userId] = deque()

        num_tweets = len(self.tweet_origin)
        tweet = Tweet(tweetId, userId, num_tweets)
        self.tweet_origin[tweetId] = tweet
        self.tweets_sent[userId].add(tweet)
        self.tweets_history[userId].appendleft(tweet)

        followed = self.followed.get(userId, {})
        # add own tweet to feed
        self.addToFeed(userId, tweet)

        # add own tweet to feed of people who followed userId
        for follower in followed:
            self.addToFeed(follower, tweet)

    def addToFeed(self, userId, tweetId):
        if userId not in self.feed:
            self.feed[userId] = deque()

        self.feed[userId].appendleft(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        # print('GET_NEWS_FEED', userId, self.feed[userId], self.followed)
        user_feed = self.feed.get(userId, deque())
        recent = []

        for k in range(len(user_feed)):
            if len(recent) == 10:
                break

            tweet = user_feed[k]
            tweet_creator = self.tweet_origin[tweet.tweet_id].sender_id
            followers_of_tweet = self.followed.get(tweet_creator, set())

            # print('TWC', tweet, tweet_creator)
            if (userId in followers_of_tweet) or (tweet_creator == userId):
                recent.append(tweet)

        return [tweet.sender_id for tweet in recent]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        :param followerId: person who is following
        :param followeeId: person who is being followed
        :return:
        """
        if followeeId not in self.followers:
            self.followed[followeeId] = set()

        self.followed[followeeId].add(followerId)

        if followerId not in self.followers:
            self.followers[followerId] = set()

        self.followers[followerId].add(followeeId)

        feed = self.feed.get(followerId, deque())
        # get history of tweets sent by newly followed user
        tweets_history = self.tweets_history[followerId]
        sent_tweet_idx = 0
        prev_tweet_id = -1
        k = 0

        while k < len(feed):
            tweet = feed[k]
            tweet_id = tweet.tweet_id
            sent_tweet_id = tweets_history[sent_tweet_idx].tweet_id

            while tweet_id > sent_tweet_id > prev_tweet_id:
                raise NotImplementedError

            prev_tweet_id = tweet_id
            k += 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].remove(followeeId)
        self.followed[followeeId].remove(followerId)
        # print('FFF', followerId, self.feed[followerId])


if __name__ == '__main__':
    obj = Twitter()

    commands = ["Twitter", "postTweet", "getNewsFeed", "follow", "getNewsFeed", "unfollow", "getNewsFeed"]
    inputs = [[], [1, 1], [1], [2, 1], [2], [2, 1], [2]]
    results = []

    for command, command_input in zip(commands, inputs):
        print('EXEC', command, command_input)

        if command == 'Twitter':
            results.append([])
            continue

        result = getattr(obj, command)(*command_input)
        results.append(result)

        print('RESULT >', result)

    print(results)

# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
