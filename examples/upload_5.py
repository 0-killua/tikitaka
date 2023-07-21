from tiktok_uploader.upload import upload_videos
from tiktok_uploader.auth import AuthBackend

videos = [{'video': '../assets/2.mp4', 'description': '#ai   #fyp   #foryoupage   #aitools   #crush   #pics'} for _ in range(5)]

auth = AuthBackend(cookies='../assets/cookies.txt')
failed_videos = upload_videos(videos=videos, auth=auth)

for video in failed_videos: # each input video object which failed
    print(f"{video['video']} with description '{video['description']}' failed")
