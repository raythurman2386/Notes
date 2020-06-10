# https://www.hackerrank.com/challenges/strange-advertising/problem
# Viral Advertising

"""
Hackerland enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly 5 people on social media.

On the first day, half of those 5 people(i.e., floor(5/2) == 2) like the advertisement and each shares it with 3 of their friends. At the beginning of the second day, (floor(5/2) * 3 = 2 * 3 = 6) people receive the advertisement.

Each day, (floor recipients/2) of the recipients like the advertisement and will share it with 3 friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.
"""

def viral_advertising(n):
    total_likes = 0
    days = [day for day in range(1, n + 1)]
    print(days)
    # TODO: Day 1 always has 5 recipients
    # TODO: Find how many share on day one like = 5//2
    # TODO: Half of those recipients share with 3 friends 
    #     new_recipients = like * 3
    #     like = new_recipients // 2
    # TODO: Rinse and repeat till no more days
    # TODO: Possible recursion implementation
    # 3 days should equal 9 total likes
    # Day 1 - 2 likes - 5 recipients
    # Day 2 - 3 likes - 6 recipients
    # Day 3 - 4 likes - 9 recipients

viral_advertising(3)