from collections import deque
from typing import List, Dict, Set, Deque


__DEBUG__ = True


def log(*args, **kwargs):
    if __DEBUG__:
        print(*args, **kwargs)


class Tweet(object):
    def __init__(self, tweet_id: int, sender_id: int, stamp: int):
        self.tweet_id = tweet_id
        self.sender_id = sender_id
        self.stamp = stamp

    def serialize(self):
        return self.tweet_id, self.sender_id, self.stamp

    def __hash__(self):
        return hash(self.serialize())

    def __eq__(self, other):
        assert type(other) == Tweet
        return self.serialize() == other.serialize()

    def __repr__(self):
        return self.__class__.__name__ + (
            f'({self.tweet_id}, {self.sender_id}, {self.stamp})'
        )


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
        self.feed_set: Dict[int, Set[Tweet]] = {}

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

    def addToFeed(self, userId, tweet: Tweet):
        if userId not in self.feed:
            self.feed[userId] = deque()
            self.feed_set[userId] = set()

        self.feed[userId].appendleft(tweet)
        self.feed_set[userId].add(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        log('GET_NEWS_FEED', userId, self.feed, self.followed)
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
            else:
                print('POP', tweet)

        return [tweet.tweet_id for tweet in recent]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        :param followerId: person who is following
        :param followeeId: person who is being followed
        :return:
        """
        if followeeId not in self.followed:
            self.followed[followeeId] = set()

        self.followed[followeeId].add(followerId)

        if followerId not in self.followers:
            self.followers[followerId] = set()

        self.followers[followerId].add(followeeId)

        if followerId not in self.feed:
            self.feed[followerId] = deque()
            self.feed_set[followerId] = set()

        feed = self.feed[followerId]
        feed_set = self.feed_set[followerId]
        # get history of tweets sent by newly followed user
        log('OLD_FEED', followerId, feed)

        try:
            tweets_history = self.tweets_history[followeeId]
            log('TWEET_HIST', tweets_history)
        except KeyError:
            log('NO_TWEET_HIST')
            return

        sent_tweet_idx = 0
        prev_tweet_stamp = float('inf')
        all_tweets_added = False
        k = 0

        # add new followee tweet history to Twitter feed
        while k < len(feed):
            tweet = feed[k]
            tweet_stamp = tweet.stamp
            sent_tweet = tweets_history[sent_tweet_idx]
            sent_tweet_stamp = sent_tweet.stamp
            new_tweets_added = False

            while prev_tweet_stamp > sent_tweet_stamp > tweet_stamp:
                log('INSERT', k, sent_tweet)
                feed.insert(k, sent_tweet)
                feed_set.add(sent_tweet)
                sent_tweet_idx += 1

                if sent_tweet_idx >= len(tweets_history):
                    all_tweets_added = True
                    break

                new_tweets_added = Tweet
                break

            if all_tweets_added:
                break
            if new_tweets_added:
                continue

            prev_tweet_stamp = tweet_stamp
            k += 1

        # add remaining tweets at tweet history end to feed end
        log('REMAIN', feed)
        while sent_tweet_idx < len(tweets_history):
            sent_tweet = tweets_history[sent_tweet_idx]

            if sent_tweet not in feed_set:
                feed.append(sent_tweet)
                feed_set.add(sent_tweet)

            sent_tweet_idx += 1

        log('NEW_FEED', followerId, feed)
        log('TOTAL_FEED', self.feed)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.followers[followerId].remove(followeeId)
        except KeyError:
            pass

        try:
            self.followed[followeeId].remove(followerId)
            # print('FFF', followerId, self.feed[followerId])
        except KeyError:
            pass


if __name__ == '__main__':
    obj = Twitter()

    commands = ["Twitter","postTweet","follow","follow","getNewsFeed","postTweet","getNewsFeed","getNewsFeed","unfollow","getNewsFeed","getNewsFeed","unfollow","getNewsFeed","getNewsFeed"]
    inputs = [[],[1,5],[1,2],[2,1],[2],[2,6],[1],[2],[2,1],[1],[2],[1,2],[1],[2]]
    results = []

    for command, command_input in zip(commands, inputs):
        print('EXEC', command, command_input)

        if command == 'Twitter':
            results.append([])
            continue

        result = getattr(obj, command)(*command_input)
        results.append(result)

        print('RESULT >', result)
        print('----------------')

    print(results)

# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
