from .ai_route import ai_route

def register_blueprints(app):
    # 블루프린트를 리스트로 정의하여 등록
    blueprints = [
        (ai_route, '/api/ai')
    ]
    
    # 각 블루프린트를 등록
    for blueprint, prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=prefix)
