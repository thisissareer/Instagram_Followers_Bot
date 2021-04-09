# Import
from instapy import InstaPy
from instapy import smart_run

# Login
insta_username = ''
insta_password = ''

session = InstaPy(username=insta_username,
                  password=insta_password)

with smart_run(session):
    session.set_dont_include(["sareer_bot"])

    session.set_do_follow(True, percentage=50)
    session.set_do_comment(True, percentage=50)
    session.set_comments(["hi @{}, have a look", "Great content @{} have a look",
                          ":heart_eyes: :heart_eyes: :heart_eyes: @{}"])
    session.set_quota_supervisor(enabled=True, peak_comments_daily=500, peak_comments_hourly=50, peak_likes_daily=500,
                                 peak_likes_hourly=250, sleep_after=['likes', 'follows'])
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    min_followers=150,
                                    min_following=50)

    session.like_by_tags(['follow_for_followback', 'machine'], amount=10)

session.end()
