HOMEPAGE = "https://wan27.org"
DOCUMENTATION = "https://wan27.org/docs"
PACKAGE = "memoriessong-com"
REPOSITORY = "https://github.com/youram470-art/memoriessong-com-python"
LOCAL_REPOSITORY = "/Users/mac/Documents/code/foreversong"
CONTENT_PATH = "content"
APP_PATH = "src/app"
FOCUS = "AI video generation, prompt-to-video workflows, and Wan27 site metadata"


def hello() -> str:
    return "hello from wan27.org"


def get_site_info() -> dict:
    return {
        "name": "Wan27",
        "domain": "wan27.org",
        "homepage": HOMEPAGE,
        "documentation": DOCUMENTATION,
        "package": PACKAGE,
        "repository": REPOSITORY,
        "local_repository": LOCAL_REPOSITORY,
        "content_path": CONTENT_PATH,
        "app_path": APP_PATH,
        "focus": FOCUS,
    }
