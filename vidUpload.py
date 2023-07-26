from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
import os
import time
def VidUpload(path):
    # loggin into the channel
    channel = Channel()
    channel.login("client_secret.json", "credentials.storage")
    # Get the filename from the link
    filename = os.path.basename(path)

    # Remove the ".mp4" extension
    title, _ = os.path.splitext(filename)
    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path=path)

    # setting snippet
    video.set_title(title)
    video.set_description(str(time.ctime(time.time())))
    #video.set_tags(["this", "tag"])
    #video.set_category("gaming")
    video.set_default_language("en-US")

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("private")
    video.set_public_stats_viewable(True)

    # setting thumbnail
    #video.set_thumbnail_path('test_thumb.png')

    # uploading video and printing the results
    video = channel.upload_video(video)
    print(video.id)
    #print(video)

    # liking video
    video.like()