from flask import Flask, render_template, request

app = Flask(__name__)

# 동영상 데이터 관리
videos = [
    {
        "id": 1,
        "title": "Sample Video 1",
        "file": "video1.mp4",
        "thumbnail": "thumbnails/sample1.jpg",
        "tags": ["Tag1", "Tag2"],
        "category": "Category1"
    },
    {
        "id": 2,
        "title": "Sample Video 2",
        "file": "video/sample2.mp4",
        "thumbnail": "thumbnails/sample2.jpg",
        "tags": ["Tag3", "Tag4"],
        "category": "Category2"
    },
    # 추가 동영상 데이터 ...
]

@app.route('/')
def index():
    category_filter = request.args.get('category')
    tag_filter = request.args.get('tag')

    filtered_videos = videos
    if category_filter:
        filtered_videos = [video for video in filtered_videos if video["category"] == category_filter]
    if tag_filter:
        filtered_videos = [video for video in filtered_videos if tag_filter in video["tags"]]

    categories = list(set(video["category"] for video in videos))
    tags = list(set(tag for video in videos for tag in video["tags"]))

    return render_template('index.html', videos=filtered_videos, categories=categories, tags=tags)

@app.route('/player/<int:video_id>')
def player(video_id):
    current_video = next((video for video in videos if video["id"] == video_id), None)
    if not current_video:
        return "Video not found", 404

    # 관련 동영상 (주변 동영상)
    start_index = max(0, video_id - 5)
    end_index = min(len(videos), video_id + 5)
    related_videos = videos[start_index:end_index]

    return render_template('player.html', video=current_video, related_videos=related_videos)

if __name__ == '__main__':
    app.run(debug=True)
