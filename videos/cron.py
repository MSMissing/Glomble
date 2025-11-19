from .models import Video, recalculate_score
from django.utils import timezone
from datetime import timedelta

def reset_recommendations():
    videos = Video.objects.all()
    for video in videos:
        for i in video.recommendations:
            video.recommendations.remove(i)
    Video.objects.bulk_update(videos, ['recommendations'])

def recalculate_score():
    videos = Video.objects.select_related('uploader').prefetch_related('likes', 'dislikes')
    now = timezone.now()

    for video in videos:
        recalculate_score(video)

    Video.objects.bulk_update(videos, ['score'])
